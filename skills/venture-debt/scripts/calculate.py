"""Venture debt: interest-only then amortizing schedules, warrant coverage, runway impact."""
from __future__ import annotations


def payment_schedule(principal: float, annual_rate: float, io_months: int,
                     amort_months: int) -> list[dict]:
    """Monthly schedule: interest-only period then level amortization."""
    r = annual_rate / 12
    rows = []
    for m in range(1, io_months + 1):
        rows.append({"month": m, "interest": principal * r, "principal": 0.0,
                     "balance": principal})
    pmt = principal * r / (1 - (1 + r) ** -amort_months)
    bal = principal
    for m in range(io_months + 1, io_months + amort_months + 1):
        interest = bal * r
        princ = pmt - interest
        bal -= princ
        rows.append({"month": m, "interest": interest, "principal": princ,
                     "balance": max(bal, 0.0)})
    return rows


def warrant_coverage_shares(loan: float, coverage_pct: float, strike: float) -> float:
    """Shares under warrant = (loan x coverage%) / strike price."""
    return loan * coverage_pct / strike


def total_cost_of_debt(rows: list[dict], closing_fee: float, final_payment_fee: float) -> float:
    return sum(r["interest"] for r in rows) + closing_fee + final_payment_fee


def runway_extension_months(net_loan_proceeds: float, monthly_burn: float) -> float:
    return net_loan_proceeds / monthly_burn


if __name__ == "__main__":
    sched = payment_schedule(5_000_000, 0.12, 12, 24)
    assert len(sched) == 36
    assert all(r["principal"] == 0 for r in sched[:12])
    assert abs(sched[11]["balance"] - 5_000_000) < 1e-6
    assert abs(sched[-1]["balance"]) < 0.01
    assert abs(sum(r["principal"] for r in sched) - 5_000_000) < 0.01
    w = warrant_coverage_shares(5_000_000, 0.10, 2.50)
    assert w == 200_000
    assert abs(runway_extension_months(4_900_000, 700_000) - 7.0) < 1e-12
    print(f"36-month schedule OK | warrants {w:,.0f} shares | +7.0 months runway | OK")
