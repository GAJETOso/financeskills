import pandas as pd
import numpy as np

def calculate_cagr(beginning_value: float, ending_value: float, years: int) -> float:
    """Calculates the Compound Annual Growth Rate."""
    if years <= 0:
        return 0.0
    return (ending_value / beginning_value) ** (1 / years) - 1

def calculate_volatility(prices: pd.Series) -> float:
    """Calculates annualized volatility from a series of prices."""
    log_returns = np.log(prices / prices.shift(1))
    return log_returns.std() * np.sqrt(252)

def generate_simple_pnl(revenue: float, costs: float, tax_rate: float = 0.21) -> dict:
    """Generates a basic P&L dictionary."""
    ebitda = revenue - costs
    tax = max(0, ebitda * tax_rate)
    net_income = ebitda - tax
    return {
        "Revenue": revenue,
        "Costs": costs,
        "EBITDA": ebitda,
        "Tax": tax,
        "Net Income": net_income
    }
