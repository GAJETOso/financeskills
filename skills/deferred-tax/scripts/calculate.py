"""Deferred tax (IAS 12 / ASC 740): temporary differences, DTA/DTL, rate changes."""
from __future__ import annotations


def temporary_difference(carrying_amount: float, tax_base: float) -> float:
    """Positive = taxable temporary difference (DTL); negative = deductible (DTA)."""
    return carrying_amount - tax_base


def deferred_tax_balance(temp_diff: float, tax_rate: float) -> dict:
    """DTL for taxable differences, DTA for deductible ones, at enacted rate."""
    amount = temp_diff * tax_rate
    return {"dtl": max(amount, 0.0), "dta": max(-amount, 0.0)}


def rate_change_adjustment(temp_diff: float, old_rate: float, new_rate: float) -> float:
    """P&L (or OCI) impact of remeasuring the deferred balance at a new enacted rate."""
    return temp_diff * (new_rate - old_rate)


def effective_tax_rate(current_tax: float, deferred_tax_expense: float, pretax_income: float) -> float:
    return (current_tax + deferred_tax_expense) / pretax_income


if __name__ == "__main__":
    td = temporary_difference(1_000_000, 700_000)   # accelerated tax depreciation
    assert td == 300_000
    bal = deferred_tax_balance(td, 0.30)
    assert bal["dtl"] == 90_000 and bal["dta"] == 0
    assert deferred_tax_balance(-120_000, 0.30)["dta"] == 36_000
    assert abs(rate_change_adjustment(300_000, 0.30, 0.25) - (-15_000)) < 1e-9
    assert abs(effective_tax_rate(80_000, 10_000, 400_000) - 0.225) < 1e-12
    print(f"DTL: {bal['dtl']:,.0f} | rate-change credit: 15,000 | OK")
