"""Budgeting & forecasting: driver-based projection, CAGR, scenario deltas."""
from __future__ import annotations


def cagr(beginning: float, ending: float, years: float) -> float:
    if beginning <= 0 or years <= 0:
        raise ValueError("beginning value and years must be positive")
    return (ending / beginning) ** (1 / years) - 1


def project_revenue(base: float, growth_rates: list[float]) -> list[float]:
    out, val = [], base
    for g in growth_rates:
        val *= 1 + g
        out.append(val)
    return out


def driver_based_budget(units: float, price: float, variable_cost_pct: float,
                        fixed_costs: float) -> dict:
    revenue = units * price
    var = revenue * variable_cost_pct
    return {"revenue": revenue, "variable_costs": var, "fixed_costs": fixed_costs,
            "operating_income": revenue - var - fixed_costs}


def scenario_delta(base_case: dict, scenario: dict) -> dict:
    return {k: scenario[k] - base_case[k] for k in base_case}


if __name__ == "__main__":
    g = cagr(48_000_000, 57_600_000, 1)
    assert abs(g - 0.20) < 1e-12
    proj = project_revenue(57_600_000, [0.15, 0.12, 0.10])
    assert abs(proj[-1] - 57_600_000 * 1.15 * 1.12 * 1.10) < 1e-6
    b = driver_based_budget(100_000, 600.0, 0.55, 18_000_000)
    assert abs(b["operating_income"] - 9_000_000) < 1e-6
    d = scenario_delta(b, driver_based_budget(90_000, 600.0, 0.55, 18_000_000))
    assert abs(d["operating_income"] - (-2_700_000)) < 1e-6
    print(f"CAGR {g:.0%} | budget OI {b['operating_income']:,.0f} | OK")
