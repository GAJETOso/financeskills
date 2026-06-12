# Worked Example - variance-analysis

## Ask

> We expected to use 1,000 lbs of steel at $5/lb. We actually used 1,100 lbs at $4.50/lb. Calculate the variances.

## What a correct response contains

Should calculate Material Price Variance ($0.50 favorable * 1,100 lbs = $550 F). Should calculate Material Usage Variance (100 lbs unfavorable * $5 = $500 U). Should provide a Production Variance Report.

## File-driven variant

With fixture(s) `evals/files/production_data.xlsx`:

> Compute material price, material usage, labor rate, and labor efficiency variances from the attached production workbook (evals/files/production_data.xlsx). Label each favourable/adverse and explain the most material driver.

Expected: MPV -25,500 (adverse), MUV -30,000, LRV -15,620 (adverse), LEV 20,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
