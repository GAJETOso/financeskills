# Worked Example - personal-budgeting

## Ask

> My take-home is $4,500/month. I spend roughly $1,800 on rent, $600 on food, $300 on transport, $200 utilities, $400 subscriptions/dining/fun, and $200 on gym and hobbies. I never seem to save anything. Help me build a budget.

## What a correct response contains

Should calculate total expenses ($3,500) and surplus ($1,000). Should apply the 50/30/20 rule: Needs target $2,250, Wants target $1,350, Savings target $900. Should identify that Needs ($2,900) exceed the 50% target. Should recommend moving the savings surplus to an automated transfer. Should provide a concrete action plan with category-level reductions.

## File-driven variant

With fixture `evals/files/monthly_expenses.csv`:

> From the attached monthly expense data (evals/files/monthly_expenses.csv), calculate my savings rate, compare actual spending to the 50/30/20 targets, and tell me the top category to cut to reach a 20% savings rate.

Expected: income $5,000; Needs $2,600 (52%), Wants $1,300 (26%), Savings $600 (12%); savings rate 12%; needs to save $1,000/month for 20% target; top cut category is Dining ($400).

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) — import its functions rather than doing arithmetic in prose.
