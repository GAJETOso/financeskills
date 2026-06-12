# Worked Example - credit-analysis

## Ask

> Borrower requests a 500M term loan, 5 years. EBITDA 280M (includes a 40M one-off insurance recovery), cash taxes 45M, maintenance capex 60M, existing debt 320M with 38M annual interest, new loan interest ~12%, straight-line amortization. Assess debt service capacity.

## What a correct response contains

Normalize EBITDA to 240M. Total debt 820M -> leverage 3.4x. Total interest ~98M, principal 100M/yr. DSCR = (240-45-60)/(98+100) = 135/198 = ~0.68x - fails. Restructure needed: smaller amount, longer tenor, or back-ended amortization.

## File-driven variant

With fixture(s) `evals/files/borrower_financials.csv`:

> Assess the borrower in the attached file (evals/files/borrower_financials.csv): compute interest coverage, net leverage, and DSCR, then measure headroom against both covenants and state which is tighter.

Expected: Interest coverage 4.0x; net leverage 3.2x vs max 4.0x (20% headroom); DSCR 1.20x vs min 1.25x (-4.0% headroom). DSCR is the binding constraint.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
