# Worked Example - startup-valuation

## Ask

> We have a SaaS startup with a working MVP and 2 technical co-founders. We're raising $500k. How much should we be valued at?

## What a correct response contains

Should apply the Berkus Method to assign value for 'Sound Idea', 'Prototype', and 'Quality Management'. Should ask about traction or TAM. Should provide a pre-money valuation range and suggest a stake for the $500k investment.

## File-driven variant

With fixture(s) `evals/files/round_terms.csv`:

> Apply the VC method to the attached round terms (evals/files/round_terms.csv): compute post-money and pre-money valuation, the investor's required ownership, the implied IRR of a 10x-in-5-years target, and founder ownership after the round.

Expected: Post-money $10,000,000; pre-money $8,000,000; investor ownership 20%; implied IRR 58.5%; founder falls to 48%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
