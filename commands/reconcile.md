---
description: Reconcile a bank statement against the GL cash ledger and produce a reconciliation statement
argument-hint: <bank.csv> <gl.csv> [opening balance]
---
Use the automated-reconciliation skill in skills/automated-reconciliation/SKILL.md.

Reconcile these files: $ARGUMENTS

Requirements:
- Match transactions with code (amount + date proximity + reference), not by eye
- Classify unmatched items: deposits in transit, outstanding payments, bank-only items
- Prove adjusted balances agree to the cent; if not, list unresolved items with ages
- Output using skills/automated-reconciliation/assets/reconciliation-statement-template.md
- Draft the adjusting journal entries for bank-only items
