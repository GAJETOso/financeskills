# Worked Example - automated-reconciliation

## Ask

> I have 500 bank transactions and 510 ledger entries. Most are exact matches, but 20 have slightly different names like 'AWS' vs 'Amazon'. How can I reconcile this?

## What a correct response contains

Should recommend a two-step process: Deterministic matching for exact entries and Probabilistic/Fuzzy matching for name variances. Should mention vendor name normalization. Should provide a Reconciliation Report structure.

## File-driven variant

With fixture(s) `evals/files/bank_statement.csv`, `evals/files/gl_cash.csv`:

> Reconcile the attached May bank statement (evals/files/bank_statement.csv) against the GL cash ledger (evals/files/gl_cash.csv). Both start from an agreed opening balance of $100,000.00. Match transactions, identify deposits in transit, outstanding cheques, and bank-only items, then produce a bank reconciliation statement proving the adjusted balances agree.

Expected: Bank ending balance $147,060.00; GL ending balance $154,540.00. Deposit in transit $27,300.00 (INV1045); outstanding cheques $12,640.00 (2206) and $7,120.00 (2207); bank-only items: charges $350.00 and interest $410.00 to be booked in GL. Adjusted balance both sides $154,600.00.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
