# Worked Example - ai-anomaly-detection

## Ask

> We have 1 million credit card transactions. We want to find weird spending patterns that don't follow our standard rules. Which ML model should we use?

## What a correct response contains

Should recommend unsupervised learning models like Isolation Forest or Autoencoders. Should explain why these are better than rules-based systems for large datasets. Should mention feature engineering (e.g. txn frequency, distance). Should provide an AI Audit Report structure.

## File-driven variant

With fixture(s) `evals/files/expense_ledger.csv`:

> Screen the attached expense ledger (evals/files/expense_ledger.csv) for anomalies using at least two methods (z-score and IQR). Report flagged rows with their references and quantify how extreme each is.

Expected: Two planted anomalies: GL-4057 (290.00, high) and GL-4101 (12.00, low). Z-score flags indices [57, 101].

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
