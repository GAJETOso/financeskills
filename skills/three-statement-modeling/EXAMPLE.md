# Worked Example - three-statement-modeling

## Ask

> Build a simple 3-year integrated model: revenue 1,000 growing 10%, EBITDA margin 25%, D&A 50/yr (capex 60/yr), tax 30%, DSO 45, DPO 30, DIO 0, opening cash 100, no debt, no dividends. Show the three statements and prove the balance sheet balances.

## What a correct response contains

A coded model producing IS (NI year 1 = (250-50)x0.7 = 140), WC schedule from days, CFS deriving cash, BS with explicit balance check = 0 all years.

## File-driven variant

With fixture(s) `evals/files/model_inputs.xlsx`:

> Project one year of the linked three-statement model from the attached workbook (evals/files/model_inputs.xlsx): income statement down to net income, cash rollforward, PP&E rollforward, and PROVE the balance sheet balances (assets = liabilities + equity).

Expected: Revenue 110.0; net income 13.16; closing cash 26.80; PP&E 81.10; equity 67.90; balance check passes.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
