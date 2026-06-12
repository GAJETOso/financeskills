# Beta Unlevering and Relevering

## Why
Observed (levered) betas embed each comparable's capital structure. To apply a peer's beta to a target, strip out the peer's leverage, average, then relever at the target's structure.

## Hamada Formulas (debt beta = 0, tax shield discounted at Rd)
- **Unlever**: `βu = βl / (1 + (1 - T) × D/E)`
- **Relever**: `βl = βu × (1 + (1 - T) × D/E_target)`

## Harris-Pringle (tax shield as risky as assets — common in continuous rebalancing)
- **Unlever**: `βu = βl / (1 + D/E)`
- Use when the firm maintains a constant leverage ratio rather than fixed debt.

## Procedure
1. Select 5–8 pure-play comparables.
2. Pull 2–5 year weekly/monthly regression betas.
3. Unlever each at its own D/E (market values) and marginal tax rate.
4. Take the median unlevered beta (median resists outliers better than mean).
5. Relever at the target's capital structure (target or industry-normal D/E for private firms).

## Sanity Checks
- Unlevered betas across true comparables should cluster (spread < ~0.3).
- Asset beta for stable utilities ≈ 0.3–0.5; tech ≈ 1.0–1.4; commodity E&P ≈ 0.9–1.3.
- If relevered beta > 2.5, re-examine D/E inputs — likely book values leaked in.
