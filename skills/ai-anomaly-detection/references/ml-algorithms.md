# Anomaly Detection Algorithms for Financial Data

## Algorithm Selection
| Algorithm | Best For | Notes |
|---|---|---|
| Z-score / modified Z (MAD) | Univariate amounts, quick baselines | Robust version uses median/MAD; flag \|z\| > 3 (or > 3.5 MAD) |
| IQR fences | Skewed distributions | Outlier if < Q1 − 1.5×IQR or > Q3 + 1.5×IQR |
| Isolation Forest | Multivariate, mixed features, large JE populations | contamination ≈ expected anomaly rate (0.001–0.01 for JEs); fast, no distribution assumption |
| Local Outlier Factor | Density-varying data (different entities/scales) | Catches local anomalies global methods miss |
| One-Class SVM | Small, clean training sets | Sensitive to scaling; slower |
| Autoencoder | High-dimensional, abundant data | Reconstruction error as anomaly score; needs volume |
| Benford's Law | First/second-digit tests on populations > 1,000 | Screening only — deviations need investigation, not accusation |
| Time-series (STL + residual z) | Seasonality-aware account monitoring | Decompose, then flag residual outliers |

## Practical Pipeline for Journal Entry Testing
1. Score with 2–3 uncorrelated methods (e.g., Isolation Forest + MAD + rules).
2. Combine: rank-average or max-rule; rule-based flags (weekend posting, round amounts, manual JEs by unusual users, just-below-approval-threshold) always surface regardless of model score.
3. Triage queue sorted by composite score × monetary value.

## Evaluation Without Labels
- Precision@k: review top-k flags, count true issues.
- Inject synthetic anomalies (duplicated invoices, split transactions) to measure recall.
- Track investigator feedback to recalibrate quarterly.

## Pitfalls
- Scaling: tree methods don't need it; distance methods (LOF, SVM) require it.
- Train/score leakage: fit on prior periods, score current.
- Anomalous ≠ fraudulent — output is a *review queue*, never an auto-accusation.
