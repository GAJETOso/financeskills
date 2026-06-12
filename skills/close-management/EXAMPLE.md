# Worked Example - close-management

## Ask

> Our close takes 9 working days. Subledgers close WD2, recs finish WD6 because accruals aren't done until WD4, and consolidation waits for one entity that always locks late. Build us a plan to get to 5 days.

## What a correct response contains

Should identify the critical path (accruals -> recs -> entity lock -> consolidation), move predictable accruals pre-close, set intercompany/late-entity deadlines with escalation, and produce a day-by-day close calendar with dependencies.

## File-driven variant

With fixture(s) `evals/files/close_status_day4.csv`:

> It is Day 4 of the close. Assess the attached status (evals/files/close_status_day4.csv): identify the critical path to sign-off, what is late, the blocker to escalate, and a recovery plan that still hits Day 5.

Expected: Critical path T-03/T-04 -> T-06 -> T-07. T-03 is 2 days late with no dependency - start immediately. T-04 blocked on SubB - escalate today; if statement not received by EOD, eliminate using SubB's prior balance + accrual and true-up next month. T-06 compresses to Day 5 morning; T-07 Day 5 afternoon.
