# Worked Example - corporate-consolidation

## Ask

> Parent Co owns 80% of Sub Co. Parent sold $100k of goods to Sub, which are still in Sub's inventory. How do we handle this in consolidation?

## What a correct response contains

Should identify this as an intercompany transaction with unrealized profit. Should eliminate the intercompany Sales/COGS ($100k). Should eliminate the unrealized profit from Inventory and COGS. Should calculate the NCI (20%). Should provide a Consolidated Financial Package.

## File-driven variant

With fixture(s) `evals/files/acquisition.csv`:

> Using the attached acquisition data (evals/files/acquisition.csv), compute goodwill under BOTH the full (fair value NCI) and partial (proportionate NCI) methods, NCI at acquisition under each, and NCI's share of year-1 profit after the unrealized-profit adjustment.

Expected: Full goodwill $2,300,000; partial goodwill $2,000,000; NCI at acquisition $1,800,000 (full) / $1,500,000 (partial); NCI profit share $190,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
