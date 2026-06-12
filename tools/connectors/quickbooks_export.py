#!/usr/bin/env python3
"""QuickBooks Online -> skill-ready CSV connector.

Exports the GL (JournalEntry/Purchase/Invoice lines via the Reports API
GeneralLedger) into the (date, description, amount, ref) shape used by
automated-reconciliation, journal-entry review, and financial-analysis.

  python3 quickbooks_export.py --mock -o gl.csv
  QBO_ACCESS_TOKEN=... QBO_REALM_ID=... python3 quickbooks_export.py \
      --start 2026-05-01 --end 2026-05-31 --account "Bank - Operating" -o gl.csv

Network: only without --mock, only to the Intuit API host, only with your token
(OAuth2 access token - refresh outside this script).
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
import urllib.parse
import urllib.request

HOST = os.environ.get("QBO_HOST", "https://quickbooks.api.intuit.com")


def fetch(start: str, end: str, account: str | None) -> list[dict]:
    tok, realm = os.environ.get("QBO_ACCESS_TOKEN"), os.environ.get("QBO_REALM_ID")
    if not (tok and realm):
        sys.exit("QBO_ACCESS_TOKEN / QBO_REALM_ID not set (or use --mock)")
    params = {"start_date": start, "end_date": end, "columns": "tx_date,memo,subt_nat_amount,doc_num"}
    url = f"{HOST}/v3/company/{realm}/reports/GeneralLedger?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}",
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        report = json.loads(r.read())
    rows = []
    def walk(node):
        for item in node.get("Rows", {}).get("Row", []):
            if item.get("type") == "Data":
                cols = [c.get("value", "") for c in item["ColData"]]
                rows.append({"date": cols[0], "description": cols[1],
                             "amount": float(cols[2] or 0), "ref": cols[3] or ""})
            walk(item)
    walk(report)
    if account:
        rows = [r for r in rows if account.lower() in r["description"].lower()] or rows
    return rows


def mock_rows() -> list[dict]:
    return [
        {"date": "2026-05-02", "description": "Invoice 1041 - Acme Industries", "amount": 48_200.00, "ref": "INV1041"},
        {"date": "2026-05-08", "description": "Bill payment - Apex Supplies chq 2204", "amount": -18_400.00, "ref": "CHQ2204"},
        {"date": "2026-05-20", "description": "Payroll run May", "amount": -84_300.00, "ref": "PR-2026-05"},
        {"date": "2026-05-29", "description": "Bill payment - Omega Services chq 2206", "amount": -12_640.00, "ref": "CHQ2206"},
        {"date": "2026-05-31", "description": "Invoice 1045 - Zenith Ltd", "amount": 27_300.00, "ref": "INV1045"},
    ]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--start", default="2026-05-01")
    ap.add_argument("--end", default="2026-05-31")
    ap.add_argument("--account", help="filter to one GL account")
    ap.add_argument("-o", "--out", default="qbo_gl.csv")
    a = ap.parse_args()
    rows = mock_rows() if a.mock else fetch(a.start, a.end, a.account)
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "description", "amount", "ref"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rows -> {a.out}" + (" (MOCK DATA)" if a.mock else ""))


if __name__ == "__main__":
    main()
