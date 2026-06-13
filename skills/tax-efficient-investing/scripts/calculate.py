"""Tax-efficient investing: tax drag, after-tax FV, tax-equivalent yield, Roth vs. traditional."""
from __future__ import annotations


def after_tax_future_value(
    principal: float,
    gross_annual_rate: float,
    annual_tax_rate: float,
    years: int,
) -> float:
    """FV of a lump sum in a taxable account where gains are taxed annually."""
    after_tax_rate = gross_annual_rate * (1 - annual_tax_rate)
    return round(principal * (1 + after_tax_rate) ** years, 2)


def tax_free_future_value(
    principal: float,
    gross_annual_rate: float,
    years: int,
) -> float:
    """FV of a lump sum in a tax-advantaged account (Roth / ISA) — no annual tax drag."""
    return round(principal * (1 + gross_annual_rate) ** years, 2)


def tax_drag_cost(
    principal: float,
    gross_annual_rate: float,
    annual_tax_rate: float,
    years: int,
) -> dict[str, float]:
    taxable_fv = after_tax_future_value(principal, gross_annual_rate, annual_tax_rate, years)
    tax_free_fv = tax_free_future_value(principal, gross_annual_rate, years)
    cost = round(tax_free_fv - taxable_fv, 2)
    pct_cost = round(cost / tax_free_fv, 4)
    return {
        "tax_free_fv": tax_free_fv,
        "taxable_fv": taxable_fv,
        "tax_drag_cost": cost,
        "tax_drag_pct": pct_cost,
    }


def tax_equivalent_yield(tax_free_yield: float, marginal_tax_rate: float) -> float:
    """Gross yield a taxable bond must offer to match a tax-free bond."""
    if marginal_tax_rate >= 1.0:
        raise ValueError("marginal_tax_rate must be < 1.0")
    return round(tax_free_yield / (1 - marginal_tax_rate), 4)


def roth_vs_traditional(
    contribution: float,
    years: int,
    gross_annual_rate: float,
    current_tax_rate: float,
    future_tax_rate: float,
) -> dict[str, float]:
    """
    Compare after-tax wealth from Roth vs. traditional contribution.
    Roth: contribute post-tax dollars, withdraw tax-free.
    Traditional: contribute pre-tax dollars, pay tax on withdrawal.
    """
    fv = contribution * (1 + gross_annual_rate) ** years
    roth_after_tax = round(fv, 2)  # no tax on withdrawal
    trad_pre_tax_contribution = round(contribution / (1 - current_tax_rate), 2)
    trad_fv = trad_pre_tax_contribution * (1 + gross_annual_rate) ** years
    trad_after_tax = round(trad_fv * (1 - future_tax_rate), 2)
    return {
        "roth_after_tax_wealth": roth_after_tax,
        "traditional_after_tax_wealth": trad_after_tax,
        "roth_advantage": round(roth_after_tax - trad_after_tax, 2),
    }


if __name__ == "__main__":
    drag = tax_drag_cost(10_000, 0.07, 0.15, 25)
    assert drag["tax_free_fv"] > drag["taxable_fv"]
    assert abs(drag["tax_free_fv"] - 54_274) < 500, f"TF FV={drag['tax_free_fv']}"
    assert abs(drag["taxable_fv"] - 42_415) < 500, f"Taxable FV={drag['taxable_fv']}"

    tey = tax_equivalent_yield(0.04, 0.24)
    assert abs(tey - 0.04 / 0.76) < 1e-3  # tolerance for 4 d.p. rounding

    rv = roth_vs_traditional(6_000, 30, 0.07, 0.22, 0.22)
    # Same tax rate → traditional should match Roth (same after-tax outcome)
    assert abs(rv["roth_advantage"]) < 1.0, f"Same rate should be ~equal: {rv}"

    rv2 = roth_vs_traditional(6_000, 30, 0.07, 0.22, 0.32)
    assert rv2["roth_advantage"] > 0, "Roth wins when future rate is higher"

    print(
        f"Tax drag on $10k @ 7% for 25yr (15% tax): ${drag['tax_drag_cost']:,.2f} | "
        f"TEY at 24%: {tey:.2%} | OK"
    )
