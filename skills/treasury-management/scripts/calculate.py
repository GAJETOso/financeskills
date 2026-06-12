"""Treasury: liquidity metrics, cash forecasting position, FX forwards (CIP)."""
from __future__ import annotations


def liquidity_runway_days(unrestricted_cash: float, committed_facilities: float,
                          daily_net_outflow: float) -> float:
    return (unrestricted_cash + committed_facilities) / daily_net_outflow


def cash_position(opening: float, receipts: list[float], disbursements: list[float]) -> float:
    return opening + sum(receipts) - sum(disbursements)


def fx_forward_rate(spot: float, domestic_rate: float, foreign_rate: float,
                    days: int, basis: int = 360) -> float:
    """Covered interest parity: F = S x (1 + r_dom x t) / (1 + r_for x t)."""
    t = days / basis
    return spot * (1 + domestic_rate * t) / (1 + foreign_rate * t)


def hedge_pnl(notional_foreign: float, contracted_forward: float, spot_at_maturity: float) -> float:
    """P&L of a forward purchase of foreign currency vs buying at maturity spot."""
    return notional_foreign * (spot_at_maturity - contracted_forward)


if __name__ == "__main__":
    assert abs(liquidity_runway_days(8_000_000, 4_000_000, 150_000) - 80.0) < 1e-9
    assert cash_position(1_000_000, [500_000, 200_000], [300_000]) == 1_400_000
    f = fx_forward_rate(1500.0, 0.22, 0.05, 180)   # e.g. NGN per USD
    assert abs(f - 1500 * (1 + 0.22 * 0.5) / (1 + 0.05 * 0.5)) < 1e-9
    assert f > 1500   # higher domestic rate -> forward discount on domestic ccy
    assert hedge_pnl(1_000_000, f, f + 50) == 50_000_000 / 1000 * 1000
    print(f"runway 80 days | 6m forward {f:,.2f} | OK")
