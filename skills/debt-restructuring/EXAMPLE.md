# Worked Example - debt-restructuring

## Ask

> Our company has $10M in debt and only $500k in annual EBITDA. We can't pay the interest. What are our options?

## What a correct response contains

Should identify a severe solvency crisis. Should suggest a 'Haircut' or a 'Debt-for-Equity Swap'. Should discuss recovery values in restructuring vs liquidation. Should provide a Restructuring Proposal structure.

## File-driven variant

With fixture(s) `evals/files/capital_structure.csv`:

> Run the priority waterfall in the attached capital structure (evals/files/capital_structure.csv) at the stated distributable enterprise value. Recovery $ and % per tranche, and identify the fulcrum security.

Expected: Senior secured 100% ($500m); senior unsecured 75% ($300m); subs 0%. Fulcrum = senior unsecured.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
