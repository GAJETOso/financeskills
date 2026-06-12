"""Crypto accounting: ASU 2023-08 fair-value remeasurement vs IAS 38 cost-impairment."""
from __future__ import annotations


def fair_value_remeasurement(carrying: float, fair_value: float) -> dict:
    """US GAAP (ASU 2023-08): measure at fair value, changes through net income."""
    return {"new_carrying": fair_value, "pnl_impact": fair_value - carrying}


def cost_less_impairment(cost: float, lowest_observed: float, current_price: float) -> dict:
    """IAS 38 cost model: impair to lowest observed; no reversal above carrying
    (simplified - IFRS allows reversal to the impaired-cost ceiling)."""
    carrying = min(cost, lowest_observed)
    return {"carrying": carrying, "impairment_loss": cost - carrying,
            "unrecognized_gain": max(current_price - carrying, 0.0)}


def realized_gain_fifo(lots: list[tuple[float, float]], units_sold: float,
                       sale_price: float) -> float:
    """lots: (units, unit_cost) in acquisition order."""
    remaining, cost_basis = units_sold, 0.0
    for units, unit_cost in lots:
        take = min(units, remaining)
        cost_basis += take * unit_cost
        remaining -= take
        if remaining <= 0:
            break
    if remaining > 1e-9:
        raise ValueError("sold more units than held")
    return units_sold * sale_price - cost_basis


if __name__ == "__main__":
    fv = fair_value_remeasurement(60_000, 75_000)
    assert fv["pnl_impact"] == 15_000
    ci = cost_less_impairment(60_000, 42_000, 75_000)
    assert ci["impairment_loss"] == 18_000 and ci["unrecognized_gain"] == 33_000
    g = realized_gain_fifo([(2.0, 30_000), (1.0, 50_000)], 2.5, 70_000)
    assert g == 2.5 * 70_000 - (2 * 30_000 + 0.5 * 50_000) == 90_000
    print(f"FV gain 15,000 | impairment 18,000 | FIFO gain {g:,.0f} | OK")
