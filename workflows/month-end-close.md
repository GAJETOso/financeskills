# Workflow: Month-End Close (skill orchestration)

Chains seven skills into one repeatable close. Run via `/close-the-books` or
follow manually. Each phase names its skill, inputs, and the artifact it must
produce before the next phase starts.

## Phase 0 - Plan (close-management)
Input: prior close calendar or task list. Output: sequenced Day 1-5 task list
with owners and dependencies. Gate: critical path identified.

## Phase 1 - Subledger entries (journal-entry, fixed-asset-accounting, lease-accounting, deferred-tax)
Input: payroll summary, asset register, lease portfolio, temp-difference schedule.
Compute every figure with the skills' scripts/calculate.py. Output: balanced JE
batch validated by journal_entry.validate_entry, each on the JE voucher template.
Gate: all entries balance; accruals carry reversal dates.

## Phase 2 - Reconciliations (automated-reconciliation, intercompany-accounting)
Input: bank statements (via tools/connectors/ or exports), GL cash, IC balances.
Output: reconciliation statements proving adjusted balances agree; IC mismatch
list with resolutions. Gate: zero unexplained differences; adjusting JEs from
bank-only items loop back through Phase 1.

## Phase 3 - Statements (statement-preparation, financial-analysis)
Input: post-adjustment trial balance + prior period. Output: P&L, balance sheet,
indirect cash flow (closing cash must tie), ratio/flux memo flagging moves
> 10% or > materiality. Gate: balance sheet balances; cash ties; flux explained.

## Phase 4 - Review pack (close-management)
Output: sign-off pack - statements, flux memo, rec statements, JE register,
open-items list with owners. Gate: reviewer sign-off fields present.

## Rules
- Every calculation through scripts/calculate.py functions - no mental math.
- Every output on its skill's assets/ template where one exists.
- Anything estimated (accrual bases, allocations) labeled with basis and owner.
- AI-prepared close requires human review before posting - say so in the pack.
