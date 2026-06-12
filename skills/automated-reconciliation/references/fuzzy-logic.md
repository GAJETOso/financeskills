# Fuzzy Matching Logic for Reconciliations

## Matching Tiers (run in order, lock matched items after each pass)
1. **Exact**: amount + date + reference all equal.
2. **Tolerance**: amount within ±0.5% or fixed threshold (e.g., ₦100/$1 for bank fees), date within ±3 business days, reference exact.
3. **Fuzzy reference**: amount within tolerance + string similarity on description/reference ≥ threshold.
4. **One-to-many / many-to-many**: subset-sum matching (one GL entry vs. several bank lines, e.g., batched settlements). Cap combination size at 5 to control false positives.

## String Similarity Techniques
- **Normalize first**: uppercase, strip punctuation/whitespace, remove noise tokens ("PAYMENT", "TRF", "REF"), expand known abbreviations from a maintained alias table.
- **Levenshtein ratio**: good for typos; threshold ≥ 0.85.
- **Token-set ratio** (rapidfuzz): robust to word reordering ("ACME LTD INVOICE 123" vs "INV123 ACME LIMITED").
- **Vendor alias map**: persist confirmed matches into a lookup so the same counterparty never needs fuzzy matching twice.

## Python Sketch
```python
from rapidfuzz import fuzz
def is_match(a, b, amt_a, amt_b, tol=0.005):
    amt_ok = abs(amt_a - amt_b) <= tol * max(abs(amt_a), abs(amt_b))
    return amt_ok and fuzz.token_set_ratio(a, b) >= 85
```

## Guardrails
- Never auto-match across different currencies without FX conversion at transaction-date rate.
- Flag fuzzy matches ≥ materiality for human review; auto-clear only below threshold.
- Log match tier + score on every pairing — auditors will ask.
- False-positive monitoring: sample 25 auto-matches monthly; > 2 errors → raise thresholds.
