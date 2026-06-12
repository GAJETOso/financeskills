# Time-Series Forecasting for Cash Burn

## Method Ladder (use the simplest that fits)
1. **Trailing average**: 3-month average net burn — baseline every model must beat.
2. **Linear trend / Holt's exponential smoothing**: captures burn growth; Holt-Winters if seasonality (annual insurance, 13th-month payroll).
3. **Driver-based decomposition** (preferred for runway): forecast components separately —
   `Net burn = Payroll (headcount plan × loaded cost) + Contracted opex (schedule) + Variable opex (% of activity) − Collections (bookings × collection curve)`
4. **ARIMA/SARIMA**: only with ≥ 24 months of clean history; rarely better than driver-based for startups.
5. **Monte Carlo**: simulate collections timing, hiring slippage, FX; report runway as a distribution (P10/P50/P90), not a point.

## Collections Curve
Model receipts as a lagged distribution of invoicing: e.g., 20% month 0, 50% month 1, 25% month 2, 5% bad debt — fit from AR aging history. The curve, not revenue, drives cash.

## Runway Mathematics
- Simple: `Runway = Cash / trailing 3-mo net burn`.
- Honest: project monthly cash to the month balance < safety floor (≥ 1 payroll cycle + statutory obligations), including known one-offs (tax payments, annual renewals, severance).
- Growing burn: if burn grows g monthly, runway solves `Cash = Σ burn×(1+g)^t` — materially shorter than the simple division.

## Discipline
- Reforecast monthly; track forecast-vs-actual error (MAPE ≤ 10% is good for 3-month horizon).
- Separate committed vs. discretionary spend so scenario levers are real.
- Never net financing inflows into operating burn — report both.
