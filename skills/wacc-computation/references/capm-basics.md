# CAPM Basics

## The Model
`Re = Rf + β × ERP (+ size premium + country risk premium, if applicable)`

- **Rf (Risk-Free Rate)**: Yield on default-free government bonds matching the cash flow horizon. Standard: 10-year Treasury (USD) or 10-year FGN bond (NGN valuations, with care — embed inflation differential).
- **β (Beta)**: Sensitivity of the stock's returns to market returns. β > 1 = more volatile than market.
- **ERP (Equity Risk Premium)**: Expected market return minus Rf. Common practice: 4.5%–6.0% mature-market ERP (Damodaran's updates are the standard citation).

## Adjustments
- **Size premium**: Add 1%–3% for small caps (Duff & Phelps/Kroll size deciles).
- **Country risk premium (CRP)**: For emerging markets, add CRP = sovereign default spread × (σ_equity / σ_bond). Apply fully or scaled by the firm's revenue exposure (lambda approach).
- **Currency consistency**: Match Rf, ERP, and cash flow currency. Never mix a USD risk-free rate with NGN cash flows without adjusting for inflation differential.

## Common Errors
1. Using a short-term T-bill rate for long-horizon valuation.
2. Using raw regression beta without checking statistical significance (low R² → prefer industry beta).
3. Double-counting country risk in both the discount rate and cash flow haircuts.
4. Applying historical ERP over too short a window.

## When CAPM Breaks Down
- Private companies: no observable beta → unlever/relever industry comparables (see beta-math.md).
- Thinly traded stocks: betas are unreliable → use sector betas.
- Multi-business firms: compute divisional betas from pure-play comparables.
