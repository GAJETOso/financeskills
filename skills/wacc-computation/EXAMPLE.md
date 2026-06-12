# Worked Example - wacc-computation

## Ask

> Our stock beta is 1.2, the 10-year Treasury is at 4%, and the Equity Risk Premium is 5%. We have $1M in debt at 6% interest and $2M in market cap. Tax rate is 25%. What's our WACC?

## What a correct response contains

Should calculate Cost of Equity (4% + 1.2 * 5% = 10%). Should calculate After-tax Cost of Debt (6% * (1 - 0.25) = 4.5%). Should weight the components (1/3 Debt, 2/3 Equity). Should calculate the final WACC ((1/3 * 4.5%) + (2/3 * 10%) = 8.16%). Should provide a WACC Computation Memo.

## File-driven variant

With fixture(s) `evals/files/comparables.csv`:

> Using the attached peer set (evals/files/comparables.csv), estimate WACC for a target with: target D/E 0.60, tax rate 30%, risk-free rate 4.5%, ERP 5.5%, pre-tax cost of debt 8.5%. Unlever each peer at its own structure, take the median unlevered beta, relever at the target structure, and produce your WACC Computation Memo.

Expected: Median unlevered beta approx 0.833; relevered beta approx 1.183; cost of equity approx 11.01%; weights 62.5% equity / 37.5% debt; WACC approx 9.11%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
