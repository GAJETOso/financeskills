"""Credit analysis: coverage and leverage ratios, covenant headroom."""
from __future__ import annotations


def interest_coverage(ebit: float, interest: float) -> float:
    return ebit / interest


def fixed_charge_coverage(ebitda: float, capex: float, fixed_charges: float) -> float:
    """(EBITDA - maintenance capex) / (interest + scheduled principal + leases)."""
    return (ebitda - capex) / fixed_charges


def net_leverage(total_debt: float, cash: float, ebitda: float) -> float:
    return (total_debt - cash) / ebitda


def dscr(cfads: float, debt_service: float) -> float:
    """Cash flow available for debt service / total debt service."""
    return cfads / debt_service


def covenant_headroom(actual: float, covenant: float, lower_is_better: bool = True) -> float:
    """Headroom as fraction of covenant level. Positive = compliant."""
    return (covenant - actual) / covenant if lower_is_better else (actual - covenant) / covenant


if __name__ == "__main__":
    assert interest_coverage(8_000_000, 2_000_000) == 4.0
    assert abs(fixed_charge_coverage(10_000_000, 2_000_000, 4_000_000) - 2.0) < 1e-12
    nl = net_leverage(45_000_000, 5_000_000, 12_500_000)
    assert abs(nl - 3.2) < 1e-12
    assert abs(dscr(6_600_000, 5_500_000) - 1.2) < 1e-12
    hr = covenant_headroom(3.2, 4.0)   # max leverage 4.0x, actual 3.2x
    assert abs(hr - 0.2) < 1e-12
    assert covenant_headroom(1.2, 1.25, lower_is_better=False) < 0  # DSCR breach
    print(f"net leverage {nl:.1f}x | headroom {hr:.0%} | OK")
