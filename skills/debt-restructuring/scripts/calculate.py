"""Debt restructuring: priority waterfall recoveries, haircuts, NPV of modified terms."""
from __future__ import annotations


def waterfall(enterprise_value: float, tranches: list[tuple[str, float]]) -> list[dict]:
    """tranches: (name, claim) in priority order. Returns recovery per tranche."""
    remaining = enterprise_value
    out = []
    for name, claim in tranches:
        paid = min(claim, max(remaining, 0.0))
        out.append({"tranche": name, "claim": claim, "recovery": paid,
                    "recovery_pct": paid / claim if claim else 0.0})
        remaining -= paid
    return out


def haircut_pct(face_value: float, new_value: float) -> float:
    return 1 - new_value / face_value


def npv_of_terms(principal: float, rate: float, years: int, discount_rate: float) -> float:
    """PV of interest-only payments plus bullet principal, at the discount rate."""
    coupons = sum(principal * rate / (1 + discount_rate) ** t for t in range(1, years + 1))
    return coupons + principal / (1 + discount_rate) ** years


if __name__ == "__main__":
    w = waterfall(800.0, [("Senior secured", 500.0), ("Senior unsecured", 400.0),
                          ("Subordinated", 200.0)])
    assert w[0]["recovery"] == 500 and w[0]["recovery_pct"] == 1.0
    assert w[1]["recovery"] == 300 and abs(w[1]["recovery_pct"] - 0.75) < 1e-12
    assert w[2]["recovery"] == 0
    assert abs(haircut_pct(400, 300) - 0.25) < 1e-12
    old = npv_of_terms(1000, 0.10, 5, 0.12)
    new = npv_of_terms(1000, 0.06, 8, 0.12)
    assert new < old   # extended maturity + lower coupon = creditor concession
    print(f"unsecured recovery 75% | concession NPV {old - new:,.1f} | OK")
