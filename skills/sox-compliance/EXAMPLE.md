# Worked Example - sox-compliance

## Ask

> I need to test a daily three-way-match control in P2P for the full year. Population is about 18,000 matched invoices. How many samples, how do I pick them, and what do I document?

## What a correct response contains

Sample of 25-40 (daily/per-transaction frequency), random selection across the full period including period-end, population completeness validation against the GL/system, and item-level attribute documentation.

## File-driven variant

With fixture(s) `evals/files/revenue_population.csv`:

> This is the Jan-May population for the revenue approval control (evals/files/revenue_population.csv), which operates per-transaction (daily frequency). Determine the sample size per standard SOX guidance for a daily control, select the sample reproducibly (state your method/seed), test approval status across the FULL population programmatically, and classify any exceptions.

Expected: Daily/multiple-times-daily control -> 25 selections (or 40 per some methodologies - state the table used). Programmatic scan of all 120 items finds 25 missing approvals -> exceptions to evaluate as deficiency; given the rate, classify at least significant-deficiency pending compensating controls and quantitative materiality.
