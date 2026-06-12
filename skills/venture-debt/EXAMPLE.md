# Worked Example - venture-debt

## Ask

> We're a Series B startup with $5M in MRR. We want to borrow $10M in venture debt to avoid dilution. What should we expect for terms?

## What a correct response contains

Should identify that venture debt is typically 20-30% of the last equity round or linked to MRR multiples. Should discuss Warrants and Covenants (Minimum Cash/MRR). Should provide a Venture Debt Term Sheet structure.

## File-driven variant

With fixture(s) `evals/files/term_sheet.csv`:

> Analyze the attached venture-debt term sheet (evals/files/term_sheet.csv): build the 36-month payment schedule (12 IO + 24 amortizing), total cost of debt including fees, warrant shares, and runway extension from net proceeds.

Expected: Total interest+fees $1,498,817; warrants 200,000 shares; runway extension 7.1 months; monthly payment in amortization ~$235,367.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
