# Worked Example - company-valuation

## Ask

> Value this company: FCF next year 100M growing 10% for 5 years then 3% terminal; WACC 12%. Net debt 250M. 50M shares. What's the per-share value?

## What a correct response contains

Explicit FCFs years 1-5 (100, 110, 121, 133.1, 146.41), TV at end of year 5 = 146.41x1.03/(0.12-0.03) = 1,675.5; discount all at 12% -> EV ~ 1,395M; equity = ~1,145M; ~22.9/share. Numbers verified by code; TV share of EV (~68%) noted.

## File-driven variant

With fixture(s) `evals/files/fcf_projections.csv`:

> Run a DCF on the attached projections (evals/files/fcf_projections.csv): discount the five FCF years at the stated WACC, compute Gordon terminal value, enterprise value, and bridge to equity value using net debt.

Expected: Terminal value $185,705,882; EV $156,614,561; equity value $128,614,561.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
