---
description: Allocate a contract's transaction price to performance obligations (IFRS 15 / ASC 606)
argument-hint: <contract file or terms: POs, stated prices, SSPs, timing>
---
Use the revenue-recognition skill in skills/revenue-recognition/SKILL.md.

Contract details: $ARGUMENTS

Requirements:
- Relative-SSP allocation via skills/revenue-recognition/scripts/calculate.py; allocation must tie to the transaction price exactly
- Build the recognition schedule (point-in-time vs over-time per PO)
- State period-end contract asset/liability position
- Output using skills/revenue-recognition/assets/allocation-workpaper-template.md
