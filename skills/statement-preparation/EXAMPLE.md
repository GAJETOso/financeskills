# Worked Example - statement-preparation

## Ask

> Here is our Trial Balance. Can you prepare the P&L and Balance Sheet? We also need to record $5k in depreciation.

## What a correct response contains

Should validate the Trial Balance (Debits=Credits). Should record the $5k adjusting entry for depreciation. Should map accounts to the Income Statement and Balance Sheet. Should ensure Net Income flows into Retained Earnings. Should provide the full Financial Statement Package.

## File-driven variant

With fixture(s) `evals/files/movement_data.csv`:

> Prepare an indirect-method cash flow statement from the attached movement data (evals/files/movement_data.csv): CFO with working-capital adjustments, CFI, CFF, and prove closing cash.

Expected: CFO $2,238,000; CFI $-3,100,000; CFF $1,562,000; closing cash $4,200,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
