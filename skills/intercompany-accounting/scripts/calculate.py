"""Intercompany: balance matching, elimination entries, unrealized profit in inventory."""
from __future__ import annotations


def match_balances(entity_a_books: dict[str, float], entity_b_books: dict[str, float],
                   tolerance: float = 0.01) -> dict:
    """Compare IC receivable on A vs IC payable on B per counterparty key."""
    diffs = {}
    for key in set(entity_a_books) | set(entity_b_books):
        a, b = entity_a_books.get(key, 0.0), entity_b_books.get(key, 0.0)
        if abs(a - b) > tolerance:
            diffs[key] = a - b
    return {"matched": not diffs, "differences": diffs}


def unrealized_profit_in_inventory(ic_sale_price: float, cost: float,
                                   pct_still_held: float) -> float:
    """Profit to eliminate on inventory still held within the group."""
    return (ic_sale_price - cost) * pct_still_held


def elimination_entry(ic_revenue: float, unrealized_profit: float) -> list[dict]:
    """Eliminate IC revenue/COGS and defer unrealized margin in inventory."""
    return [
        {"account": "IC Revenue", "dr": ic_revenue, "cr": 0.0},
        {"account": "IC COGS", "dr": 0.0, "cr": ic_revenue - unrealized_profit},
        {"account": "Inventory", "dr": 0.0, "cr": unrealized_profit},
    ]


if __name__ == "__main__":
    m = match_balances({"SubB": 500_000.0}, {"SubB": 480_000.0})
    assert not m["matched"] and abs(m["differences"]["SubB"] - 20_000) < 1e-9
    up = unrealized_profit_in_inventory(300_000, 200_000, 0.40)
    assert up == 40_000
    entry = elimination_entry(300_000, up)
    dr = sum(e["dr"] for e in entry); cr = sum(e["cr"] for e in entry)
    assert abs(dr - cr) < 1e-9, "elimination entry must balance"
    print(f"mismatch 20,000 | URP {up:,.0f} | entry balances | OK")
