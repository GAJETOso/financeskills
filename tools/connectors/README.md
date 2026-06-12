# Live-Data Connectors

Opt-in scripts that pull real financial data into the CSV shapes the skills
consume. This is the **only** networked code among the repo's tools, it runs
only when you invoke it, and only with credentials you supply via environment
variables (never stored).

| Connector | Source | Feeds skills | Credentials |
|---|---|---|---|
| `stripe_export.py` | Stripe balance transactions | automated-reconciliation, revenue-recognition, predictive-burn-rate | `STRIPE_API_KEY` |
| `plaid_export.py` | Bank transactions via Plaid | automated-reconciliation, predictive-burn-rate, treasury-management | `PLAID_CLIENT_ID/SECRET/ACCESS_TOKEN` |
| `quickbooks_export.py` | QuickBooks Online GL | automated-reconciliation, journal-entry, financial-analysis | `QBO_ACCESS_TOKEN`, `QBO_REALM_ID` |
| `xero_export.py` | Xero bank transactions | automated-reconciliation, treasury-management | `XERO_ACCESS_TOKEN`, `XERO_TENANT_ID` |
| `csv_mapper.py` | ANY CSV export (SAP, Sage, bank portals) | everything file-driven | none - offline column mapper |

Every connector has a `--mock` flag that generates realistic sample data with
no network access - use it to test the full pipeline before wiring real keys.

## Example pipeline: bank rec from live data

```bash
python3 tools/connectors/plaid_export.py  --start 2026-05-01 --end 2026-05-31 -o bank.csv
# export your GL cash ledger from your ERP to gl.csv, then in your agent:
#   /reconcile bank.csv gl.csv
```
