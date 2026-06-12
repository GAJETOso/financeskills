# Worked Example - risk-assessment

## Ask

> Our portfolio is 40% tech stocks and 60% crypto. What's the risk if the Fed raises interest rates?

## What a correct response contains

Should identify high interest rate sensitivity in tech and crypto. Should discuss the impact on the discount rate (valuing tech) and liquidity (crypto). Should suggest a VaR calculation or stress test. Should recommend diversification or hedging strategies.

## File-driven variant

With fixture(s) `evals/files/daily_returns.csv`:

> Portfolio value $10,000,000. From the attached daily return history (evals/files/daily_returns.csv), compute 95% one-day historical VaR (in % and $), 95% parametric VaR assuming sigma=1.2% and zero mean, and annualized volatility. Compare the two VaR estimates.

Expected: Historical VaR 1.94% ($194,370); parametric VaR $197,388; annualized vol 19.4%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
