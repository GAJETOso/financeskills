# Worked Example - investment-analysis

## Ask

> Is Tesla a good buy at $170? Its P/E is 45 and revenue growth is slowing. Can you run a quick valuation?

## What a correct response contains

Should identify the need for a DCF or Multiples analysis. Should discuss the high P/E (45) relative to slowing revenue growth. Should identify key drivers for Tesla (Deliveries, FSD, Margins). Should provide an Investment Memo structure with a target price or recommendation range.

## File-driven variant

With fixture(s) `evals/files/project_cashflows.csv`:

> Evaluate the project in the attached cash-flow file (evals/files/project_cashflows.csv) at a 10% hurdle: NPV, IRR, payback period, and profitability index. Recommend accept/reject with reasoning.

Expected: NPV $267,946; IRR 21.9%; payback 2.5 years; PI 1.27. Accept (IRR > hurdle, NPV > 0).

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
