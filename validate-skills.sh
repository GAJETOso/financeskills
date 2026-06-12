#!/bin/bash
# FinanceSkills validation - delegates to the Python validator, which enforces
# the full Agent Skills spec (frontmatter, evals schema, links, self-tests).
set -e
cd "$(dirname "$0")"
python3 validate_skills.py "$@"
python3 tools/evals/run_evals.py --dry-run
