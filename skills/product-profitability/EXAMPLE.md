# Worked Example - product-profitability

## Ask

> Our 'Premium' service has 80% gross margins but only 5% of our sales. Our 'Standard' service has 20% margins but 95% of sales. Should we shut down 'Standard'?

## What a correct response contains

Should perform a Contribution Margin analysis. Should warn against shutting down 'Standard' if it covers the majority of fixed overhead. Should discuss the impact of fixed cost re-allocation. Should provide a Product Profitability Dashboard.

## File-driven variant

With fixture(s) `evals/files/product_lines.csv`:

> Build a product P&L from the attached file (evals/files/product_lines.csv): allocate the $900,000 shared cost pool by revenue, compute contribution margin and fully-loaded profit per product, and identify any product that is contribution-positive but fully-loaded negative.

Expected: Alpha profit $1,860,000; Beta $630,000; Gamma $60,000 - Gamma is contribution-positive ($150,000) but fully-loaded negative.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
