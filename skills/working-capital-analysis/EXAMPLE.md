# Worked Example - working-capital-analysis

## Ask

> Revenue 7.3B/year, COGS 5.1B/year. AR 1.2B, inventory 900M, AP 700M. Compute the CCC and tell me what 10 days of DSO improvement is worth.

## What a correct response contains

DSO = 60 days, DIO = 64.4 days, DPO = 50.1 days, CCC = ~74.3 days. One day of revenue = 20M, so 10 DSO days = ~200M cash release.

## File-driven variant

With fixture(s) `evals/files/wc_balances.csv`:

> From the attached balances (evals/files/wc_balances.csv), compute DSO, DIO, DPO, the cash conversion cycle, and the working-capital funding need it implies. Quantify the cash freed by cutting DSO by 10 days.

Expected: DSO 60.0, DIO 77.8, DPO 53.7; CCC 84.1 days; funding need $13,278,279; 10 fewer DSO days frees ~$1,578,082.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
