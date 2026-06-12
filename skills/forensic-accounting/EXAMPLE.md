# Worked Example - forensic-accounting

## Ask

> Our petty cash is missing $5,000 over the last 3 months. Only the office manager has the key. Can you investigate?

## What a correct response contains

Should recognize this as a potential asset misappropriation investigation. Should ask for the petty cash log and bank withdrawal records. Should recommend a reconciliation of physical cash vs log. Should suggest checking for 'top-up' patterns. Should provide a structured Forensic Report structure with Evidence Chain and Control Recommendations.

## File-driven variant

With fixture(s) `evals/files/disbursements.csv`:

> Run a Benford first-digit analysis on the attached disbursements (evals/files/disbursements.csv) - overall AND segmented by the 'segment' column. Report chi-square per segment against the 15.507 critical value and identify which population deviates.

Expected: Operations chi2 16 (conforms); Procurement-VendorX chi2 544 (strong deviation - first digits cluster 4-8); overall chi2 217. Flags VendorX for follow-up, noting deviation is an indicator not proof.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
