# Worked Example - ecl-computation

## Ask

> We have $1M in trade receivables. Historically, 2% of these fail to pay. This year, the economy is heading into a recession. How should we calculate our provision?

## What a correct response contains

Should recommend a Provision Matrix approach for trade receivables. Should discuss adjusting the historical 2% rate upwards for the expected recession. Should mention Stage 1/2/3 classification for non-trade assets. Should provide an ECL Analysis Report.

## File-driven variant

With fixture(s) `evals/files/receivables_aging.csv`:

> Apply the IFRS 9 simplified approach (provision matrix) to the attached receivables aging (evals/files/receivables_aging.csv). Compute the loss allowance per bucket and in total, and state the coverage ratio.

Expected: Allowance per bucket from balance x loss rate; total $721,400; coverage 10.66% of gross receivables.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
