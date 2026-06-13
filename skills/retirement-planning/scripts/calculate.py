"""Retirement planning: future value, gap analysis, safe withdrawal, contribution solver."""
from __future__ import annotations
import math


def future_value(
    principal: float,
    annual_rate: float,
    years: int,
    monthly_contribution: float = 0.0,
) -> float:
    """FV of lump sum + regular monthly contributions compounded monthly."""
    if annual_rate == 0:
        return round(principal + monthly_contribution * years * 12, 2)
    r = annual_rate / 12
    n = years * 12
    fv_principal = principal * (1 + r) ** n
    fv_contributions = monthly_contribution * (((1 + r) ** n - 1) / r)
    return round(fv_principal + fv_contributions, 2)


def required_monthly_contribution(
    target: float,
    principal: float,
    annual_rate: float,
    years: int,
) -> float:
    """Monthly contribution needed to reach target given existing principal."""
    if annual_rate == 0:
        remaining = target - principal
        return round(remaining / (years * 12), 2)
    r = annual_rate / 12
    n = years * 12
    fv_principal = principal * (1 + r) ** n
    fv_factor = ((1 + r) ** n - 1) / r
    pmt = (target - fv_principal) / fv_factor
    return round(pmt, 2)


def safe_withdrawal(portfolio: float, rate: float = 0.04) -> dict[str, float]:
    annual = round(portfolio * rate, 2)
    return {"annual": annual, "monthly": round(annual / 12, 2)}


def nest_egg_target(desired_annual_income: float, rate: float = 0.04) -> float:
    return round(desired_annual_income / rate, 2)


def replacement_ratio(pre_retirement_income: float, retirement_income: float) -> float:
    if pre_retirement_income <= 0:
        raise ValueError("pre_retirement_income must be positive")
    return round(retirement_income / pre_retirement_income, 4)


if __name__ == "__main__":
    fv = future_value(45_000, 0.07, 30, 500)
    assert abs(fv - 975_228) < 2_000, f"FV={fv}"

    req = required_monthly_contribution(1_500_000, 45_000, 0.07, 30)
    fv_check = future_value(45_000, 0.07, 30, req)
    assert abs(fv_check - 1_500_000) < 10, f"FV check={fv_check}"

    sw = safe_withdrawal(1_500_000)
    assert sw["annual"] == 60_000.0

    target = nest_egg_target(60_000)
    assert target == 1_500_000.0

    rr = replacement_ratio(100_000, 70_000)
    assert abs(rr - 0.70) < 1e-9

    print(
        f"FV $45k+$500/mo @ 7% for 30yr: ${fv:,.0f} | "
        f"Required PMT to reach $1.5M: ${req:,.2f}/mo | OK"
    )
