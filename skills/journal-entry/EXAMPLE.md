# Worked Example - journal-entry

## Ask

> We received legal services worth $25,000 in June but the invoice won't arrive until July. Prepare the June entry.

## What a correct response contains

Dr Legal/Professional Fees 25,000 / Cr Accrued Liabilities 25,000, flagged auto-reversing in July, with documentation basis (engagement letter, work confirmation).

## File-driven variant

With fixture(s) `evals/files/draft_entries.csv`:

> Review the attached draft journal entries (evals/files/draft_entries.csv) before posting. Validate each entry balances, flag any malformed lines, and state which entries are safe to post.

Expected: JE-101 and JE-103 are valid. JE-102 is out of balance by $450 (17,500 vs 17,050 - transposition). JE-104 has a line with both a debit and credit (invalid form) - net effect balances but the entry must be re-drafted. Only JE-101 and JE-103 post as-is.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
