# IFRS 9 Expected Credit Loss: Standard Essentials

## The Three-Stage Model
| Stage | Trigger | ECL Horizon | Interest Revenue Basis |
|---|---|---|---|
| 1 | No significant increase in credit risk (SICR) since origination | 12-month ECL | Gross carrying amount |
| 2 | SICR (rebuttable: >30 days past due) | Lifetime ECL | Gross carrying amount |
| 3 | Credit-impaired (default; rebuttable: >90 DPD) | Lifetime ECL | Net (amortized cost) |

## SICR Indicators
Quantitative: PD doubling or breach of origination-PD threshold; 30+ DPD backstop. Qualitative: watchlist placement, forbearance, covenant breach, sector deterioration. Low-credit-risk exemption (investment grade) is optional, use sparingly.

## ECL Formula
`ECL = Σt [ PDt × LGDt × EADt × Dt ]` — probability-weighted across at least 2–3 macro scenarios (base/upside/downside) with scenario weights documented.

- **PD**: Point-in-time, forward-looking (adjust TTC ratings with macro overlays — GDP, oil price, unemployment, policy rate).
- **LGD**: 1 − recovery rate; collateral haircuts, time-to-recovery discounting at EIR.
- **EAD**: Amortization profile + CCF on undrawn commitments.
- **D**: Discount at original effective interest rate.

## Simplified Approach (Trade Receivables)
Lifetime ECL always; provision matrix by aging bucket with forward-looking adjustment. Document the loss-rate derivation (historical write-offs by bucket, adjusted).

## Governance
- Staging overrides require credit committee sign-off.
- Post-model adjustments (PMAs/overlays) documented with quantified rationale and release criteria.
- Back-test: actual defaults vs. predicted PDs annually.
