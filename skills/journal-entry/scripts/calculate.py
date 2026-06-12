"""Journal entries: balance validation, accrual reversal pairs, proration."""
from __future__ import annotations


def validate_entry(lines: list[dict]) -> dict:
    """lines: [{'account': str, 'dr': float, 'cr': float}]. Checks Dr = Cr and no dual-sided lines."""
    errors = []
    for ln in lines:
        if ln.get("dr", 0) and ln.get("cr", 0):
            errors.append(f"{ln['account']}: line has both debit and credit")
        if ln.get("dr", 0) < 0 or ln.get("cr", 0) < 0:
            errors.append(f"{ln['account']}: negative amount - flip the side instead")
    total_dr = sum(ln.get("dr", 0) for ln in lines)
    total_cr = sum(ln.get("cr", 0) for ln in lines)
    if abs(total_dr - total_cr) > 0.005:
        errors.append(f"unbalanced: Dr {total_dr:,.2f} vs Cr {total_cr:,.2f}")
    return {"balanced": not errors, "total_dr": total_dr, "total_cr": total_cr,
            "errors": errors}


def reversal(lines: list[dict]) -> list[dict]:
    """Flip Dr/Cr for an accrual reversal."""
    return [{"account": ln["account"], "dr": ln.get("cr", 0), "cr": ln.get("dr", 0)}
            for ln in lines]


def prorate_accrual(monthly_amount: float, days_elapsed: int, days_in_month: int) -> float:
    return monthly_amount * days_elapsed / days_in_month


if __name__ == "__main__":
    entry = [
        {"account": "Payroll expense", "dr": 84_300.0, "cr": 0.0},
        {"account": "Accrued liabilities", "dr": 0.0, "cr": 84_300.0},
    ]
    v = validate_entry(entry)
    assert v["balanced"] and v["total_dr"] == v["total_cr"] == 84_300
    bad = validate_entry([{"account": "Cash", "dr": 100.0, "cr": 0.0}])
    assert not bad["balanced"]
    rev = reversal(entry)
    assert rev[0]["cr"] == 84_300 and rev[1]["dr"] == 84_300
    assert abs(prorate_accrual(31_000, 12, 31) - 12_000) < 1e-9
    print("entry balances | reversal flips | proration OK")
