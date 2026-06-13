# Worked Example - retirement-planning

## Ask

> I'm 35 years old, have $45,000 saved for retirement, and contribute $500/month. I want to retire at 65 with $1.5M. My expected return is 7% per year. Am I on track? If not, how much more do I need to contribute?

## What a correct response contains

Should project the future value of $45,000 + $500/month at 7% over 30 years. Should compare the projection to the $1.5M target. Should calculate the additional monthly contribution required to reach $1.5M. Should mention the 4% rule and the annual withdrawal $1.5M would support.

## File-driven variant

With fixture `evals/files/retirement_inputs.csv`:

> From the attached inputs (evals/files/retirement_inputs.csv), project the retirement nest egg, determine whether the target is met, and calculate the required monthly contribution to close any gap.

Expected: Projected nest egg $975,228; gap $524,772; need to contribute approximately $930/month to hit $1.5M target; 4% withdrawal from $1.5M supports $60,000/year.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) — import its functions rather than doing arithmetic in prose.
