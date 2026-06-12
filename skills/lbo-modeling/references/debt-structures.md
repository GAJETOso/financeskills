# LBO Debt Structures

## Typical Capital Stack (top = paid first)
| Tranche | Leverage | Pricing (indicative) | Features |
|---|---|---|---|
| Revolver | undrawn at close | SOFR + 200–350 | Liquidity backstop; springing covenant |
| Term Loan A | with TLB, 0.5–1.5x | SOFR + 250–350 | Bank-held, 5–10% annual amortization |
| Term Loan B | 3–4.5x cumulative | SOFR + 350–500, 0–0.5% floor | Institutional, 1% amort, covenant-lite common |
| Senior Notes / High Yield | +1–2x | Fixed 7–10% | No amort, call protection (NC-2/3) |
| Mezzanine / PIK | +0.5–1x | 11–14% cash+PIK | Warrants sometimes attached |
| Sponsor Equity | 40–60% of capital | — | Residual claim |

## Key Terms to Model
- **Amortization**: TLA meaningful; TLB 1%/yr; notes bullet.
- **Cash sweep / ECF sweep**: % of excess cash flow, often leverage-ratcheted.
- **PIK toggle**: interest accrues to principal — compounds against the exit equity.
- **Call protection**: HY non-call periods and premiums (e.g., 105/102.5/100) matter for refi scenarios.
- **Covenants**: maintenance (leverage, coverage — tested quarterly, TLA/revolver) vs. incurrence (HY). Model headroom ≥ 15–25% cushion to projections.
- **OID & financing fees**: amortize into interest expense (effective yield); add cash cost at close.

## Structuring Logic
More TLA/amortizing debt = faster deleveraging, better IRR from paydown but tighter covenants. More HY/PIK = flexibility, higher cost, returns lean on growth. Match amortization burden to FCF stability of the business.
