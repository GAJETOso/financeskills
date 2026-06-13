# Worked Example - tax-efficient-investing

## Ask

> I'm in the 24% federal tax bracket, single filer, earning $95,000. I have a 401k at work with a 4% employer match, and I have $10,000 to invest this year. How should I allocate it across account types for maximum tax efficiency?

## What a correct response contains

Should first confirm whether the user is capturing the full employer 4% match (free money). Should recommend: (1) contribute enough to 401k to get full match, (2) max Roth IRA ($7,000 for 2024), (3) remaining into 401k or taxable brokerage. Should calculate the tax savings from pre-tax 401k contributions. Should explain Roth vs. traditional trade-off at 24% bracket.

## File-driven variant

With fixture `evals/files/tax_inputs.csv`:

> From the attached tax inputs (evals/files/tax_inputs.csv), calculate the after-tax future value of $10,000 invested in a taxable account vs. a Roth IRA over 25 years at 7% gross return. Quantify the tax drag in dollar terms.

Expected: Roth IRA FV $54,274 (no tax drag); Taxable FV $42,415 (15% tax on gains applied annually); tax drag cost $11,859 over 25 years; Roth advantage: 21.8% more wealth.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) — import its functions rather than doing arithmetic in prose.
