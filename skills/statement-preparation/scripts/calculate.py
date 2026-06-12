"""Statement preparation: indirect-method cash flow from balance sheet deltas."""
from __future__ import annotations


def operating_cash_flow_indirect(net_income: float, depreciation: float,
                                 delta_receivables: float, delta_inventory: float,
                                 delta_payables: float, other_noncash: float = 0.0) -> float:
    """Deltas are (closing - opening). AR/inventory increases consume cash."""
    return (net_income + depreciation + other_noncash
            - delta_receivables - delta_inventory + delta_payables)


def investing_cash_flow(capex: float, disposal_proceeds: float = 0.0,
                        acquisitions: float = 0.0) -> float:
    return -capex + disposal_proceeds - acquisitions


def financing_cash_flow(debt_drawn: float, debt_repaid: float,
                        dividends_paid: float, equity_issued: float = 0.0) -> float:
    return debt_drawn - debt_repaid - dividends_paid + equity_issued


def cash_reconciliation(opening_cash: float, cfo: float, cfi: float, cff: float) -> float:
    return opening_cash + cfo + cfi + cff


if __name__ == "__main__":
    cfo = operating_cash_flow_indirect(
        net_income=4_928_000, depreciation=2_100_000,
        delta_receivables=11_050_000 - 7_900_000,
        delta_inventory=8_780_000 - 6_200_000,
        delta_payables=5_640_000 - 4_700_000,
    )
    assert cfo == 4_928_000 + 2_100_000 - 3_150_000 - 2_580_000 + 940_000 == 2_238_000
    cfi = investing_cash_flow(3_500_000, disposal_proceeds=400_000)
    assert cfi == -3_100_000
    cff = financing_cash_flow(2_000_000, 0, 438_000)
    assert cff == 1_562_000
    closing = cash_reconciliation(3_500_000, cfo, cfi, cff)
    assert closing == 4_200_000
    print(f"CFO {cfo:,.0f} | closing cash ties at {closing:,.0f} | OK")
