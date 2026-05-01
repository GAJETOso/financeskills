# 🛡️ Smart Audit System

An AI-driven anomaly detection engine designed to scan large volumes of financial transactions for fraud, errors, and compliance violations.

## 🚀 Overview
The Smart Audit System leverages machine learning and heuristic rules to identify "needles in the haystack." It automates the tedious parts of an audit, allowing human auditors to focus on high-risk flags.

## 🛠️ Features
- **Statistical Profiling**: Automatically determines "normal" behavior for specific accounts or vendors.
- **Anomaly Detection**: Flag transactions that deviate significantly from historical patterns (using Isolation Forest or Z-Score).
- **Rule-Based Engine**: Customizable checks for compliance (e.g., "Flag all transactions > $10,000 without an attached invoice").
- **Audit Logging**: Every flag generated is logged with a confidence score and reasoning.

## 📂 Project Structure
```text
audit-system/
├── core/             # Anomaly detection logic
├── scripts/          # Data ingestion and report generation
├── data/             # Sample datasets (anonymized)
└── tests/            # Performance and accuracy evals
```

## 🏁 Getting Started
1.  Place your transaction logs in `data/raw_transactions.csv`.
2.  Run `python scripts/analyze_transactions.py`.
3.  Review the `audit_report.pdf` generated in the root.
