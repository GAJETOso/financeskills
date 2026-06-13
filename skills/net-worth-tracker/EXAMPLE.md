# Worked Example - net-worth-tracker

## Ask

> Here are my finances: checking $3,000, savings $12,000, 401k $68,000, car value $15,000. Debts: car loan $9,000, student loan $22,000, credit card $3,500. What's my net worth and how healthy does it look?

## What a correct response contains

Should total assets: $98,000. Should total liabilities: $34,500. Should calculate net worth: $63,500. Should compute debt-to-asset ratio: 35% (healthy, below 50%). Should assess liquidity: liquid assets $15,000 (15% — adequate). Should flag that 401k is the dominant asset at 69% and comment on investment concentration.

## File-driven variant

With fixture `evals/files/balance_sheet.csv`:

> From the attached balance sheet (evals/files/balance_sheet.csv), calculate net worth, debt-to-asset ratio, and asset allocation. Compare to the prior period values in the file.

Expected: Current net worth $87,500; prior net worth $74,200; change +$13,300 (+17.9%); debt-to-asset ratio 28.6%; investment assets 71% of total. Primary driver of growth: retirement account appreciation.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) — import its functions rather than doing arithmetic in prose.
