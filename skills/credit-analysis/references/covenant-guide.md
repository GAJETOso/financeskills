# Covenant Design Guide

## Covenant Taxonomy
- **Maintenance** (tested quarterly): leverage, coverage, DSCR, minimum net worth, minimum liquidity. Bank-market standard.
- **Incurrence** (tested on action): limits on additional debt, dividends/restricted payments, asset sales, liens, investments. Bond-market standard; covenant-lite loans import this style.
- **Information**: monthly/quarterly reporting, compliance certificates, budget delivery, auditor access.

## The Big Four Financial Covenants
| Covenant | Definition Discipline |
|---|---|
| Net leverage | Cap EBITDA addbacks (run-rate synergies ≤ 10–20% of EBITDA, time-boxed); define netted cash (exclude restricted) |
| Interest coverage | Cash interest, not effective-rate accounting interest; include capitalized interest |
| DSCR | Include scheduled amortization AND mandatory prepayments; exclude voluntary |
| Minimum liquidity | Committed undrawn counts only while conditions to draw are met |

## Headroom Setting
Set covenants off the BORROWER's base case with 20–25% EBITDA cushion at the tightest point, widening over time only with deleveraging. Headroom < 15% = expect waiver requests; > 40% = covenant is decoration. Model the cushion quarterly, not annually — seasonality breaches happen mid-year.

## Definitions Hygiene (where deals are won/lost)
1. "EBITDA" addbacks: exceptional items capped and itemized; pro-forma acquisitions limited to completed deals with diligence-quality numbers.
2. "Debt": include guarantees, leases (state convention), deferred consideration, factoring with recourse.
3. Equity cure: limit frequency (2–3 over life, not consecutive), cash must actually arrive, no over-cure gaming.
4. FX: covenant currency and testing-date rates specified; high-volatility currencies need average-rate testing or you covenant FX noise.

## Early Warning Stack (monitor between test dates)
Utilization creep on the revolver, aged payables stretching, management account delays, auditor change, key customer loss, covenant-adjacent metrics (e.g., 12.1x against a 12.5x cap two quarters running). A covenant breach is a LAGGING indicator — the file should show concern before the certificate does.
