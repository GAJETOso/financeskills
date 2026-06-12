# Credit Risk Modeling for ECL

## PD Modeling
- **Scorecard/logistic regression**: `PD = 1/(1+e^-(β0+βX))` on borrower financials + behavioral data. Standard for retail and SME books.
- **Rating-based**: Map internal/external ratings to PD via transition matrices; derive multi-year cumulative PDs from matrix powers (Markov assumption — validate it).
- **PIT conversion**: Vasicek single-factor: `PD_PIT = N[(N⁻¹(PD_TTC) + √ρ × Z)/√(1−ρ)]` where Z is the macro factor.

## LGD Modeling
- Workout LGD: discounted recoveries less costs / EAD. Segment by collateral type and seniority.
- Downturn LGD for stressed scenarios.
- Floors: regulatory floors may apply; never let modeled LGD go negative.

## EAD / CCF
- Term loans: amortization schedule.
- Revolvers: `EAD = Drawn + CCF × Undrawn`. Estimate CCF from defaulted-facility history (typical 40%–75%).

## Macro Scenario Integration
1. Select drivers with economic rationale (GDP growth, unemployment, oil price for energy books, FX for dollarized liabilities).
2. Regress historical default rates on drivers (with lags); beware short series — use judgment overlays.
3. Apply to base/up/down scenarios; weights typically 40–50/20–30/25–35.

## Validation Checklist
- Discriminatory power: AUC/Gini > 0.6 acceptable, > 0.7 good.
- Calibration: predicted vs. observed default rates by grade (binomial test).
- Stability: PSI < 0.1 stable, 0.1–0.25 monitor, > 0.25 rebuild.
- Sensitivity: ECL response to ±1σ macro moves should be monotonic and explainable.
