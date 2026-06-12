# Worked Example - aro-computation

## Ask

> We built a factory that must be restored in 10 years at an estimated cost of $1M. Our credit-adjusted risk-free rate is 5%. How do we record this today?

## What a correct response contains

Should calculate the Present Value of the $1M ($1M / (1.05)^10 = ~$613.9k). Should describe the entry to Debit Asset / Credit ARO Liability. Should mention subsequent Accretion and Depreciation. Should provide an ARO Schedule.

## File-driven variant

With fixture(s) `evals/files/retirement_obligations.csv`:

> Using the attached asset retirement obligations file (evals/files/retirement_obligations.csv), measure the initial ARO liability for each asset (inflate current cost to retirement date, discount back at the credit-adjusted rate), total the provision, and compute year-1 accretion expense.

Expected: AROs: Alpha $5,893,636, Beta $4,979,947, Gamma $1,270,349; total $12,143,931; year-1 accretion $958,811.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
