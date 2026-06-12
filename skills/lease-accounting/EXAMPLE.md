# Worked Example - lease-accounting

## Ask

> We signed a 5-year office lease: 10,000,000 NGN per year paid annually in arrears, IBR 18%, no incentives, no restoration. Compute the initial lease liability and ROU asset and give me year-1 entries.

## What a correct response contains

Liability = PV of 5 payments of 10M at 18% = ~31,272,000 NGN. ROU = same. Year 1: interest = ~5,629,000, payment 10M reduces liability to ~26,901,000; ROU depreciation = ~6,254,400/yr straight-line.

## File-driven variant

With fixture(s) `evals/files/lease_portfolio.csv`:

> Using the attached lease portfolio (evals/files/lease_portfolio.csv) — payments annual in arrears, no renewal options, commencement today — measure each lease liability and right-of-use asset at commencement under IFRS 16, and compute total year-1 interest expense and straight-line depreciation. Produce a commencement summary table and the initial journal entry.

Expected: Liabilities: L-01 $1,025,049, L-02 $689,597, L-03 $194,383; total $1,909,029 (ROU assets equal liabilities here). Year-1 interest $144,416; year-1 depreciation $339,805.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
