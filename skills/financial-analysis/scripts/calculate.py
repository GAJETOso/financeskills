"""Core financial ratios with divide-by-zero safety and DuPont decomposition."""
from __future__ import annotations


def safe_div(num: float, den: float) -> float | None:
    """None when the denominator is zero/negative-meaningless rather than raising."""
    return None if den == 0 else num / den


def liquidity_ratios(current_assets: float, inventory: float, current_liabilities: float) -> dict:
    return {
        "current_ratio": safe_div(current_assets, current_liabilities),
        "quick_ratio": safe_div(current_assets - inventory, current_liabilities),
    }


def profitability_ratios(revenue: float, cogs: float, net_income: float, equity: float, assets: float) -> dict:
    return {
        "gross_margin": safe_div(revenue - cogs, revenue),
        "net_margin": safe_div(net_income, revenue),
        "roe": safe_div(net_income, equity) if equity > 0 else None,  # negative equity: ROE meaningless
        "roa": safe_div(net_income, assets),
    }


def dupont(net_income: float, revenue: float, assets: float, equity: float) -> dict:
    """ROE = margin x asset turnover x leverage."""
    if equity <= 0:
        return {"roe": None, "note": "negative or nil equity - DuPont not meaningful"}
    margin = safe_div(net_income, revenue)
    turnover = safe_div(revenue, assets)
    leverage = safe_div(assets, equity)
    return {"net_margin": margin, "asset_turnover": turnover,
            "equity_multiplier": leverage, "roe": margin * turnover * leverage}


def solvency_ratios(total_liabilities: float, equity: float, ebit: float, interest: float) -> dict:
    return {
        "debt_to_equity": safe_div(total_liabilities, equity) if equity > 0 else None,
        "interest_coverage": safe_div(ebit, interest),
    }


if __name__ == "__main__":
    d = dupont(120, 1000, 800, 400)
    assert abs(d["roe"] - 0.30) < 1e-9
    assert profitability_ratios(1000, 600, 120, -50, 800)["roe"] is None
    assert liquidity_ratios(500, 200, 250)["quick_ratio"] == 1.2
    print(f"DuPont ROE {d['roe']:.1%} = {d['net_margin']:.1%} x {d['asset_turnover']:.2f} x {d['equity_multiplier']:.2f}")
