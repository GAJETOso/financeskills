# Bank Reconciliation Statement

**Account:** {bank, account no} | **Period:** {month} | **Prepared:** {date} | **Preparer:** AI agent (review required)

## Reconciliation
| | Amount |
|---|---|
| Balance per bank statement, {date} | {x} |
| Add: deposits in transit | {x} |
| Less: outstanding cheques/payments | ({x}) |
| **Adjusted bank balance** | **{x}** |
| Balance per general ledger, {date} | {x} |
| Add: bank credits not booked (interest, collections) | {x} |
| Less: bank debits not booked (charges, returned items) | ({x}) |
| **Adjusted GL balance** | **{x}** |

Difference: {must be 0.00 - if not, list unresolved items below}

## Outstanding Items Detail
| Type | Date | Ref | Description | Amount | Age (days) |
|---|---|---|---|---|---|

## Adjusting Journal Entries Required
| Account | Dr | Cr | Memo |
|---|---|---|---|

## Exceptions / Unresolved
{Items needing investigation, with owner and due date. Flag anything > 30 days old.}

---
*Matching performed with scripts/calculate.py. Reviewed by: ____________ Date: ________*
