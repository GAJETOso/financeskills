#!/usr/bin/env python3
"""Generic export bridge: map ANY ERP/bank CSV export to the skill-ready shape.

Handles locale issues on the way through: thousands separators, currency
symbols, parentheses negatives, and DD/MM/YYYY vs MM/DD/YYYY dates.

  python3 csv_mapper.py sap_export.csv -o gl.csv \
      --date "Posting Date" --desc "Text" --amount "Amount in LC" --ref "Document No." \
      --dayfirst

No network. Pure file-in, file-out.
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import re
import sys

AMOUNT_RE = re.compile(r"[^\d.,\-()]")


def parse_amount(raw: str) -> float:
    """'₦1.234.567,89', '(1,234.50)', '$ 1,234.50-' -> float."""
    s = AMOUNT_RE.sub("", str(raw).strip())
    neg = "(" in s or s.endswith("-") or s.startswith("-")
    s = s.strip("()-")
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):          # 1.234.567,89 (EU)
            s = s.replace(".", "").replace(",", ".")
        else:                                     # 1,234,567.89 (US/UK)
            s = s.replace(",", "")
    elif "," in s:
        frac = s.rsplit(",", 1)[1]
        s = s.replace(",", ".") if len(frac) in (1, 2) else s.replace(",", "")
    if not s:
        return 0.0
    return -float(s) if neg else float(s)


def parse_date(raw: str, dayfirst: bool) -> str:
    s = str(raw).strip()[:10].replace(".", "-").replace("/", "-")
    parts = s.split("-")
    try:
        if len(parts[0]) == 4:
            d = dt.date(int(parts[0]), int(parts[1]), int(parts[2]))
        elif dayfirst:
            d = dt.date(int(parts[2]), int(parts[1]), int(parts[0]))
        else:
            d = dt.date(int(parts[2]), int(parts[0]), int(parts[1]))
        return d.isoformat()
    except (ValueError, IndexError):
        return s


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("infile")
    ap.add_argument("-o", "--out", default="mapped.csv")
    ap.add_argument("--date", required=True, help="source column for date")
    ap.add_argument("--desc", required=True, help="source column for description")
    ap.add_argument("--amount", required=True, help="source column for amount")
    ap.add_argument("--ref", default=None, help="source column for reference")
    ap.add_argument("--dayfirst", action="store_true", help="dates are DD/MM/YYYY")
    ap.add_argument("--negate", action="store_true", help="flip amount signs")
    a = ap.parse_args()

    with open(a.infile, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [c for c in (a.date, a.desc, a.amount) if c not in reader.fieldnames]
        if missing:
            sys.exit(f"columns not found: {missing}. Available: {reader.fieldnames}")
        rows = []
        for i, r in enumerate(reader):
            amt = parse_amount(r[a.amount])
            rows.append({"date": parse_date(r[a.date], a.dayfirst),
                         "description": r[a.desc].strip(),
                         "amount": -amt if a.negate else amt,
                         "ref": (r.get(a.ref) or f"ROW-{i+1}").strip() if a.ref else f"ROW-{i+1}"})
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "description", "amount", "ref"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rows mapped -> {a.out}")


if __name__ == "__main__":
    main()


def _selftest() -> None:
    assert parse_amount("₦1.234.567,89") == 1234567.89
    assert parse_amount("(1,234.50)") == -1234.50
    assert parse_amount("$ 1,234.50-") == -1234.50
    assert parse_amount("1234") == 1234.0
    assert parse_date("31/05/2026", True) == "2026-05-31"
    assert parse_date("05/31/2026", False) == "2026-05-31"
    assert parse_date("2026-05-31", False) == "2026-05-31"
