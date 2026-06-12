---
description: Run the full month-end close - entries, reconciliations, statements, review pack
argument-hint: <period, e.g. "May 2026"> <data files: TB, bank stmt, GL cash, payroll, asset register...>
---
Execute the orchestrated close in workflows/month-end-close.md for: $ARGUMENTS

Work phase by phase (Plan -> Entries -> Reconciliations -> Statements -> Review pack).
Do not start a phase until the prior phase's gate is met; state each gate check.
Use each phase's skill (skills/<name>/SKILL.md), compute exclusively with their
scripts/calculate.py functions, and format outputs on their assets/ templates.
If an input file is missing for a phase, list exactly what is needed and pause
that phase rather than estimating silently.
