"""ARO/decommissioning provision math: initial PV, accretion schedule, revisions."""
from __future__ import annotations


def initial_aro(current_cost: float, inflation: float, discount: float, years: int) -> float:
    """PV of an inflated future restoration cost."""
    future = current_cost * (1 + inflation) ** years
    return future / (1 + discount) ** years


def accretion_schedule(opening_pv: float, discount: float, years: int) -> list[dict[str, float]]:
    """Year-by-year unwinding; closing balance equals the settlement amount."""
    rows, bal = [], opening_pv
    for y in range(1, years + 1):
        accretion = bal * discount
        rows.append({"year": y, "opening": round(bal, 2),
                     "accretion": round(accretion, 2), "closing": round(bal + accretion, 2)})
        bal += accretion
    return rows


def revision_adjustment(
    old_remaining_pv: float, new_cost_estimate: float,
    discount: float, years_remaining: int, inflation: float = 0.0,
) -> float:
    """IFRIC 1 revision: returns the adjustment to BOTH provision and asset (+ = increase)."""
    new_pv = initial_aro(new_cost_estimate, inflation, discount, years_remaining)
    return new_pv - old_remaining_pv


if __name__ == "__main__":
    pv = initial_aro(1_000_000, 0.0, 0.08, 3)
    assert abs(pv - 1_000_000 / 1.08 ** 3) < 1e-6
    sched = accretion_schedule(pv, 0.08, 3)
    assert abs(sched[-1]["closing"] - 1_000_000) < 1.0  # ties to settlement
    adj = revision_adjustment(pv, 1_200_000, 0.08, 3)
    assert adj > 0
    print(f"initial PV {pv:,.2f} | final closing {sched[-1]['closing']:,.2f} | revision +{adj:,.2f}")
