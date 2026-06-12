# Worked Example - intercompany-accounting

## Ask

> Parent shows due-from Sub A of 125M; Sub A shows due-to Parent of 117M. Walk me through resolving the 8M difference.

## What a correct response contains

Apply the hierarchy: check in-transit items around cut-off, FX rate differences (different sources/dates), missing bookings on one side, then pricing disputes. Fix entity books before consolidation; never eliminate a mismatch.

## File-driven variant

With fixture(s) `evals/files/ic_receivables_parent.csv`, `evals/files/ic_payables_subs.csv`:

> Match the attached intercompany balances (evals/files/ic_receivables_parent.csv vs evals/files/ic_payables_subs.csv) and identify mismatches. Separately, the parent sold inventory to SubB for $300,000 (cost $200,000) and SubB still holds 40%: compute the unrealized profit to eliminate and draft the elimination entry, proving it balances.

Expected: SubB mismatch $20,000 (cash/goods in transit to investigate); SubC and SubD agree. URP $40,000; elimination: Dr IC Revenue 300,000 / Cr IC COGS 260,000 / Cr Inventory 40,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
