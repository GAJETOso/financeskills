# Eval Baseline

![evals](https://img.shields.io/badge/evals-pending_first_run-lightgrey)

**Status: no baseline run published yet.** All 43 skills have runnable evals
(184 evals, every skill includes at least one file-based eval with realistic
fixtures and code-verified expected values), but the scored run requires a
model API key.

## Publish the first baseline

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 tools/evals/run_evals.py --all          # ~30-60 min, writes results/
python3 tools/evals/make_baseline.py            # regenerates this file + badge
```

Or trigger the **eval-baseline** GitHub Action (workflow_dispatch) after adding
`ANTHROPIC_API_KEY` to the repository secrets - it runs the suite and commits
the scorecard.

Until then, `python3 tools/evals/run_evals.py --dry-run` verifies all schemas
and fixtures offline (runs in CI on every push).
