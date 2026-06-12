"""Product profitability: cost allocation, contribution margin, unit economics."""
from __future__ import annotations


def allocate_costs(shared_cost: float, drivers: dict[str, float]) -> dict[str, float]:
    """Allocate a shared cost pool pro-rata to a driver (revenue, units, hours...)."""
    total = sum(drivers.values())
    return {k: shared_cost * v / total for k, v in drivers.items()}


def product_pnl(revenue: float, direct_costs: float, allocated_costs: float) -> dict:
    cm = revenue - direct_costs
    return {"contribution_margin": cm, "cm_pct": cm / revenue,
            "fully_loaded_profit": cm - allocated_costs}


def unit_economics(arpu: float, variable_cost_per_user: float, cac: float) -> dict:
    cm = arpu - variable_cost_per_user
    return {"contribution_per_user": cm, "cac_payback_periods": cac / cm}


if __name__ == "__main__":
    alloc = allocate_costs(900_000, {"A": 6_000_000, "B": 3_000_000})
    assert alloc["A"] == 600_000 and alloc["B"] == 300_000
    p = product_pnl(6_000_000, 3_600_000, alloc["A"])
    assert p["contribution_margin"] == 2_400_000 and abs(p["cm_pct"] - 0.4) < 1e-12
    assert p["fully_loaded_profit"] == 1_800_000
    u = unit_economics(45.0, 15.0, 360.0)
    assert u["cac_payback_periods"] == 12.0
    print(f"product A profit {p['fully_loaded_profit']:,.0f} | CAC payback 12 | OK")
