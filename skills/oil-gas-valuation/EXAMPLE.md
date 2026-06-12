# Worked Example - oil-gas-valuation

## Ask

> We have 1 million barrels of proved reserves. Lifting costs are $15/bbl. Current oil price is $80/bbl. What's the PV-10 assuming a 10-year production life?

## What a correct response contains

Should calculate annual production (100k bbl/yr). Should calculate annual net cash flow ($80 - $15 = $65/bbl * 100k = $6.5M/yr). Should discount the 10-year annuity at 10% to find PV-10 (approx. $39.9M). Should provide an Oil & Gas Valuation Memo.

## File-driven variant

With fixture(s) `evals/files/field_parameters.csv`:

> Value the field described in the attached parameters (evals/files/field_parameters.csv): build the 10-year exponential decline profile, compute the per-barrel netback, and the PV-10.

Expected: Netback $41.50/bbl; year-10 production 387,420 bbl; PV-10 $179,605,644.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
