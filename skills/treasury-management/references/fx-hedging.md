# FX Hedging for Treasury

## Exposure Taxonomy
- **Transaction**: booked receivables/payables in foreign currency — hedge mechanically.
- **Forecast**: probable future revenues/costs — hedge a declining ratio (e.g., 80% next quarter, 50% out 12 months).
- **Translation**: net investment in foreign subsidiaries — usually NOT hedged with cash instruments unless covenant/ratio-driven.
- **Economic/competitive**: pricing-power erosion — managed structurally (sourcing, pricing), not with derivatives.

## Instrument Selection
| Instrument | Use | Cost Profile |
|---|---|---|
| Forward/NDF | Firm exposures, illiquid currencies (NDF for NGN, partial convertibility) | Zero premium; locks rate (forward points = carry) |
| Vanilla option | Uncertain exposures (bids, forecasts) | Premium; keeps upside |
| Collar | Premium reduction | Caps both directions |
| Cross-currency swap | Debt in foreign currency | Converts principal + coupons |
| Natural hedge | Match currency of revenue and cost/debt | Free — exhaust first |

## High-Carry Currency Reality (NGN and peers)
Forward points on high-interest-differential currencies make systematic forward hedging expensive (you pay the carry). Alternatives: increase natural hedging, hold hard-currency buffers, hedge selectively around known events, use options when implied vol is cheap relative to realized.

## Hedge Accounting (IFRS 9)
- Cash flow hedge: effective portion → OCI, recycle when hedged item hits P&L. Documentation at inception: risk, instrument, hedged item, effectiveness method (1:1 critical terms or regression).
- Forward points/option time value: may be treated as cost of hedging (OCI amortization) — reduces P&L noise.
- Without hedge accounting, MTM volatility lands in P&L — decide deliberately.

## Policy Skeleton
Hedge ratios by horizon, approved instruments (no written naked options), counterparty limits by rating, mandatory competitive quotes (≥ 2), monthly effectiveness and exposure reporting to treasury committee.
