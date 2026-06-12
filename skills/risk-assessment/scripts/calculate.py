"""Market risk: historical and parametric VaR, volatility, hedge ratio."""
from __future__ import annotations
import math
import statistics


def historical_var(returns: list[float], confidence: float = 0.95) -> float:
    """Loss threshold (positive number) at the given confidence, from history."""
    ordered = sorted(returns)
    idx = int((1 - confidence) * len(ordered))
    return -ordered[idx]


def parametric_var(portfolio_value: float, mu: float, sigma: float,
                   confidence: float = 0.95) -> float:
    """One-period Gaussian VaR in currency terms."""
    z = {0.90: 1.2816, 0.95: 1.6449, 0.99: 2.3263}[round(confidence, 2)]
    return portfolio_value * (z * sigma - mu)


def annualized_volatility(periodic_returns: list[float], periods_per_year: int = 252) -> float:
    return statistics.stdev(periodic_returns) * math.sqrt(periods_per_year)


def minimum_variance_hedge_ratio(corr: float, sigma_spot: float, sigma_future: float) -> float:
    return corr * sigma_spot / sigma_future


if __name__ == "__main__":
    rets = [(-1) ** i * 0.01 * (1 + i % 5) for i in range(100)]  # symmetric test set
    hv = historical_var(rets, 0.95)
    assert hv == 0.05, hv
    pv = parametric_var(10_000_000, 0.0, 0.02, 0.95)
    assert abs(pv - 10_000_000 * 1.6449 * 0.02) < 1e-6
    av = annualized_volatility([0.01, -0.01, 0.02, -0.02, 0.015])
    assert av > 0
    assert abs(minimum_variance_hedge_ratio(0.8, 0.25, 0.20) - 1.0) < 1e-12
    print(f"hist VaR 5% | param VaR {pv:,.0f} | hedge ratio 1.00 | OK")
