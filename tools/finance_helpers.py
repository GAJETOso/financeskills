"""Shared finance helper functions (canonical copy - the only one in the repo)."""
from __future__ import annotations

import pandas as pd


def calculate_cagr(beginning_value: float, ending_value: float, years: float) -> float:
    """Calculates the Compound Annual Growth Rate."""
    if beginning_value <= 0 or years <= 0:
        return 0.0
    return (ending_value / beginning_value) ** (1 / years) - 1


def calculate_volatility(returns: pd.Series) -> float:
    """Standard deviation of a return series (sample basis)."""
    return float(returns.std())


def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Detect outliers in a dataframe column using 1.5x IQR fences."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return df[(df[column] < lower) | (df[column] > upper)]


def generate_simple_pnl(revenue: float, cogs: float, opex: float) -> dict[str, float]:
    """Build a simple P&L dict with gross and operating profit."""
    gross = revenue - cogs
    return {
        "revenue": revenue,
        "cogs": cogs,
        "gross_profit": gross,
        "opex": opex,
        "operating_profit": gross - opex,
    }

# --- locale-hardened parsing (use for ANY raw export before computing) ---
import datetime as _dt
import re as _re

_AMOUNT_JUNK = _re.compile(r"[^\d.,\-()]")


def parse_amount(raw: str | float | int) -> float:
    """Parse real-world export amounts: '\u20a61.234.567,89', '(1,234.50)',
    '$ 1,234.50-', '1 234,56'. Parentheses and trailing minus mean negative."""
    if isinstance(raw, (int, float)):
        return float(raw)
    s = _AMOUNT_JUNK.sub("", str(raw).strip().replace("\u00a0", "").replace(" ", ""))
    neg = "(" in s or s.endswith("-") or s.startswith("-")
    s = s.strip("()-")
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") \
            else s.replace(",", "")
    elif "," in s:
        frac = s.rsplit(",", 1)[1]
        s = s.replace(",", ".") if len(frac) in (1, 2) else s.replace(",", "")
    if not s:
        return 0.0
    return -float(s) if neg else float(s)


def parse_date(raw: str, dayfirst: bool = False) -> str:
    """Normalize 'DD/MM/YYYY', 'MM-DD-YYYY', 'YYYY.MM.DD' to ISO. Ambiguous
    day/month order must be declared via dayfirst - do not guess."""
    s = str(raw).strip()[:10].replace(".", "-").replace("/", "-")
    parts = s.split("-")
    if len(parts) != 3:
        raise ValueError(f"unrecognized date: {raw!r}")
    if len(parts[0]) == 4:
        y, m, d = parts
    elif dayfirst:
        d, m, y = parts
    else:
        m, d, y = parts
    return _dt.date(int(y), int(m), int(d)).isoformat()


def _parsing_selftest() -> None:
    assert parse_amount("\u20a61.234.567,89") == 1234567.89
    assert parse_amount("(1,234.50)") == -1234.50
    assert parse_amount("$ 1,234.50-") == -1234.50
    assert parse_amount("1 234,56") == 1234.56
    assert parse_amount(-42) == -42.0
    assert parse_date("31/05/2026", dayfirst=True) == "2026-05-31"
    assert parse_date("05/31/2026") == "2026-05-31"
    assert parse_date("2026.05.31") == "2026-05-31"


if __name__ == "__main__":
    _parsing_selftest()
    print("finance_helpers self-tests OK")
