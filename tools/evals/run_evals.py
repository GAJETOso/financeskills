#!/usr/bin/env python3
"""FinanceSkills eval runner.

Feeds each eval prompt (plus any fixture files) to an agent backend with the
skill's SKILL.md as system context, then grades the response against the
eval's assertions using an LLM judge.

Backends:
  api   - Anthropic Messages API (requires ANTHROPIC_API_KEY). Default.
  cli   - `claude -p` (Claude Code CLI must be on PATH).
  dry   - no model calls; validates schema and fixture files only.

Usage:
  python3 tools/evals/run_evals.py --dry-run                 # validate all
  python3 tools/evals/run_evals.py --skill wacc-computation  # run one skill
  python3 tools/evals/run_evals.py --all                     # run everything
  python3 tools/evals/run_evals.py --all --backend cli

Results land in tools/evals/results/<timestamp>/ as JSON + Markdown.
Exit code is non-zero if any eval fails (CI-friendly).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO / "skills"
RESULTS_DIR = Path(__file__).resolve().parent / "results"
MODEL = os.environ.get("FINANCESKILLS_EVAL_MODEL", "claude-sonnet-4-6")
JUDGE_MODEL = os.environ.get("FINANCESKILLS_JUDGE_MODEL", MODEL)
MAX_FILE_CHARS = 20_000

JUDGE_SYSTEM = (
    "You are a strict grader for finance-skill evaluations. You receive a task "
    "prompt, an agent's response, and a list of assertions. For each assertion, "
    "decide if the response satisfies it. Numeric assertions tolerate rounding "
    "differences of less than 1% relative error. Reply ONLY with JSON: "
    '{"results": [{"assertion": str, "pass": bool, "reason": str}]}'
)


def call_api(system: str, user: str, model: str) -> str:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("ANTHROPIC_API_KEY not set. Use --backend cli or --dry-run.")
    body = json.dumps({
        "model": model,
        "max_tokens": 4096,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.loads(resp.read())
    return "".join(b.get("text", "") for b in data.get("content", []))


def call_cli(system: str, user: str, model: str) -> str:
    prompt = f"<system-context>\n{system}\n</system-context>\n\n{user}"
    out = subprocess.run(
        ["claude", "-p", "--model", model, prompt],
        capture_output=True, text=True, timeout=600,
    )
    if out.returncode != 0:
        raise RuntimeError(f"claude CLI failed: {out.stderr[:500]}")
    return out.stdout



def render_xlsx(fp: Path) -> str:
    """Render an xlsx fixture as CSV-style text (requires openpyxl)."""
    import openpyxl  # only needed when a fixture is an Excel file
    wb = openpyxl.load_workbook(fp, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"### Sheet: {ws.title}")
        for row in ws.iter_rows(values_only=True):
            out.append(",".join("" if c is None else str(c) for c in row))
    return "\n".join(out)


def build_user_prompt(skill_dir: Path, ev: dict) -> str:
    parts = [ev["prompt"]]
    for rel in ev.get("files", []):
        fp = (skill_dir / rel).resolve()
        if not str(fp).startswith(str(skill_dir.resolve())):
            raise ValueError(f"fixture path escapes skill dir: {rel}")
        if fp.suffix.lower() in (".xlsx", ".xls"):
            content = render_xlsx(fp)[:MAX_FILE_CHARS]
        else:
            content = fp.read_text(errors="replace")[:MAX_FILE_CHARS]
        parts.append(f"\n--- Attached file: {rel} ---\n{content}")
    return "\n".join(parts)


def judge(call, prompt: str, response: str, assertions: list[str]) -> list[dict]:
    user = (
        f"TASK PROMPT:\n{prompt}\n\nAGENT RESPONSE:\n{response}\n\n"
        f"ASSERTIONS:\n{json.dumps(assertions, indent=2)}"
    )
    raw = call(JUDGE_SYSTEM, user, JUDGE_MODEL)
    start, end = raw.find("{"), raw.rfind("}")
    parsed = json.loads(raw[start:end + 1])
    return parsed["results"]


def validate_eval_file(skill_dir: Path) -> list[str]:
    """Schema + fixture checks. Returns list of error strings."""
    errors = []
    ef = skill_dir / "evals" / "evals.json"
    if not ef.exists():
        return [f"{skill_dir.name}: missing evals/evals.json"]
    try:
        spec = json.loads(ef.read_text())
    except json.JSONDecodeError as e:
        return [f"{skill_dir.name}: invalid JSON ({e})"]
    if spec.get("skill_name") != skill_dir.name:
        errors.append(f"{skill_dir.name}: skill_name '{spec.get('skill_name')}' != dir name")
    evals = spec.get("evals", [])
    if not evals:
        errors.append(f"{skill_dir.name}: no evals defined")
    for ev in evals:
        eid = ev.get("id", "?")
        for field in ("prompt", "expected_output", "assertions"):
            if not ev.get(field):
                errors.append(f"{skill_dir.name} eval {eid}: missing '{field}'")
        for rel in ev.get("files", []):
            if not (skill_dir / rel).exists():
                errors.append(f"{skill_dir.name} eval {eid}: fixture not found: {rel}")
    return errors


def run_skill(skill_dir: Path, call) -> dict:
    spec = json.loads((skill_dir / "evals" / "evals.json").read_text())
    system = (skill_dir / "SKILL.md").read_text()
    results = []
    for ev in spec.get("evals", []):
        user = build_user_prompt(skill_dir, ev)
        try:
            response = call(system, user, MODEL)
            graded = judge(call, user, response, ev["assertions"])
            passed = all(g["pass"] for g in graded)
        except Exception as e:  # noqa: BLE001 - record and continue
            response, graded, passed = f"<error: {e}>", [], False
        results.append({
            "id": ev.get("id"), "passed": passed,
            "assertions": graded, "response": response,
        })
        n_ok = sum(g["pass"] for g in graded)
        print(f"  eval {ev.get('id')}: {'PASS' if passed else 'FAIL'} "
              f"({n_ok}/{len(ev['assertions'])} assertions)")
    return {"skill": skill_dir.name, "results": results}


def write_report(all_results: list[dict]) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = RESULTS_DIR / stamp
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(all_results, indent=2))
    lines = [f"# Eval run {stamp}", "", "| Skill | Evals | Passed |", "|---|---|---|"]
    for r in all_results:
        n = len(r["results"])
        p = sum(x["passed"] for x in r["results"])
        lines.append(f"| {r['skill']} | {n} | {p} |")
    (out / "report.md").write_text("\n".join(lines) + "\n")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skill", help="run a single skill by name")
    ap.add_argument("--all", action="store_true", help="run every skill")
    ap.add_argument("--backend", choices=["api", "cli"], default="api")
    ap.add_argument("--dry-run", action="store_true",
                    help="validate eval schemas and fixtures without model calls")
    args = ap.parse_args()

    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if args.skill:
        dirs = [d for d in dirs if d.name == args.skill]
        if not dirs:
            sys.exit(f"skill not found: {args.skill}")

    errors = [e for d in dirs for e in validate_eval_file(d)]
    if errors:
        print("Schema/fixture errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"Schemas OK for {len(dirs)} skill(s).")
    if args.dry_run:
        return
    if not (args.skill or args.all):
        sys.exit("Specify --skill NAME, --all, or --dry-run.")

    call = call_api if args.backend == "api" else call_cli
    all_results = [run_skill(d, call) for d in dirs]
    out = write_report(all_results)
    total = sum(len(r["results"]) for r in all_results)
    passed = sum(x["passed"] for r in all_results for x in r["results"])
    print(f"\n{passed}/{total} evals passed. Report: {out}")
    if passed < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
