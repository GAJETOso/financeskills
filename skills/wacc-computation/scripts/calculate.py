"""WACC calculation helpers: CAPM, beta unlevering/relevering, WACC."""
from __future__ import annotations
from dataclasses import dataclass


def cost_of_equity_capm(
    risk_free: float, beta: float, erp: float,
    size_premium: float = 0.0, country_risk_premium: float = 0.0,
) -> float:
    """CAPM cost of equity. All inputs as decimals (0.05 = 5%)."""
    return risk_free + beta * erp + size_premium + country_risk_premium


def unlever_beta(levered_beta: float, debt_to_equity: float, tax_rate: float) -> float:
    """Hamada unlevering (debt beta assumed zero)."""
    return levered_beta / (1.0 + (1.0 - tax_rate) * debt_to_equity)


def relever_beta(unlevered_beta: float, debt_to_equity: float, tax_rate: float) -> float:
    """Hamada relevering at the target capital structure."""
    return unlevered_beta * (1.0 + (1.0 - tax_rate) * debt_to_equity)


@dataclass
class WaccInputs:
    equity_value: float
    debt_value: float
    cost_of_equity: float
    pre_tax_cost_of_debt: float
    tax_rate: float
    preferred_value: float = 0.0
    cost_of_preferred: float = 0.0


def wacc(i: WaccInputs) -> float:
    """Weighted average cost of capital from market-value weights."""
    total = i.equity_value + i.debt_value + i.preferred_value
    if total <= 0:
        raise ValueError("Capital structure values must sum to a positive number")
    return (
        i.equity_value / total * i.cost_of_equity
        + i.debt_value / total * i.pre_tax_cost_of_debt * (1.0 - i.tax_rate)
        + i.preferred_value / total * i.cost_of_preferred
    )


if __name__ == "__main__":
    re = cost_of_equity_capm(0.04, 1.2, 0.055)
    assert abs(re - 0.106) < 1e-9
    bu = unlever_beta(1.5, 0.6, 0.30)
    assert abs(bu - 1.5 / 1.42) < 1e-9
    w = wacc(WaccInputs(700, 300, 0.106, 0.08, 0.30))
    assert abs(w - (0.7 * 0.106 + 0.3 * 0.08 * 0.7)) < 1e-9
    print(f"cost of equity: {re:.2%} | unlevered beta: {bu:.3f} | WACC: {w:.2%}")
