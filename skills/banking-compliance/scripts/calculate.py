"""Basel III capital and liquidity: capital ratios, leverage ratio, LCR, NSFR."""
from __future__ import annotations


def capital_ratio(capital: float, rwa: float) -> float:
    """Works for CET1, Tier 1, or Total capital against risk-weighted assets."""
    return capital / rwa


def rwa_from_exposures(exposures: list[tuple[float, float]]) -> float:
    """exposures: list of (exposure_amount, risk_weight)."""
    return sum(amt * rw for amt, rw in exposures)


def leverage_ratio(tier1: float, total_exposure: float) -> float:
    return tier1 / total_exposure


def lcr(hqla: float, net_outflows_30d: float) -> float:
    return hqla / net_outflows_30d


def nsfr(available_stable_funding: float, required_stable_funding: float) -> float:
    return available_stable_funding / required_stable_funding


def buffer_check(cet1_ratio: float, minimum: float = 0.045, conservation: float = 0.025,
                 countercyclical: float = 0.0, dsib: float = 0.0) -> dict:
    required = minimum + conservation + countercyclical + dsib
    return {"required": required, "surplus": cet1_ratio - required, "compliant": cet1_ratio >= required}


if __name__ == "__main__":
    rwa = rwa_from_exposures([(1_000_000_000, 0.0), (500_000_000, 0.20), (2_000_000_000, 1.00)])
    assert rwa == 2_100_000_000
    cet1 = capital_ratio(252_000_000, rwa)
    assert abs(cet1 - 0.12) < 1e-12
    chk = buffer_check(cet1, countercyclical=0.01)
    assert abs(chk["required"] - 0.08) < 1e-12 and chk["compliant"]
    assert abs(leverage_ratio(252_000_000, 4_200_000_000) - 0.06) < 1e-12
    assert abs(lcr(330_000_000, 300_000_000) - 1.1) < 1e-12
    assert nsfr(1_050_000_000, 1_000_000_000) > 1.0
    print(f"CET1 {cet1:.1%} vs req {chk['required']:.1%} | LCR 110% | OK")
