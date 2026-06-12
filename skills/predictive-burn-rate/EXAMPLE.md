# Worked Example - predictive-burn-rate

## Ask

> Our burn rate has been $100k, $120k, and $150k over the last 3 months. We have $1M in the bank. When do we run out of money?

## What a correct response contains

Should identify the accelerating burn trend. Should note that a simple average is dangerous due to the acceleration. Should calculate the 'Zero Date' based on the trend (approx. 5-6 months). Should suggest using Prophet for a more detailed seasonal forecast. Should provide a Runway Forecast Report.

## File-driven variant

With fixture(s) `evals/files/monthly_cash.csv`:

> Cash on hand is $7,500,000. Using the attached six months of actuals (evals/files/monthly_cash.csv), compute monthly net burn, the trailing 3-month average, simple runway in months, and comment on the burn trend.

Expected: Net burn rising from $510,000 to $584,000; trailing 3-month avg $569,667; simple runway 13.2 months; trend-adjusted runway is shorter - flag it.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
