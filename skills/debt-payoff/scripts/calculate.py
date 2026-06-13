"""Debt payoff: avalanche and snowball simulators, interest calculations."""
from __future__ import annotations
import copy


def monthly_interest(balance: float, annual_rate: float) -> float:
    return round(balance * (annual_rate / 12), 2)


def _run_schedule(debts: list[dict], monthly_budget: float, strategy: str) -> dict:
    """
    Simulate month-by-month payoff.

    debts: list of {"name": str, "balance": float, "annual_rate": float, "min_payment": float}
    strategy: "avalanche" (highest rate first) or "snowball" (lowest balance first)
    Returns: {"months": int, "total_interest": float, "total_paid": float}
    """
    state = copy.deepcopy(debts)
    total_interest = 0.0
    total_paid = 0.0
    months = 0

    while any(d["balance"] > 0 for d in state):
        months += 1
        if months > 1200:  # 100-year guard
            break

        # Apply monthly interest
        for d in state:
            if d["balance"] > 0:
                interest = monthly_interest(d["balance"], d["annual_rate"])
                d["balance"] = round(d["balance"] + interest, 2)
                total_interest += interest

        # Pay minimums
        extra = monthly_budget
        for d in state:
            if d["balance"] > 0:
                payment = min(d["min_payment"], d["balance"])
                d["balance"] = round(d["balance"] - payment, 2)
                total_paid += payment
                extra -= payment

        # Rank target debt
        active = [d for d in state if d["balance"] > 0]
        if not active:
            break
        if strategy == "avalanche":
            target = max(active, key=lambda d: d["annual_rate"])
        else:  # snowball
            target = min(active, key=lambda d: d["balance"])

        # Apply extra to target
        if extra > 0:
            payment = min(extra, target["balance"])
            target["balance"] = round(target["balance"] - payment, 2)
            total_paid += payment

    return {
        "months": months,
        "total_interest": round(total_interest, 2),
        "total_paid": round(total_paid, 2),
    }


def avalanche_schedule(debts: list[dict], monthly_budget: float) -> dict:
    return _run_schedule(debts, monthly_budget, "avalanche")


def snowball_schedule(debts: list[dict], monthly_budget: float) -> dict:
    return _run_schedule(debts, monthly_budget, "snowball")


def interest_savings(debts: list[dict], monthly_budget: float) -> dict:
    av = avalanche_schedule(debts, monthly_budget)
    sn = snowball_schedule(debts, monthly_budget)
    return {
        "avalanche_interest": av["total_interest"],
        "snowball_interest": sn["total_interest"],
        "savings_from_avalanche": round(sn["total_interest"] - av["total_interest"], 2),
        "avalanche_months": av["months"],
        "snowball_months": sn["months"],
    }


if __name__ == "__main__":
    debts = [
        {"name": "Credit Card", "balance": 3_000.0, "annual_rate": 0.20, "min_payment": 60.0},
        {"name": "Car Loan",    "balance": 5_000.0, "annual_rate": 0.06, "min_payment": 100.0},
    ]
    budget = 400.0

    av = avalanche_schedule(debts, budget)
    sn = snowball_schedule(debts, budget)

    assert av["total_interest"] <= sn["total_interest"], "Avalanche must pay <= interest than snowball"
    assert av["months"] > 0 and sn["months"] > 0

    cmp = interest_savings(debts, budget)
    assert cmp["savings_from_avalanche"] >= 0

    print(
        f"Avalanche: {av['months']} months, ${av['total_interest']:,.2f} interest | "
        f"Snowball: {sn['months']} months, ${sn['total_interest']:,.2f} interest | "
        f"Savings: ${cmp['savings_from_avalanche']:,.2f} | OK"
    )
