"""Net worth tracking: assets, liabilities, ratios, period-over-period change."""
from __future__ import annotations


def net_worth(assets: dict[str, float], liabilities: dict[str, float]) -> float:
    return round(sum(assets.values()) - sum(liabilities.values()), 2)


def asset_allocation(assets: dict[str, float]) -> dict[str, float]:
    total = sum(assets.values())
    if total == 0:
        raise ValueError("Total assets must be non-zero")
    return {k: round(v / total, 4) for k, v in assets.items()}


def debt_to_asset_ratio(assets: dict[str, float], liabilities: dict[str, float]) -> float:
    total_assets = sum(assets.values())
    if total_assets == 0:
        raise ValueError("Total assets must be non-zero")
    return round(sum(liabilities.values()) / total_assets, 4)


def period_change(current_nw: float, previous_nw: float) -> dict:
    delta = round(current_nw - previous_nw, 2)
    pct = round(delta / abs(previous_nw), 4) if previous_nw != 0 else None
    return {"dollar_change": delta, "pct_change": pct}


def liquid_asset_ratio(liquid_assets: float, total_assets: float) -> float:
    if total_assets <= 0:
        raise ValueError("total_assets must be positive")
    return round(liquid_assets / total_assets, 4)


if __name__ == "__main__":
    assets = {
        "checking": 3_000,
        "savings": 12_000,
        "retirement_401k": 68_000,
        "car": 15_000,
    }
    liabilities = {
        "car_loan": 9_000,
        "student_loan": 22_000,
        "credit_card": 3_500,
    }

    nw = net_worth(assets, liabilities)
    assert nw == 63_500.0, f"NW={nw}"

    alloc = asset_allocation(assets)
    assert abs(sum(alloc.values()) - 1.0) < 1e-9

    dta = debt_to_asset_ratio(assets, liabilities)
    assert abs(dta - 34_500 / 98_000) < 1e-4, f"DTA={dta}"

    chg = period_change(63_500, 54_000)
    assert chg["dollar_change"] == 9_500

    liq = liquid_asset_ratio(15_000, 98_000)
    assert abs(liq - 15_000 / 98_000) < 1e-4

    print(
        f"Net worth: ${nw:,.0f} | Debt-to-asset: {dta:.1%} | "
        f"Liquid ratio: {liq:.1%} | OK"
    )
