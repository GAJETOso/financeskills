# Worked Example - lbo-modeling

## Ask

> We want to buy a company for $100M (10x EBITDA). We are using $60M in debt and $40M in equity. If we exit in 5 years at the same multiple, what's our IRR?

## What a correct response contains

Should calculate the entry EBITDA ($10M). Should identify the need for cash flow projections to pay down debt. Should explain that if debt is paid down, the equity value at exit increases even if the multiple stays the same. Should provide an LBO Analysis Summary structure.

## File-driven variant

With fixture(s) `evals/files/lbo_assumptions.xlsx`:

> Run the LBO described in the attached assumptions workbook (evals/files/lbo_assumptions.xlsx). Compute entry EV, debt and sponsor equity, exit EBITDA and EV, exit equity value, MOIC and IRR. Debt is a bullet (no paydown); ignore cash generation.

Expected: Entry EV $400m, debt $240m, equity $160m. Exit EBITDA $73.5m, exit EV $588m, exit equity $348m. MOIC 2.17x, IRR 16.8%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
