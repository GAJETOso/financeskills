#!/usr/bin/env python3
"""Convert the most recent eval run into tools/evals/BASELINE.md + a README badge line."""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
runs = sorted((HERE / "results").glob("*/results.json")) if (HERE / "results").exists() else []
if not runs:
    sys.exit("No eval results found. Run: python3 tools/evals/run_evals.py --all")
latest = runs[-1]
data = json.loads(latest.read_text())
stamp = latest.parent.name

rows, total, passed = [], 0, 0
for r in data:
    n = len(r["results"]); p = sum(x["passed"] for x in r["results"])
    total += n; passed += p
    rows.append(f"| {r['skill']} | {p}/{n} | {'PASS' if p == n else 'FAIL'} |")

pct = 100 * passed / total if total else 0
badge = f"![evals](https://img.shields.io/badge/evals-{passed}%2F{total}_passing_({pct:.0f}%25)-{'brightgreen' if pct >= 90 else 'yellow' if pct >= 70 else 'red'})"
md = f"""# Eval Baseline

{badge}

**Run:** {stamp} | **Model:** see run config | **Result: {passed}/{total} evals passing ({pct:.0f}%)**

Reproduce: `ANTHROPIC_API_KEY=... python3 tools/evals/run_evals.py --all`

| Skill | Passed | Status |
|---|---|---|
{chr(10).join(rows)}

Raw output: `tools/evals/results/{stamp}/`
"""
(HERE / "BASELINE.md").write_text(md)
print(f"BASELINE.md written: {passed}/{total} ({pct:.0f}%)")
print(f"Badge line for README:\n{badge}")
