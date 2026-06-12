---
description: Run a full ratio and trend analysis on financial statements (file path or pasted figures)
argument-hint: <path-to-statements.csv/xlsx or pasted figures>
---
Use the financial-analysis skill in skills/financial-analysis/SKILL.md.

Analyze the financial statements provided here: $ARGUMENTS

Requirements:
- Import functions from skills/financial-analysis/scripts/calculate.py — do not do mental math
- Use average balances for ROE/DSO where two periods are available
- Follow skills/financial-analysis/assets/analysis-memo-template.md for the output
- Flag anything growing materially faster than revenue
