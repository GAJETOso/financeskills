"""Startup valuation: VC method, Berkus method, dilution math."""
from __future__ import annotations


def vc_method(exit_value: float, target_multiple: float, investment: float) -> dict:
    """Post-money = exit / target return multiple; ownership = investment / post-money."""
    post_money = exit_value / target_multiple
    ownership = investment / post_money
    return {"post_money": post_money, "pre_money": post_money - investment,
            "required_ownership": ownership}


def vc_method_irr(exit_value: float, years: int, required_irr: float, investment: float) -> dict:
    return vc_method(exit_value, (1 + required_irr) ** years, investment)


def berkus(sound_idea: float, prototype: float, team: float, relationships: float,
           rollout: float, cap_per_factor: float = 500_000) -> float:
    vals = [sound_idea, prototype, team, relationships, rollout]
    if any(v < 0 or v > cap_per_factor for v in vals):
        raise ValueError(f"each factor must be 0..{cap_per_factor}")
    return sum(vals)


def dilution(founder_pct: float, new_money: float, post_money: float) -> float:
    """Founder ownership after the round."""
    return founder_pct * (1 - new_money / post_money)


if __name__ == "__main__":
    v = vc_method(100_000_000, 10, 2_000_000)
    assert v["post_money"] == 10_000_000 and v["pre_money"] == 8_000_000
    assert abs(v["required_ownership"] - 0.20) < 1e-12
    vi = vc_method_irr(100_000_000, 5, 0.5849, 2_000_000)
    assert abs(vi["post_money"] - 100_000_000 / 1.5849 ** 5) < 1.0
    assert berkus(400_000, 500_000, 500_000, 300_000, 200_000) == 1_900_000
    assert abs(dilution(0.60, 2_000_000, 10_000_000) - 0.48) < 1e-12
    print(f"post-money {v['post_money']:,.0f} | founder after round 48% | OK")
