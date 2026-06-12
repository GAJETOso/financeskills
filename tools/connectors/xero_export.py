#!/usr/bin/env python3
"""Xero -> skill-ready CSV connector.

Exports bank transactions into (date, description, amount, ref) for
automated-reconciliation and treasury-management.

  python3 xero_export.py --mock -o bank.csv
  XERO_ACCESS_TOKEN=... XERO_TENANT_ID=... python3 xero_export.py \
      --since 2026-05-01 -o bank.csv

Network: only without --mock, only to api.xero.com, only with your token.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
import urllib.request

API = "https://api.xero.com/api.xro/2.0/BankTransactions"


def fetch(since: str) -> list[dict]:
    tok, tenant = os.environ.get("XERO_ACCESS_TOKEN"), os.environ.get("XERO_TENANT_ID")
    if not (tok and tenant):
        sys.exit("XERO_ACCESS_TOKEN / XERO_TENANT_ID not set (or use --mock)")
    req = urllib.request.Request(API, headers={
        "Authorization": f"Bearer {tok}", "Xero-Tenant-Id": tenant,
        "Accept": "application/json",
        "If-Modified-Since": f"{since}T00:00:00"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    out = []
    for t in data.get("BankTransactions", []):
        sign = -1 if t.get("Type") == "SPEND" else 1
        out.append({"date": t.get("DateString", "")[:10],
                    "description": (t.get("Contact") or {}).get("Name", "") or t.get("Reference", ""),
                    "amount": sign * float(t.get("Total", 0)),
                    "ref": t.get("BankTransactionID", "")[:13]})
    return out


def mock_rows() -> list[dict]:
    return [
        {"date": "2026-05-05", "description": "Acme Industries receipt", "amount": 31_750.00, "ref": "xero_mock_1"},
        {"date": "2026-05-15", "description": "Delta Logistics payment", "amount": -9_750.00, "ref": "xero_mock_2"},
        {"date": "2026-05-28", "description": "Bank fees", "amount": -350.00, "ref": "xero_mock_3"},
    ]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--since", default="2026-05-01")
    ap.add_argument("-o", "--out", default="xero_bank.csv")
    a = ap.parse_args()
    rows = mock_rows() if a.mock else fetch(a.since)
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "description", "amount", "ref"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rows -> {a.out}" + (" (MOCK DATA)" if a.mock else ""))


if __name__ == "__main__":
    main()
