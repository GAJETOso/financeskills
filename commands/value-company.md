---
description: DCF valuation with terminal value and EV-to-equity bridge
argument-hint: <FCF projections, WACC, growth/exit multiple, net debt>
---
Use the company-valuation skill in skills/company-valuation/SKILL.md.

Inputs: $ARGUMENTS

Requirements:
- Discount with skills/company-valuation/scripts/calculate.py; cross-check Gordon terminal value against an exit multiple
- Show the EV -> equity bridge (net debt, minorities)
- Sensitivity: WACC +/-1%, terminal growth +/-0.5%
- State which inputs are assumptions vs provided facts
