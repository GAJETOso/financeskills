# Worked Example - budget-forecast

## Ask

> We need a budget for 2025. Last year revenue was $10M with 15% growth. We want to double our marketing spend to $1M. Can you build a high-level roadmap?

## What a correct response contains

Should identify revenue drivers (base revenue + growth rate). Should calculate projected revenue ($11.5M). Should account for fixed vs variable costs. Should discuss the impact of doubling marketing spend on EBITDA. Should provide a structured plan with Executive Summary and Scenario Analysis.

## File-driven variant

With fixture(s) `evals/files/history_and_drivers.csv`:

> From the attached history and drivers (evals/files/history_and_drivers.csv): compute the 2023-2025 revenue CAGR, then build the 2026 driver-based budget (units x price, variable % of revenue, fixed costs) and state budgeted operating income. Sanity-check the implied 2026 growth against the historical CAGR.

Expected: CAGR 31.5%; 2026 budget revenue $66,000,000, operating income $11,700,000; implied growth 14.6% vs CAGR 31.5%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
