# Skill: Audit Checklist

## When to use
Use this skill to verify the integrity of financial records and ensure compliance with internal controls or accounting standards.

## Inputs
- **General Ledger**: Export of transactions for a specific period.
- **Support Documentation**: Invoices, receipts, bank statements (for sampling).
- **Control Rules**: List of internal policies (e.g., "All expenses > $500 require manager approval").

## Steps
1.  **Duplicate Detection**: Scan for transactions with identical amounts, dates, and vendors.
2.  **Threshold Analysis**: Identify transactions just below approval thresholds (e.g., many $499 items when the limit is $500).
3.  **Vendor Verification**: Check for unusual vendor names or missing tax IDs.
4.  **Sequential Testing**: Ensure invoice/check numbers follow a logical sequence.
5.  **Reconciliation Check**: Match bank statement totals to internal ledger totals.

## Output Format
- **Audit Findings Log**: List of discrepancies found.
- **Compliance Score**: % of sampled items that met all criteria.
- **Remediation Steps**: What needs to be corrected.
