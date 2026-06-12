"""IFRS 9 ECL helpers: 12m/lifetime ECL, provision matrix, scenario weighting."""
from __future__ import annotations
from typing import Sequence


def ecl_single_period(pd_: float, lgd: float, ead: float, discount_factor: float = 1.0) -> float:
    """ECL for one period: PD x LGD x EAD x discount."""
    return pd_ * lgd * ead * discount_factor


def lifetime_ecl(
    marginal_pds: Sequence[float], lgds: Sequence[float],
    eads: Sequence[float], eir: float,
) -> float:
    """Lifetime ECL: sum of marginal-PD-weighted discounted losses per period (t starts at 1)."""
    if not (len(marginal_pds) == len(lgds) == len(eads)):
        raise ValueError("Input vectors must have equal length")
    return sum(
        pd_ * lgd * ead / (1.0 + eir) ** (t + 1)
        for t, (pd_, lgd, ead) in enumerate(zip(marginal_pds, lgds, eads))
    )


def provision_matrix(aging_balances: dict[str, float], loss_rates: dict[str, float]) -> dict[str, float]:
    """Simplified-approach provision per aging bucket; includes 'total'."""
    missing = set(aging_balances) - set(loss_rates)
    if missing:
        raise ValueError(f"No loss rate for buckets: {missing}")
    out = {b: aging_balances[b] * loss_rates[b] for b in aging_balances}
    out["total"] = sum(out.values())
    return out


def scenario_weighted_ecl(scenario_ecls: Sequence[float], weights: Sequence[float]) -> float:
    """Probability-weighted ECL across macro scenarios; weights must sum to 1."""
    if abs(sum(weights) - 1.0) > 1e-9:
        raise ValueError("Scenario weights must sum to 1")
    return sum(e * w for e, w in zip(scenario_ecls, weights))


if __name__ == "__main__":
    assert abs(ecl_single_period(0.02, 0.45, 1_000_000) - 9_000.0) < 1e-6
    le = lifetime_ecl([0.02, 0.03], [0.45, 0.45], [1_000_000, 900_000], 0.10)
    assert abs(le - (9000 / 1.1 + 12150 / 1.21)) < 1e-6
    pm = provision_matrix({"current": 500_000, "90+": 50_000}, {"current": 0.01, "90+": 0.40})
    assert abs(pm["total"] - 25_000.0) < 1e-6
    assert abs(scenario_weighted_ecl([100, 150, 300], [0.5, 0.3, 0.2]) - 155.0) < 1e-9
    print(f"lifetime ECL: {le:,.2f} | matrix total: {pm['total']:,.2f}")
