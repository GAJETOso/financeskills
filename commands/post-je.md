---
description: Prepare a balanced journal entry with support and approval fields
argument-hint: <what happened: e.g. "accrue May payroll 84,300, reverses June">
---
Use the journal-entry skill in skills/journal-entry/SKILL.md.

Transaction: $ARGUMENTS

Requirements:
- Validate Dr = Cr with skills/journal-entry/scripts/calculate.py (validate_entry) before presenting
- State the business purpose and supporting document
- If it's an accrual, provide the reversal entry too
- Output using skills/journal-entry/assets/journal-entry-template.md
