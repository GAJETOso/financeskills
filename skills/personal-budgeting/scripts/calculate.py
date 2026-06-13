"""Personal budgeting: 50/30/20 allocation, zero-based budget, savings rate."""
from __future__ import annotations


def fifty_thirty_twenty(monthly_income: float) -> dict[str, float]:
    if monthly_income <= 0:
        raise ValueError("monthly_income must be positive")
    return {
        "needs": round(monthly_income * 0.50, 2),
        "wants": round(monthly_income * 0.30, 2),
        "savings": round(monthly_income * 0.20, 2),
    }


def savings_rate(monthly_income: float, monthly_savings: float) -> float:
    if monthly_income <= 0:
        raise ValueError("monthly_income must be positive")
    return round(monthly_savings / monthly_income, 4)


def zero_based_budget(monthly_income: float, expenses: dict[str, float]) -> dict:
    total = sum(expenses.values())
    surplus = round(monthly_income - total, 2)
    return {
        "income": monthly_income,
        "total_expenses": round(total, 2),
        "surplus": surplus,
        "balanced": abs(surplus) < 0.01,
    }


def categorise_vs_target(
    income: float,
    actual_needs: float,
    actual_wants: float,
    actual_savings: float,
) -> dict:
    targets = fifty_thirty_twenty(income)
    return {
        "needs":   {"actual": actual_needs,   "target": targets["needs"],   "gap": round(actual_needs   - targets["needs"],   2)},
        "wants":   {"actual": actual_wants,   "target": targets["wants"],   "gap": round(actual_wants   - targets["wants"],   2)},
        "savings": {"actual": actual_savings, "target": targets["savings"], "gap": round(actual_savings - targets["savings"], 2)},
    }


if __name__ == "__main__":
    t = fifty_thirty_twenty(5_000)
    assert t == {"needs": 2_500, "wants": 1_500, "savings": 1_000}

    sr = savings_rate(5_000, 600)
    assert abs(sr - 0.12) < 1e-9

    zb = zero_based_budget(5_000, {"rent": 1_500, "food": 400, "transport": 300, "savings": 1_000, "wants": 1_800})
    assert zb["surplus"] == 0.0

    cmp = categorise_vs_target(5_000, 2_600, 1_300, 600)
    assert cmp["savings"]["gap"] == -400   # $400 short of the 20% target

    print(f"50/30/20 on $5 000: {t} | savings rate 12%: {sr:.0%} | OK")
