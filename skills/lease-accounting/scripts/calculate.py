"""IFRS 16 / ASC 842 lease measurement: liability PV, amortization, ROU depreciation."""
from __future__ import annotations


def lease_liability(payment: float, rate: float, term_years: int, in_arrears: bool = True) -> float:
    """PV of level lease payments at the discount rate (IBR or implicit rate)."""
    pv = payment * (1 - (1 + rate) ** -term_years) / rate
    return pv if in_arrears else pv * (1 + rate)


def amortization_schedule(payment: float, rate: float, term_years: int) -> list[dict]:
    """Year-by-year liability rollforward for payments in arrears."""
    bal = lease_liability(payment, rate, term_years)
    rows = []
    for yr in range(1, term_years + 1):
        interest = bal * rate
        principal = payment - interest
        bal -= principal
        rows.append({"year": yr, "interest": interest, "principal": principal,
                     "closing_liability": max(bal, 0.0)})
    return rows


def rou_depreciation(rou_asset: float, term_years: int) -> float:
    """Straight-line ROU depreciation (no residual)."""
    return rou_asset / term_years


if __name__ == "__main__":
    liab = lease_liability(250_000, 0.07, 5)
    assert abs(liab - 1_025_049.36) < 1.0, liab
    sched = amortization_schedule(250_000, 0.07, 5)
    assert abs(sched[0]["interest"] - liab * 0.07) < 0.01
    assert abs(sched[-1]["closing_liability"]) < 0.01
    assert abs(sum(r["principal"] for r in sched) - liab) < 0.01
    assert abs(rou_depreciation(liab, 5) - 205_009.87) < 0.01
    print(f"liability: {liab:,.2f} | y1 interest: {sched[0]['interest']:,.2f} | OK")
