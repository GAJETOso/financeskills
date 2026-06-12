#!/usr/bin/env python3
"""FinanceSkills MCP server (stdio, stdlib-only - no pip installs needed).

Exposes:
  - every public function in skills/*/scripts/calculate.py as a callable tool
    (named <skill>__<function>, e.g. lease_accounting__lease_liability)
  - meta tools: list_skills, get_skill, list_standards, get_standard, get_template

Run:        python3 tools/mcp/server.py
Configure:  see tools/mcp/README.md for Claude Code / Cursor / Codex snippets.

Security: this server reads repo files and runs the repo's own deterministic
calculators. It makes no network calls and never executes caller-supplied code.
"""
from __future__ import annotations

import dataclasses
import importlib.util
import inspect
import json
import sys
import typing
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILLS = REPO / "skills"
STANDARDS = REPO / "standards"
PROTOCOL = "2025-06-18"

TYPE_MAP = {float: "number", int: "integer", str: "string", bool: "boolean",
            list: "array", dict: "object"}


def _schema_for(annotation) -> dict:
    origin = getattr(annotation, "__origin__", None)
    if origin is list:
        return {"type": "array"}
    if origin is dict:
        return {"type": "object"}
    if dataclasses.is_dataclass(annotation):
        props = {f.name: _schema_for(f.type if not isinstance(f.type, str) else str)
                 for f in dataclasses.fields(annotation)}
        return {"type": "object", "properties": props}
    return {"type": TYPE_MAP.get(annotation, "string")} if annotation in TYPE_MAP \
        else {"type": "number"} if annotation is inspect.Parameter.empty else \
        {"type": TYPE_MAP.get(annotation, "string")}


def load_calculators() -> dict[str, dict]:
    """Returns {tool_name: {fn, doc, schema, skill}}."""
    tools: dict[str, dict] = {}
    for script in sorted(SKILLS.glob("*/scripts/calculate.py")):
        skill = script.parent.parent.name
        modname = "calc_" + skill.replace("-", "_")
        spec = importlib.util.spec_from_file_location(modname, script)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[modname] = mod   # required for @dataclass in spec-loaded modules
        try:
            spec.loader.exec_module(mod)
        except Exception as e:  # noqa: BLE001
            print(f"warn: failed loading {script}: {e}", file=sys.stderr)
            continue
        for name, fn in inspect.getmembers(mod, inspect.isfunction):
            if name.startswith("_") or fn.__module__ != modname:
                continue
            sig = inspect.signature(fn)
            try:
                hints = typing.get_type_hints(fn)
            except Exception:  # noqa: BLE001
                hints = {}
            for pname, p in sig.parameters.items():
                pass
            props, required = {}, []
            for pname, p in sig.parameters.items():
                props[pname] = _schema_for(hints.get(pname, p.annotation))
                if p.default is inspect.Parameter.empty:
                    required.append(pname)
            tool_name = f"{skill.replace('-', '_')}__{name}"
            tools[tool_name] = {
                "fn": fn, "skill": skill,
                "doc": inspect.getdoc(fn) or name,
                "schema": {"type": "object", "properties": props,
                           "required": required},
            }
    return tools


CALC = load_calculators()

META = {
    "list_skills": {
        "doc": "List all FinanceSkills with their trigger descriptions.",
        "schema": {"type": "object", "properties": {}, "required": []},
    },
    "get_skill": {
        "doc": "Return the full SKILL.md instructions for a skill (use list_skills for names).",
        "schema": {"type": "object",
                   "properties": {"name": {"type": "string"}}, "required": ["name"]},
    },
    "list_standards": {
        "doc": "List available accounting/auditing standards summaries (IFRS, IAS, US GAAP ASC, IPSAS, ISA, Basel, ESG...).",
        "schema": {"type": "object", "properties": {}, "required": []},
    },
    "get_standard": {
        "doc": "Return a standards summary, e.g. family='ifrs', name='ifrs-16'. Summaries carry an as_of date - verify before decision-grade use.",
        "schema": {"type": "object",
                   "properties": {"family": {"type": "string"}, "name": {"type": "string"}},
                   "required": ["family", "name"]},
    },
    "get_template": {
        "doc": "Return an output template from a skill's assets/, e.g. skill='wacc-computation'.",
        "schema": {"type": "object",
                   "properties": {"skill": {"type": "string"}}, "required": ["skill"]},
    },
}


def meta_call(name: str, args: dict) -> str:
    if name == "list_skills":
        out = []
        for d in sorted(SKILLS.iterdir()):
            sk = d / "SKILL.md"
            if sk.exists():
                desc = ""
                for line in sk.read_text().splitlines():
                    if line.startswith("description:"):
                        desc = line[12:].strip()
                        break
                out.append(f"- {d.name}: {desc[:200]}")
        return "\n".join(out)
    if name == "get_skill":
        p = (SKILLS / args["name"] / "SKILL.md").resolve()
        if not p.is_relative_to(SKILLS) or not p.exists():
            raise ValueError(f"unknown skill: {args['name']}")
        return p.read_text()
    if name == "list_standards":
        return "\n".join(f"- {p.parent.name}/{p.stem}"
                         for p in sorted(STANDARDS.rglob("*.md")))
    if name == "get_standard":
        p = (STANDARDS / args["family"] / f"{args['name']}.md").resolve()
        if not p.is_relative_to(STANDARDS) or not p.exists():
            raise ValueError(f"unknown standard: {args['family']}/{args['name']}")
        return p.read_text()
    if name == "get_template":
        d = (SKILLS / args["skill"] / "assets").resolve()
        if not d.is_relative_to(SKILLS) or not d.exists():
            raise ValueError(f"no assets for skill: {args['skill']}")
        return "\n\n".join(p.read_text() for p in sorted(d.glob("*.md")))
    raise ValueError(f"unknown tool: {name}")


def coerce_args(fn, args: dict) -> dict:
    """Build dataclass params from dicts where the signature expects one."""
    try:
        hints = typing.get_type_hints(fn)
    except Exception:  # noqa: BLE001
        hints = {}
    out = {}
    for pname in inspect.signature(fn).parameters:
        if pname not in args:
            continue
        v = args[pname]
        ann = hints.get(pname)
        if ann is not None and dataclasses.is_dataclass(ann) and isinstance(v, dict):
            v = ann(**v)
        out[pname] = v
    return out


def tool_result(value) -> dict:
    if dataclasses.is_dataclass(value):
        value = dataclasses.asdict(value)
    text = value if isinstance(value, str) else json.dumps(value, default=str, indent=2)
    return {"content": [{"type": "text", "text": text}]}


def handle(req: dict) -> dict | None:
    method, rid = req.get("method"), req.get("id")
    if method == "initialize":
        result = {"protocolVersion": PROTOCOL,
                  "capabilities": {"tools": {}},
                  "serverInfo": {"name": "financeskills", "version": "1.0.1"}}
    elif method in ("notifications/initialized", "notifications/cancelled"):
        return None
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        tools = [{"name": n, "description": f"[{m['skill']}] {m['doc']}",
                  "inputSchema": m["schema"]} for n, m in CALC.items()]
        tools += [{"name": n, "description": m["doc"], "inputSchema": m["schema"]}
                  for n, m in META.items()]
        result = {"tools": tools}
    elif method == "tools/call":
        name = req["params"]["name"]
        args = req["params"].get("arguments", {})
        try:
            if name in META:
                result = tool_result(meta_call(name, args))
            elif name in CALC:
                fn = CALC[name]["fn"]
                result = tool_result(fn(**coerce_args(fn, args)))
            else:
                raise ValueError(f"unknown tool: {name}")
        except Exception as e:  # noqa: BLE001
            result = {"content": [{"type": "text", "text": f"Error: {e}"}],
                      "isError": True}
    else:
        if rid is None:
            return None
        return {"jsonrpc": "2.0", "id": rid,
                "error": {"code": -32601, "message": f"method not found: {method}"}}
    if rid is None:
        return None
    return {"jsonrpc": "2.0", "id": rid, "result": result}


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            resp = handle(json.loads(line))
        except json.JSONDecodeError:
            continue
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
