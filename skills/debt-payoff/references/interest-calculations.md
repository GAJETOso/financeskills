# Interest Calculation Reference

## Monthly Interest on a Declining Balance
`Monthly Interest = Outstanding Balance × (Annual Rate / 12)`

This is simple monthly compounding, used by most consumer loans and credit cards in the US.

## Daily Periodic Rate (Some Credit Cards)
`Daily Rate = Annual Rate / 365`
`Monthly Interest = Average Daily Balance × Daily Rate × Days in Month`

When a card uses average daily balance, paying early in the cycle reduces the interest charge.

## Amortisation
For instalment loans (car, mortgage, personal), each payment is split between interest and principal:
- `Interest Portion = Remaining Balance × Monthly Rate`
- `Principal Portion = Monthly Payment − Interest Portion`

The minimum payment on an amortising loan is set to pay off the loan in exactly N months. Extra payments reduce principal directly and shorten the loan.

## APR vs. APY
- **APR (Annual Percentage Rate)**: The stated rate; does not account for compounding within the year.
- **APY (Annual Percentage Yield)**: The effective rate after intra-year compounding.
- For monthly compounding: `APY = (1 + APR/12)^12 − 1`

## Practical Note
The simulations in `calculate.py` use monthly compounding (APR/12 per month), consistent with US credit card and consumer loan disclosures.
