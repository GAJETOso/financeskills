#!/usr/bin/env python3
"""Stripe -> skill-ready CSV connector.

Exports balance transactions into the CSV shape consumed by
automated-reconciliation (date, description, amount, ref) and
revenue-recognition workflows.

  python3 tools/connectors/stripe_export.py --mock -o payouts.csv     # no key needed
  STRIPE_API_KEY=sk_live_... python3 tools/connectors/stripe_export.py \
      --start 2026-05-01 --end 2026-05-31 -o payouts.csv

Network use: ONLY when run without --mock, ONLY to api.stripe.com, ONLY with
the key you supply. Nothing else in this repo makes network calls.
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://api.stripe.com/v1/balance_transactions"


def fetch(start: str, end: str) -> list[dict]:
    key = os.environ.get("STRIPE_API_KEY")
    if not key:
        sys.exit("STRIPE_API_KEY not set (or use --mock)")
    t0 = int(dt.datetime.fromisoformat(start).timestamp())
    t1 = int(dt.datetime.fromisoformat(end).timestamp()) + 86399
    rows, starting_after = [], None
    while True:
        params = {"limit": "100", "created[gte]": str(t0), "created[lte]": str(t1)}
        if starting_after:
            params["starting_after"] = starting_after
        req = urllib.request.Request(f"{API}?{urllib.parse.urlencode(params)}",
                                     headers={"Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
        rows += data["data"]
        if not data.get("has_more"):
            return rows
        starting_after = rows[-1]["id"]


def mock_rows() -> list[dict]:
    base = dt.date(2026, 5, 1)
    items = [(1, "charge", 48_200_00, "INV1041"), (4, "charge", 31_750_00, "INV1042"),
             (8, "stripe_fee", -1_450_00, "fees"), (11, "charge", 22_600_00, "INV1043"),
             (15, "refund", -3_100_00, "INV1042 partial refund"),
             (22, "charge", 56_900_00, "INV1044"), (27, "payout", -154_900_00, "PO-2026-05")]
    return [{"created": int(dt.datetime.combine(base + dt.timedelta(days=d), dt.time(10)).timestamp()),
             "type": t, "amount": a, "description": ref, "id": f"txn_mock_{i}"}
            for i, (d, t, a, ref) in enumerate(items)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mock", action="store_true", help="generate sample data, no API call")
    ap.add_argument("--start", default="2026-05-01")
    ap.add_argument("--end", default="2026-05-31")
    ap.add_argument("-o", "--out", default="stripe_transactions.csv")
    args = ap.parse_args()

    rows = mock_rows() if args.mock else fetch(args.start, args.end)
    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "description", "amount", "ref"])
        for r in rows:
            w.writerow([dt.datetime.fromtimestamp(r["created"]).date().isoformat(),
                        f"{r['type']}: {r.get('description') or ''}",
                        r["amount"] / 100.0, r["id"]])
    print(f"{len(rows)} transactions -> {args.out}"
          + (" (MOCK DATA)" if args.mock else ""))


if __name__ == "__main__":
    main()
