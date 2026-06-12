"""Consolidation: goodwill (full and partial method), NCI, IC elimination check."""
from __future__ import annotations


def goodwill_full(consideration: float, nci_fair_value: float,
                  net_identifiable_assets: float) -> float:
    """Full goodwill (IFRS 3 option / US GAAP requirement)."""
    return consideration + nci_fair_value - net_identifiable_assets


def goodwill_partial(consideration: float, pct_acquired: float,
                     net_identifiable_assets: float) -> float:
    """Partial goodwill: NCI measured at proportionate share of net assets."""
    return consideration - pct_acquired * net_identifiable_assets


def nci_at_acquisition(method: str, nci_fair_value: float, pct_nci: float,
                       net_identifiable_assets: float) -> float:
    if method == "full":
        return nci_fair_value
    return pct_nci * net_identifiable_assets


def nci_share_of_profit(subsidiary_profit: float, pct_nci: float,
                        urp_adjustments: float = 0.0) -> float:
    return (subsidiary_profit - urp_adjustments) * pct_nci


def consolidated_equity_check(parent_equity: float, sub_post_acq_profit: float,
                              pct_owned: float, goodwill_impairment: float = 0.0) -> float:
    """Group share of equity - quick reasonableness check."""
    return parent_equity + sub_post_acq_profit * pct_owned - goodwill_impairment


if __name__ == "__main__":
    gw_full = goodwill_full(8_000_000, 1_800_000, 7_500_000)
    assert gw_full == 2_300_000
    gw_part = goodwill_partial(8_000_000, 0.80, 7_500_000)
    assert gw_part == 2_000_000
    assert gw_full - gw_part == 1_800_000 - 0.20 * 7_500_000  # NCI premium
    assert nci_at_acquisition("partial", 1_800_000, 0.20, 7_500_000) == 1_500_000
    assert nci_share_of_profit(1_000_000, 0.20, urp_adjustments=50_000) == 190_000
    eq = consolidated_equity_check(20_000_000, 3_000_000, 0.80)
    assert eq == 22_400_000
    print(f"full GW {gw_full:,.0f} | partial GW {gw_part:,.0f} | NCI profit 190,000 | OK")
