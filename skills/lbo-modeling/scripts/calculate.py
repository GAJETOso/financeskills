"""LBO quick math: sources & uses, debt schedule with cash sweep, IRR/MoM."""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class LboAssumptions:
    entry_ebitda: float
    entry_multiple: float
    exit_multiple: float
    debt_pct: float                 # of entry EV
    interest_rate: float
    tax_rate: float
    years: int
    ebitda_growth: float
    fcf_conversion: float = 0.50    # FCF before debt service as % of EBITDA
    sweep_pct: float = 1.00


@dataclass
class LboResult:
    entry_ev: float
    entry_equity: float
    exit_ev: float
    exit_debt: float
    exit_equity: float
    mom: float
    irr: float
    debt_path: list[float] = field(default_factory=list)


def run_lbo(a: LboAssumptions) -> LboResult:
    entry_ev = a.entry_ebitda * a.entry_multiple
    debt = entry_ev * a.debt_pct
    equity = entry_ev - debt
    ebitda = a.entry_ebitda
    path = [debt]
    for _ in range(a.years):
        ebitda *= 1 + a.ebitda_growth
        interest = debt * a.interest_rate
        fcf = ebitda * a.fcf_conversion - interest * (1 - a.tax_rate)
        debt = max(0.0, debt - max(0.0, fcf) * a.sweep_pct)
        path.append(debt)
    exit_ev = ebitda * a.exit_multiple
    exit_equity = exit_ev - debt
    mom = exit_equity / equity if equity > 0 else float("nan")
    irr = mom ** (1 / a.years) - 1 if mom > 0 else float("nan")
    return LboResult(entry_ev, equity, exit_ev, debt, exit_equity, mom, irr, path)


if __name__ == "__main__":
    r = run_lbo(LboAssumptions(
        entry_ebitda=100, entry_multiple=8, exit_multiple=8,
        debt_pct=0.6, interest_rate=0.09, tax_rate=0.30,
        years=5, ebitda_growth=0.07))
    assert r.entry_ev == 800 and r.entry_equity == 320
    assert r.exit_equity > r.entry_equity and 0 < r.irr < 1
    print(f"MoM {r.mom:.2f}x | IRR {r.irr:.1%} | exit debt {r.exit_debt:,.0f}")
