"""Claims reserving: chain-ladder development factors, ultimates, IBNR."""
from __future__ import annotations


def development_factors(triangle: list[list[float]]) -> list[float]:
    """Volume-weighted age-to-age factors from a cumulative paid/incurred triangle.
    triangle[i] = accident year i's cumulative values by development period."""
    n = len(triangle[0])
    factors = []
    for j in range(n - 1):
        num = sum(row[j + 1] for row in triangle if len(row) > j + 1)
        den = sum(row[j] for row in triangle if len(row) > j + 1)
        factors.append(num / den)
    return factors


def project_ultimates(triangle: list[list[float]], factors: list[float]) -> list[float]:
    ults = []
    for row in triangle:
        val = row[-1]
        for f in factors[len(row) - 1:]:
            val *= f
        ults.append(val)
    return ults


def ibnr(ultimates: list[float], paid_to_date: list[float]) -> float:
    return sum(u - p for u, p in zip(ultimates, paid_to_date))


if __name__ == "__main__":
    tri = [
        [1000.0, 1500.0, 1800.0],
        [1100.0, 1650.0],
        [1200.0],
    ]
    f = development_factors(tri)
    assert abs(f[0] - (1500 + 1650) / (1000 + 1100)) < 1e-12
    assert abs(f[1] - 1800 / 1500) < 1e-12
    ult = project_ultimates(tri, f)
    assert abs(ult[0] - 1800) < 1e-9                       # fully developed
    assert abs(ult[1] - 1650 * f[1]) < 1e-9
    assert abs(ult[2] - 1200 * f[0] * f[1]) < 1e-9
    res = ibnr(ult, [row[-1] for row in tri])
    assert res > 0
    print(f"LDFs {[round(x,3) for x in f]} | IBNR {res:,.0f} | OK")
