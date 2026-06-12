# Worked Example - insurance-reserving

## Ask

> Our paid losses for Accident Year 2023 are $500k. Historically, this line develops to 2.0x its current value by year 5. What's our IBNR?

## What a correct response contains

Should calculate Projected Ultimate Loss ($500k * 2.0 = $1M). Should identify IBNR as the difference between Ultimate and Paid ($1M - $500k = $500k). Should discuss the loss ratio. Should provide an Insurance Reserve Report.

## File-driven variant

With fixture(s) `evals/files/paid_triangle.csv`:

> Apply the chain-ladder method to the attached cumulative paid triangle (evals/files/paid_triangle.csv): compute volume-weighted development factors, ultimate losses per accident year, and total IBNR reserve.

Expected: LDFs [1.5, 1.2, 1.1]; ultimates ['8,316,000', '9,108,000', '10,098,000', '10,890,000']; IBNR $8,666,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
