"""Inventory costing: perpetual FIFO and weighted-average, periodic LIFO, LCNRV."""
from __future__ import annotations


def fifo_cogs(purchases: list[tuple[float, float]], units_sold: float) -> dict:
    """purchases: list of (units, unit_cost) in order. Returns COGS and ending value."""
    layers = [list(p) for p in purchases]
    cogs, remaining = 0.0, units_sold
    for layer in layers:
        take = min(layer[0], remaining)
        cogs += take * layer[1]
        layer[0] -= take
        remaining -= take
        if remaining <= 0:
            break
    if remaining > 1e-9:
        raise ValueError("sold more units than purchased")
    return {"cogs": cogs, "ending_inventory": sum(u * c for u, c in layers)}


def weighted_average_cogs(purchases: list[tuple[float, float]], units_sold: float) -> dict:
    units = sum(u for u, _ in purchases)
    cost = sum(u * c for u, c in purchases)
    avg = cost / units
    return {"cogs": units_sold * avg, "ending_inventory": (units - units_sold) * avg,
            "avg_cost": avg}


def lifo_cogs_periodic(purchases: list[tuple[float, float]], units_sold: float) -> dict:
    return fifo_cogs(list(reversed(purchases)), units_sold)


def lcnrv_writedown(cost: float, nrv: float) -> float:
    """IAS 2 lower of cost and NRV writedown (0 if NRV >= cost)."""
    return max(cost - nrv, 0.0)


if __name__ == "__main__":
    buys = [(100, 10.0), (100, 12.0), (100, 14.0)]
    f = fifo_cogs(buys, 150)
    assert f["cogs"] == 100 * 10 + 50 * 12 == 1600 and f["ending_inventory"] == 50 * 12 + 100 * 14
    w = weighted_average_cogs(buys, 150)
    assert abs(w["avg_cost"] - 12.0) < 1e-12 and abs(w["cogs"] - 1800) < 1e-9
    l = lifo_cogs_periodic(buys, 150)
    assert l["cogs"] == 100 * 14 + 50 * 12 == 2000
    assert lcnrv_writedown(1000, 900) == 100 and lcnrv_writedown(1000, 1100) == 0
    print(f"FIFO COGS: {f['cogs']:,.0f} | WAC: {w['cogs']:,.0f} | LIFO: {l['cogs']:,.0f} | OK")
