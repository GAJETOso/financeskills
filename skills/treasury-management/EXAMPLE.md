# Worked Example - treasury-management

## Ask

> We have $5M in cash but $2M is in Euros and the Euro is dropping. We also have a $1M payroll next week. What should we do?

## What a correct response contains

Should identify the immediate liquidity need (payroll) and the FX risk (Euro dropping). Should suggest a cash positioning review and potential FX hedging or conversion. Should provide a structured Treasury Report with a cash flow forecast and risk management recommendations.

## File-driven variant

With fixture(s) `evals/files/treasury_position.csv`:

> From the attached treasury position (evals/files/treasury_position.csv): compute liquidity runway in days, the 6-month NGN/USD forward rate under covered interest parity, and the NGN cost of hedging the $1,000,000 payable forward versus at spot.

Expected: Runway 80 days; 6m forward 1,624.39 NGN/USD; hedged cost NGN 1,624,390,244 vs spot 1,500,000,000 - forward premium 8.3%.

## Compute, don't estimate

All figures above come from [`scripts/calculate.py`](./scripts/calculate.py) - import its functions rather than doing arithmetic in prose.
