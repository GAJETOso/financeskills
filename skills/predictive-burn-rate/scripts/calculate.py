"""Burn and runway math: net burn, simple and growth-adjusted runway, collections curve."""
from __future__ import annotations
from typing import Sequence


def net_burn(gross_outflows: float, collections: float) -> float:
    return gross_outflows - collections


def simple_runway(cash: float, avg_net_burn: float) -> float:
    """Months of runway at constant burn. Returns inf if cash-flow positive."""
    return float("inf") if avg_net_burn <= 0 else cash / avg_net_burn


def growth_adjusted_runway(cash: float, current_burn: float, monthly_growth: float,
                           floor: float = 0.0, max_months: int = 240) -> int:
    """Months until cash drops below `floor` when burn grows at a monthly rate."""
    months, burn = 0, current_burn
    while cash > floor and months < max_months:
        cash -= burn
        burn *= 1 + monthly_growth
        months += 1
    return months


def apply_collections_curve(invoiced_by_month: Sequence[float], curve: Sequence[float]) -> list[float]:
    """Convert invoicing into expected cash receipts via a lag distribution.
    curve[k] = share collected k months after invoicing; should sum to <= 1 (residual = bad debt)."""
    if sum(curve) > 1.0 + 1e-9:
        raise ValueError("Collections curve cannot exceed 100%")
    horizon = len(invoiced_by_month) + len(curve) - 1
    receipts = [0.0] * horizon
    for m, inv in enumerate(invoiced_by_month):
        for k, share in enumerate(curve):
            receipts[m + k] += inv * share
    return receipts


if __name__ == "__main__":
    assert simple_runway(1_200_000, 100_000) == 12
    ga = growth_adjusted_runway(1_200_000, 100_000, 0.05)
    assert ga < 12  # growing burn shortens runway
    rec = apply_collections_curve([100, 100], [0.2, 0.5, 0.25])
    assert abs(rec[1] - (50 + 20)) < 1e-9
    print(f"simple 12 mo vs growth-adjusted {ga} mo | receipts {['%.0f' % r for r in rec]}")
