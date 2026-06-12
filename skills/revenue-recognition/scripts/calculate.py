"""IFRS 15 / ASC 606: relative-SSP allocation, over-time recognition, financing component."""
from __future__ import annotations


def allocate_transaction_price(total_price: float, ssps: dict[str, float]) -> dict[str, float]:
    """Allocate to performance obligations pro-rata to standalone selling prices."""
    total_ssp = sum(ssps.values())
    return {po: total_price * ssp / total_ssp for po, ssp in ssps.items()}


def over_time_revenue(allocated: float, months_elapsed: float, total_months: float) -> float:
    return allocated * min(months_elapsed / total_months, 1.0)


def significant_financing_split(deferred_price: float, rate: float, years: float) -> dict:
    """Split a deferred receipt into cash selling price (revenue) and interest."""
    cash_price = deferred_price / (1 + rate) ** years
    return {"revenue": cash_price, "interest_income": deferred_price - cash_price}


def contract_liability(billed: float, recognized: float) -> float:
    return max(billed - recognized, 0.0)


if __name__ == "__main__":
    alloc = allocate_transaction_price(
        100_000, {"licence": 75_000, "support": 30_000, "implementation": 20_000})
    assert abs(alloc["licence"] - 60_000) < 1e-9
    assert abs(alloc["support"] - 24_000) < 1e-9
    assert abs(alloc["implementation"] - 16_000) < 1e-9
    assert abs(sum(alloc.values()) - 100_000) < 1e-9
    q1 = alloc["licence"] + over_time_revenue(alloc["support"], 3, 12) \
         + over_time_revenue(alloc["implementation"], 3, 12)
    assert abs(q1 - 70_000) < 1e-9
    fin = significant_financing_split(121_000, 0.10, 2)
    assert abs(fin["revenue"] - 100_000) < 1e-6 and abs(fin["interest_income"] - 21_000) < 1e-6
    assert contract_liability(100_000, q1) == 30_000
    print(f"allocation {dict((k, round(v)) for k, v in alloc.items())} | Q1 rev {q1:,.0f} | OK")
