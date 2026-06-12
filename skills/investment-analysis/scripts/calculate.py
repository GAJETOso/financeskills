"""Capital budgeting: NPV, IRR, payback, profitability index."""
from __future__ import annotations


def npv(rate: float, cashflows: list[float]) -> float:
    """cashflows[0] at t=0 (usually negative)."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows: list[float], lo: float = -0.99, hi: float = 10.0,
        tol: float = 1e-7) -> float:
    """Bisection IRR; requires a sign change over [lo, hi]."""
    f_lo, f_hi = npv(lo, cashflows), npv(hi, cashflows)
    if f_lo * f_hi > 0:
        raise ValueError("no sign change - IRR not bracketed")
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def payback_period(cashflows: list[float]) -> float:
    """Years to recover the t=0 outflow (fractional, undiscounted)."""
    cum = cashflows[0]
    for t, cf in enumerate(cashflows[1:], 1):
        if cum + cf >= 0:
            return t - 1 + (-cum) / cf
        cum += cf
    raise ValueError("never pays back")


def profitability_index(rate: float, cashflows: list[float]) -> float:
    return npv(rate, [0.0] + cashflows[1:]) / -cashflows[0]


if __name__ == "__main__":
    cfs = [-1_000_000, 400_000, 400_000, 400_000, 400_000]
    v = npv(0.10, cfs)
    assert abs(v - 267_946.47) < 1.0
    r = irr(cfs)
    assert abs(npv(r, cfs)) < 1e-3 and abs(r - 0.21862) < 1e-3
    assert abs(payback_period(cfs) - 2.5) < 1e-9
    assert abs(profitability_index(0.10, cfs) - 1.26795) < 1e-4
    print(f"NPV {v:,.0f} | IRR {r:.2%} | payback 2.5y | OK")
