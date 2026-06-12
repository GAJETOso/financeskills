# Feature Engineering for Financial Anomaly Detection

## Journal Entry Features
- **Amount-based**: raw amount, log(|amount|), roundness score (trailing zeros), distance to nearest approval threshold (e.g., amount/threshold ratio in [0.9, 1.0) is suspicious), first-two-digit Benford deviation of the user's population.
- **Timing**: hour-of-day, day-of-week, posted-on-weekend/holiday flag, days from period end (entries on WD-0/WD+1 deserve weight), posting date vs. effective date gap.
- **User behavior**: entries per user per period vs. trailing median, new user flag (< 90 days), user-account pair novelty (first time this user touches this account), seniority-vs-amount mismatch.
- **Account patterns**: rare account combination flag (debit-credit pair frequency), suspense/clearing account usage, P&L-to-BS reclass patterns.
- **Text**: description length, generic-description flag ("adjustment", "misc", blank), duplicate description with different amounts.

## Transaction-Level (AP/AR) Features
- Vendor: invoice number gaps/sequences, duplicate detection key (vendor + amount + date ±3d), bank account changes, vendor-employee address/phone match.
- Payment: split-payment detection (same vendor, same day, sum > threshold), velocity (payments per vendor per week vs. baseline).

## Aggregation Windows
Build each behavioral feature at 3 windows (7/30/90 days) and use the ratio of short-to-long window as a drift signal.

## Encoding & Hygiene
- High-cardinality categoricals (account, vendor): frequency encoding or target-free hashing — never one-hot 10k vendors.
- Winsorize at 0.1%/99.9% before scaling for distance-based models.
- Keep a human-readable reason string per feature so flags are explainable to auditors.
