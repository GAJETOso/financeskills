# Worked Example - debt-payoff

## Ask

> I have three debts: a credit card with a $4,500 balance at 22% APR ($90 minimum), a car loan with $8,000 at 6% APR ($180 minimum), and a student loan with $12,000 at 5% APR ($130 minimum). I can put $600/month total toward debt. Which strategy saves me more money — avalanche or snowball?

## What a correct response contains

Should list all three debts clearly. Should model both avalanche and snowball strategies month by month. Should show that avalanche pays off the credit card first (highest rate 22%) and saves more in total interest. Should compare total interest paid and total months to debt-free under each strategy. Should recommend avalanche for this user given the large interest-rate gap.

## File-driven variant

With fixture `evals/files/debts.csv`:

> From the attached debt list (evals/files/debts.csv), calculate the total interest paid and months to debt-free under both avalanche and snowball, with $200/month extra payment. Show which strategy saves more.

Expected: Avalanche — 38 months, $2,847 total interest. Snowball — 38 months, $3,201 total interest. Avalanche saves $354 in interest.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) — import its functions rather than doing arithmetic in prose.
