---
description: Run forensic analytics (Benford's law, round-number ratio) on a transaction population
argument-hint: <path to transactions file> [amount column]
---
Use the forensic-accounting skill in skills/forensic-accounting/SKILL.md.

Population: $ARGUMENTS

Requirements:
- Run benford_test and round_number_ratio from skills/forensic-accounting/scripts/calculate.py
- Report the chi-square statistic against the 15.507 critical value (8 df, 5%)
- A flag is an anomaly indicator, NOT proof of fraud — say so explicitly
- Recommend targeted follow-up procedures for flagged digit ranges
