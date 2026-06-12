"""Three-statement model: integrity checks and a minimal linked projection."""
from __future__ import annotations


def balance_check(total_assets: float, total_liabilities: float, total_equity: float,
                  tolerance: float = 0.01) -> bool:
    return abs(total_assets - (total_liabilities + total_equity)) <= tolerance


def cash_ties(bs_cash: float, cf_closing_cash: float, tolerance: float = 0.01) -> bool:
    return abs(bs_cash - cf_closing_cash) <= tolerance


def retained_earnings_rollforward(opening_re: float, net_income: float,
                                  dividends: float) -> float:
    return opening_re + net_income - dividends


def project_year(prior: dict, assump: dict) -> dict:
    """Minimal linked projection. prior: revenue, cash, ppe, debt, equity, retained_earnings.
    assump: growth, ebitda_margin, da_pct_rev, capex_pct_rev, interest_rate, tax_rate, payout."""
    rev = prior["revenue"] * (1 + assump["growth"])
    ebitda = rev * assump["ebitda_margin"]
    da = rev * assump["da_pct_rev"]
    ebit = ebitda - da
    interest = prior["debt"] * assump["interest_rate"]
    pretax = ebit - interest
    tax = pretax * assump["tax_rate"]
    ni = pretax - tax
    dividends = ni * assump["payout"]
    capex = rev * assump["capex_pct_rev"]
    cash = prior["cash"] + ni + da - capex - dividends      # no WC movement in mini-model
    ppe = prior["ppe"] + capex - da
    re = retained_earnings_rollforward(prior["retained_earnings"], ni, dividends)
    equity = prior["equity"] + ni - dividends
    return {"revenue": rev, "net_income": ni, "cash": cash, "ppe": ppe,
            "debt": prior["debt"], "equity": equity, "retained_earnings": re,
            "balanced": balance_check(cash + ppe, prior["debt"], equity)}


if __name__ == "__main__":
    prior = {"revenue": 100.0, "cash": 20.0, "ppe": 80.0, "debt": 40.0,
             "equity": 60.0, "retained_earnings": 30.0}
    assert balance_check(prior["cash"] + prior["ppe"], prior["debt"], prior["equity"])
    yr = project_year(prior, {"growth": 0.10, "ebitda_margin": 0.25, "da_pct_rev": 0.05,
                              "capex_pct_rev": 0.06, "interest_rate": 0.08,
                              "tax_rate": 0.30, "payout": 0.40})
    assert yr["balanced"], "model must balance after a projected year"
    assert abs(yr["revenue"] - 110.0) < 1e-9
    assert cash_ties(yr["cash"], yr["cash"])
    assert not balance_check(100, 50, 49.5)
    print(f"projected revenue {yr['revenue']:.1f} | NI {yr['net_income']:.2f} | balances | OK")
