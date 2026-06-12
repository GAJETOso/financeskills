# Worked Example - crypto-accounting

## Ask

> We bought 1 BTC for $50k. It dropped to $30k last month, but now it's at $60k. How do we value it on our GAAP balance sheet?

## What a correct response contains

Should identify the GAAP impairment rule (Indefinite-lived intangible asset). Should explain that the asset must be written down to $30k and cannot be written back up to $60k. Should provide a Digital Asset Ledger Summary.

## File-driven variant

With fixture(s) `evals/files/btc_lots.csv`:

> Holdings per the attached lot file (evals/files/btc_lots.csv), reporting under US GAAP (ASU 2023-08). (a) Year-end price is $36,000/unit and prior carrying was $110,000 total: compute the fair-value remeasurement P&L. (b) Separately, if 2.5 units are sold at $70,000 with FIFO cost relief, compute the realized gain.

Expected: (a) New carrying $108,000, P&L -2,000. (b) FIFO cost basis $85,000, realized gain $90,000.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
