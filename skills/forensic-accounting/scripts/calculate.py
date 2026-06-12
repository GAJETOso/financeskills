"""Forensic analytics: Benford's law first-digit test with chi-square statistic."""
from __future__ import annotations
import math


BENFORD = {d: math.log10(1 + 1 / d) for d in range(1, 10)}
# chi-square critical value, 8 degrees of freedom, alpha = 0.05
CHI2_CRIT_8DF_05 = 15.507


def first_digit(value: float) -> int:
    s = f"{abs(value):.10e}"   # scientific notation guarantees first significant digit
    return int(s[0])


def benford_test(values: list[float]) -> dict:
    obs = {d: 0 for d in range(1, 10)}
    clean = [v for v in values if abs(v) >= 1e-9]
    for v in clean:
        obs[first_digit(v)] += 1
    n = len(clean)
    chi2 = sum((obs[d] - n * BENFORD[d]) ** 2 / (n * BENFORD[d]) for d in range(1, 10))
    return {"n": n, "observed": obs,
            "expected": {d: n * BENFORD[d] for d in range(1, 10)},
            "chi_square": chi2, "flag": chi2 > CHI2_CRIT_8DF_05}


def round_number_ratio(values: list[float], base: float = 1000.0) -> float:
    """Share of amounts that are exact multiples of `base` - a fraud tell."""
    clean = [v for v in values if abs(v) >= 1e-9]
    return sum(1 for v in clean if abs(v) % base < 1e-9) / len(clean)


if __name__ == "__main__":
    import random
    random.seed(7)
    benford_like = [10 ** random.uniform(0, 4) for _ in range(2000)]
    r = benford_test(benford_like)
    assert not r["flag"], f"natural data flagged (chi2={r['chi_square']:.1f})"
    fabricated = [random.uniform(40_000, 90_000) for _ in range(2000)]  # digits 4-8 only
    r2 = benford_test(fabricated)
    assert r2["flag"], "fabricated data not flagged"
    assert round_number_ratio([1000.0, 2500.0, 3000.0, 1234.5]) == 0.5
    print(f"natural chi2 {r['chi_square']:.1f} (pass) | fabricated chi2 {r2['chi_square']:.0f} (flag) | OK")
