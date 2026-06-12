---
description: Compute WACC with a peer-beta build-up and sensitivity grid
argument-hint: <peer file or inputs: betas, D/E, tax, rf, ERP, cost of debt>
---
Use the wacc-computation skill in skills/wacc-computation/SKILL.md.

Inputs: $ARGUMENTS

Requirements:
- Unlever each peer at its own D/E and tax (Hamada), relever the median at the target structure — use skills/wacc-computation/scripts/calculate.py
- Market-value weights; marginal (not historical) cost of debt
- Check currency consistency between rates and cash flows
- Output using skills/wacc-computation/assets/wacc-memo-template.md including the sensitivity matrix
