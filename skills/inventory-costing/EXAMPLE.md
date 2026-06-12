# Worked Example - inventory-costing

## Ask

> Purchases: 200 units at 50, then 300 at 60, then 100 at 70. We sold 450 units. Give me COGS and ending inventory under FIFO and periodic weighted average.

## What a correct response contains

Total cost 35,000 for 600 units. FIFO: COGS = 200x50 + 250x60 = 25,000; ending = 50x60 + 100x70 = 10,000. Weighted avg 58.333: COGS = 26,250; ending = 8,750. Both proved to total 35,000.

## File-driven variant

With fixture(s) `evals/files/purchases_sales.csv`:

> From the attached purchase/sale ledger (evals/files/purchases_sales.csv), compute COGS and ending inventory for the 150-unit sale under FIFO, weighted average, and periodic LIFO. State which gives the lowest taxable income in this rising-price environment.

Expected: FIFO COGS $1,600 / EI $2,000; WAC $1,800; LIFO $2,000. LIFO minimizes taxable income when prices rise.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
