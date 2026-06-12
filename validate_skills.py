#!/usr/bin/env python3
"""FinanceSkills repository validator.

Enforces the Agent Skills spec documented in AGENTS.md:
  - skill directory naming rules (lowercase, hyphens, no '--', no edge hyphens)
  - SKILL.md present with valid YAML frontmatter; name matches directory;
    description 1-1024 chars; file under 500 lines
  - evals/evals.json present, valid schema, fixture files exist
  - all relative links in SKILL.md resolve
  - every scripts/calculate.py self-test passes
  - marketplace manifests list exactly the skills on disk
  - no compiled Python artifacts committed

Usage: python3 validate_skills.py [--no-selftests]
Exit code 0 = clean, 1 = problems found.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
SKILLS = REPO / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((\.{1,2}/[^)#]+)\)")
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str) -> dict | None:
    """Minimal frontmatter parser (avoids a yaml dependency)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm: dict = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def check_skill(d: Path) -> None:
    name = d.name
    if not NAME_RE.match(name) or len(name) > 64:
        err(f"{name}: invalid skill directory name")

    sk = d / "SKILL.md"
    if not sk.exists():
        err(f"{name}: missing SKILL.md")
        return
    text = sk.read_text(encoding="utf-8", errors="replace")
    lines = text.count("\n") + 1
    if lines > 500:
        err(f"{name}: SKILL.md is {lines} lines (limit 500)")

    fm = parse_frontmatter(text)
    if fm is None:
        err(f"{name}: SKILL.md missing YAML frontmatter")
    else:
        if fm.get("name") != name:
            err(f"{name}: frontmatter name '{fm.get('name')}' != directory name")
        desc = fm.get("description", "")
        if not 1 <= len(desc) <= 1024:
            err(f"{name}: description length {len(desc)} outside 1-1024")

    # relative links must resolve
    for rel in LINK_RE.findall(text):
        if not (d / rel).resolve().exists():
            err(f"{name}: dead link in SKILL.md -> {rel}")

    # evals schema
    ef = d / "evals" / "evals.json"
    if not ef.exists():
        err(f"{name}: missing evals/evals.json")
    else:
        try:
            spec = json.loads(ef.read_text())
            if spec.get("skill_name") != name:
                err(f"{name}: evals skill_name mismatch")
            evs = spec.get("evals", [])
            if not evs:
                err(f"{name}: evals.json has no evals")
            for ev in evs:
                for field in ("id", "prompt", "expected_output", "assertions"):
                    if not ev.get(field):
                        err(f"{name} eval {ev.get('id', '?')}: missing '{field}'")
                for rel in ev.get("files", []):
                    if not (d / rel).exists():
                        err(f"{name} eval {ev.get('id')}: fixture missing -> {rel}")
        except json.JSONDecodeError as e:
            err(f"{name}: evals.json invalid JSON ({e})")


def check_selftests() -> None:
    for script in sorted(SKILLS.glob("*/scripts/*.py")):
        r = subprocess.run([sys.executable, str(script)], capture_output=True,
                           text=True, timeout=120)
        if r.returncode != 0:
            err(f"self-test failed: {script.relative_to(REPO)}\n    {r.stderr.strip().splitlines()[-1] if r.stderr else ''}")


def check_marketplaces(skill_names: set[str]) -> None:
    root_mp = REPO / "marketplace.json"
    if root_mp.exists():
        data = json.loads(root_mp.read_text())
        listed = {s["id"] for s in data.get("marketplace", data).get("skills", [])} \
            if "marketplace" in data or "skills" in data else set()
        if not listed:  # tolerate alternate shape
            listed = {s.get("id") for s in data.get("skills", [])}
        missing = skill_names - listed
        extra = listed - skill_names - {None}
        if missing:
            warnings.append(f"marketplace.json missing skills: {sorted(missing)}")
        if extra:
            warnings.append(f"marketplace.json lists unknown skills: {sorted(extra)}")


def check_cc_marketplace(skill_names: set[str]) -> None:
    mp = REPO / ".claude-plugin" / "marketplace.json"
    if not mp.exists():
        return
    data = json.loads(mp.read_text())
    listed = set()
    for plugin in data.get("plugins", []):
        for path in plugin.get("skills", []):
            listed.add(path.rstrip("/").split("/")[-1])
    missing = skill_names - listed
    extra = listed - skill_names
    if missing:
        warnings.append(f".claude-plugin/marketplace.json missing skills: {sorted(missing)}")
    if extra:
        warnings.append(f".claude-plugin/marketplace.json lists unknown skills: {sorted(extra)}")


def check_artifacts() -> None:
    junk = [p for p in REPO.rglob("*.pyc") if ".git" not in p.parts]
    junk += [p for p in REPO.rglob("__pycache__") if ".git" not in p.parts]
    for p in junk:
        err(f"compiled artifact committed: {p.relative_to(REPO)}")


def check_manifest() -> None:
    import subprocess as sp
    r = sp.run([sys.executable, str(REPO / "tools" / "security" / "manifest.py"),
                "--verify"], capture_output=True, text=True)
    if r.returncode != 0:
        warnings.append("MANIFEST.sha256 out of date - run python3 tools/security/manifest.py")


def main() -> None:
    run_selftests = "--no-selftests" not in sys.argv
    dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    for d in dirs:
        check_skill(d)
    if run_selftests:
        check_selftests()
    names = {d.name for d in dirs}
    check_marketplaces(names)
    check_cc_marketplace(names)
    check_artifacts()
    check_manifest()

    n_scripts = len(list(SKILLS.glob("*/scripts/*.py")))
    print(f"Checked {len(dirs)} skills, {n_scripts} scripts.")
    for w in warnings:
        print(f"  WARN  {w}")
    if errors:
        for e in errors:
            print(f"  ERROR {e}")
        print(f"\n{len(errors)} error(s).")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
