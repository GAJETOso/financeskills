---
description: Measure lease liabilities and ROU assets at commencement (IFRS 16 / ASC 842)
argument-hint: <lease portfolio file or terms: payment, timing, term, rate>
---
Use the lease-accounting skill in skills/lease-accounting/SKILL.md.

Lease data: $ARGUMENTS

Requirements:
- Present-value each lease with skills/lease-accounting/scripts/calculate.py (state arrears vs advance)
- Produce the commencement table, year-1 interest + depreciation, and the initial journal entry
- Note judgments: renewal options, short-term/low-value exemptions
- Output using skills/lease-accounting/assets/commencement-summary-template.md
