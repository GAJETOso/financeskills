# Worked Example - banking-compliance

## Ask

> Our bank has $100M in CET1 capital and $800M in Risk-Weighted Assets. Are we Basel III compliant?

## What a correct response contains

Should calculate the CET1 ratio ($100M / $800M = 12.5%). Should compare this to the Basel III minimum (4.5% + buffers). Should conclude the bank is currently compliant. Should provide a Regulatory Compliance Dashboard.

## File-driven variant

With fixture(s) `evals/files/exposures.csv`:

> CET1 capital is $410,000,000 and the countercyclical buffer is 1%. Using the attached exposure file (evals/files/exposures.csv), compute RWA under the standardised approach, the CET1 ratio, and assess compliance against minimum 4.5% + 2.5% conservation + 1% CCyB.

Expected: RWA $3,645,000,000; CET1 ratio 11.25% vs requirement 8.0%; surplus 3.25% - compliant.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
