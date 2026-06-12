#!/usr/bin/env python3
"""Plaid -> skill-ready CSV connector.

Exports bank transactions into the CSV shape consumed by
automated-reconciliation and predictive-burn-rate.

  python3 tools/connectors/plaid_export.py --mock -o bank.csv
  PLAID_CLIENT_ID=... PLAID_SECRET=... PLAID_ACCESS_TOKEN=... \
      python3 tools/connectors/plaid_export.py --start 2026-05-01 --end 2026-05-31 -o bank.csv

Network use: ONLY without --mock, ONLY to the Plaid environment host you set
(PLAID_ENV=sandbox|development|production), ONLY with your credentials.
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.request


def fetch(start: str, end: str) -> list[dict]:
    cid, sec, tok = (os.environ.get(k) for k in
                     ("PLAID_CLIENT_ID", "PLAID_SECRET", "PLAID_ACCESS_TOKEN"))
    if not all((cid, sec, tok)):
        sys.exit("PLAID_CLIENT_ID / PLAID_SECRET / PLAID_ACCESS_TOKEN not set (or use --mock)")
    host = {"sandbox": "https://sandbox.plaid.com",
            "development": "https://development.plaid.com",
            "production": "https://production.plaid.com"}[os.environ.get("PLAID_ENV", "sandbox")]
    out, offset = [], 0
    while True:
        body = json.dumps({"client_id": cid, "secret": sec, "access_token": tok,
                           "start_date": start, "end_date": end,
                           "options": {"count": 500, "offset": offset}}).encode()
        req = urllib.request.Request(host + "/transactions/get", data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
        out += data["transactions"]
        if len(out) >= data["total_transactions"]:
            return out
        offset = len(out)


def mock_rows() -> list[dict]:
    items = [("2026-05-02", "Customer deposit - INV1041", -48_200.00),
             ("2026-05-05", "Customer deposit - INV1042", -31_750.00),
             ("2026-05-09", "Cheque 2204 - Apex Supplies", 18_400.00),
             ("2026-05-20", "Wire out - payroll", 84_300.00),
             ("2026-05-28", "Bank charges", 350.00)]
    return [{"date": d, "name": n, "amount": a, "transaction_id": f"plaid_mock_{i}"}
            for i, (d, n, a) in enumerate(items)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--start", default="2026-05-01")
    ap.add_argument("--end", default="2026-05-31")
    ap.add_argument("-o", "--out", default="bank_transactions.csv")
    args = ap.parse_args()
    rows = mock_rows() if args.mock else fetch(args.start, args.end)
    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "description", "amount", "ref"])
        for r in rows:   # Plaid: positive = money out; flip to bank-statement sign
            w.writerow([r["date"], r["name"], -r["amount"], r["transaction_id"]])
    print(f"{len(rows)} transactions -> {args.out}" + (" (MOCK DATA)" if args.mock else ""))


if __name__ == "__main__":
    main()
