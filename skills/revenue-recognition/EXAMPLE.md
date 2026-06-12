# Worked Example - revenue-recognition

## Ask

> We sold a $12k annual subscription today. The customer paid upfront. How much revenue do we recognize this month?

## What a correct response contains

Should identify this as a multi-period performance obligation. Should calculate the monthly revenue ($1k). Should explain the deferral of the remaining $11k as Unearned Revenue. Should provide a Revenue Recognition Memo structure.

## File-driven variant

With fixture(s) `evals/files/contracts.csv`:

> Contract C-101 in the attached file (evals/files/contracts.csv) was signed on 1 January for a fixed price of $100,000. Support and implementation are both delivered evenly over 12 months. Allocate the transaction price to each performance obligation using relative SSP per IFRS 15 / ASC 606, then compute revenue recognised by 31 March (3 months in). Show the allocation table and journal-ready amounts.

Expected: Relative-SSP allocation: licence $60,000, support $24,000, implementation $16,000 (sums to $100,000). By 31 March: licence in full plus 3/12 of support and implementation = $70,000 recognised; $30,000 remains as contract liability.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
