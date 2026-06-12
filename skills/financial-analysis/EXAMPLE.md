# Worked Example - financial-analysis

## Ask

> Can you analyze these Q3 financials? Revenue: $120M, COGS: $40M, OpEx: $30M, Net Income: $35M. Cash: $50M, Current Liabilities: $25M.

## What a correct response contains

Should perform data normalization and calculate key ratios. Should identify Gross Margin (66.7%), Operating Margin (41.7%), and Net Margin (29.2%). Should calculate Current Ratio (2.0) and assess liquidity. Should check for profitability health and solvency. Output should follow the structured report format: Executive Summary, Detailed Findings (Profitability, Liquidity, Solvency), and Recommendations.

## File-driven variant

With fixture(s) `evals/files/financial_statements.csv`:

> Using the attached two-year financial statements (evals/files/financial_statements.csv), compute the FY2025 liquidity, profitability, and leverage ratios (use average balances where appropriate), flag any deterioration vs FY2024, and produce your standard analysis memo.

Expected: Current ratio 2.00, quick ratio 1.27, net margin 8.6%, ROE (avg equity) 24.7%, DSO (avg AR) 60 days, D/E 0.84, revenue growth 20%. Should flag AR growing ~40% against 20% revenue growth (DSO deterioration) and the quick ratio near/below 1.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
