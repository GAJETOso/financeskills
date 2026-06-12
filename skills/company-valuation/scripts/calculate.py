"""DCF valuation: FCF discounting, Gordon and exit-multiple terminal value, EV to equity."""
from __future__ import annotations


def npv(rate: float, cashflows: list[float]) -> float:
    """NPV of cashflows starting at t=1."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows, 1))


def terminal_value_gordon(final_fcf: float, wacc: float, g: float) -> float:
    if g >= wacc:
        raise ValueError("growth must be below WACC")
    return final_fcf * (1 + g) / (wacc - g)


def terminal_value_exit_multiple(final_ebitda: float, multiple: float) -> float:
    return final_ebitda * multiple


def enterprise_value(fcfs: list[float], wacc: float, terminal_value: float) -> float:
    return npv(wacc, fcfs) + terminal_value / (1 + wacc) ** len(fcfs)


def equity_value(ev: float, net_debt: float, minority_interest: float = 0.0) -> float:
    return ev - net_debt - minority_interest


if __name__ == "__main__":
    fcfs = [100.0, 110.0, 121.0, 133.1, 146.41]
    tv = terminal_value_gordon(146.41, 0.10, 0.03)
    assert abs(tv - 146.41 * 1.03 / 0.07) < 0.01
    ev = enterprise_value(fcfs, 0.10, tv)
    assert abs(npv(0.10, [100]) - 90.909090) < 1e-4
    eq = equity_value(ev, 300.0)
    assert abs(ev - (npv(0.10, fcfs) + tv / 1.1 ** 5)) < 1e-9 and eq == ev - 300
    print(f"EV: {ev:,.1f} | equity: {eq:,.1f} | OK")
