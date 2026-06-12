"""Reconciliation matching engine: exact, tolerance, and subset-sum passes."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Txn:
    id: str
    amount: float
    ref: str = ""


def exact_match(side_a: list[Txn], side_b: list[Txn]) -> list[tuple[str, str]]:
    """Pair items with equal amount and reference. Each item used once."""
    used_b: set[str] = set()
    pairs = []
    for a in side_a:
        for b in side_b:
            if b.id in used_b:
                continue
            if a.amount == b.amount and a.ref == b.ref:
                pairs.append((a.id, b.id))
                used_b.add(b.id)
                break
    return pairs


def tolerance_match(side_a: list[Txn], side_b: list[Txn], tol: float) -> list[tuple[str, str, float]]:
    """Pair items whose amounts differ by <= tol; returns (a, b, difference)."""
    used_b: set[str] = set()
    pairs = []
    for a in side_a:
        best = None
        for b in side_b:
            if b.id in used_b:
                continue
            d = abs(a.amount - b.amount)
            if d <= tol and (best is None or d < best[1]):
                best = (b, d)
        if best:
            pairs.append((a.id, best[0].id, round(best[1], 2)))
            used_b.add(best[0].id)
    return pairs


def one_to_many_match(target: Txn, candidates: list[Txn],
                      tol: float = 0.01, max_combo: int = 4) -> list[str] | None:
    """Find a combination of candidates summing to the target amount (batched settlements)."""
    for r in range(2, max_combo + 1):
        for combo in combinations(candidates, r):
            if abs(sum(c.amount for c in combo) - target.amount) <= tol:
                return [c.id for c in combo]
    return None


if __name__ == "__main__":
    a = [Txn("a1", 100.0, "INV1"), Txn("a2", 250.0, "INV2")]
    b = [Txn("b1", 100.0, "INV1"), Txn("b2", 249.5, "INV2X")]
    assert exact_match(a, b) == [("a1", "b1")]
    assert tolerance_match([a[1]], [b[1]], tol=1.0) == [("a2", "b2", 0.5)]
    combo = one_to_many_match(Txn("t", 300.0), [Txn("c1", 120.0), Txn("c2", 180.0), Txn("c3", 50.0)])
    assert combo == ["c1", "c2"]
    print(f"exact: 1 pair | tolerance: 1 pair (diff 0.50) | subset-sum: {combo}")
