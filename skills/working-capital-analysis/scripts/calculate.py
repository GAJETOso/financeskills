"""Working capital: DSO, DIO, DPO, cash conversion cycle, funding need."""
from __future__ import annotations


def dso(avg_receivables: float, revenue: float, days: int = 365) -> float:
    return avg_receivables / revenue * days


def dio(avg_inventory: float, cogs: float, days: int = 365) -> float:
    return avg_inventory / cogs * days


def dpo(avg_payables: float, cogs: float, days: int = 365) -> float:
    return avg_payables / cogs * days


def cash_conversion_cycle(dso_v: float, dio_v: float, dpo_v: float) -> float:
    return dso_v + dio_v - dpo_v


def working_capital_need(revenue: float, ccc_days: float, days: int = 365) -> float:
    """Rough funding requirement implied by the cycle length."""
    return revenue / days * ccc_days


if __name__ == "__main__":
    s, i, p = dso(9_475_000, 57_600_000), dio(7_490_000, 35_136_000), dpo(5_170_000, 35_136_000)
    assert abs(s - 60.04) < 0.01 and abs(i - 77.80) < 0.01 and abs(p - 53.70) < 0.01
    ccc = cash_conversion_cycle(s, i, p)
    assert abs(ccc - 84.14) < 0.01
    need = working_capital_need(57_600_000, ccc)
    assert abs(need - 57_600_000 / 365 * ccc) < 1e-6
    print(f"DSO {s:.1f} | DIO {i:.1f} | DPO {p:.1f} | CCC {ccc:.1f} days | OK")
