# Working Capital Metrics Cookbook

## Countback DSO (use when sales are seasonal — always, really)
Walk backwards through monthly sales until AR is exhausted:
AR = 950; sales: Mar 400, Feb 380, Jan 350.
- Mar covers 400 (31 days), remaining 550; Feb covers 380 (28 days), remaining 170; Jan: 170/350 × 31 = 15 days.
- **Countback DSO = 31 + 28 + 15 = 74 days.** Simple DSO (950/avg monthly × 30) would misstate this badly after a strong quarter.

## Aging Migration Matrix
Track each bucket's flow month-over-month:
| From \ To | Current | 1–30 | 31–60 | 61–90 | 90+ | Collected |
|---|---|---|---|---|---|---|
| Current | — | 22% | — | — | — | 78% |
| 1–30 | — | — | 35% | — | — | 65% |
| 31–60 | — | — | — | 48% | — | 52% |
| 61–90 | — | — | — | — | 60% | 40% |
Roll rates rising = collections discipline slipping BEFORE headline DSO moves. The 61–90 → 90+ roll rate is your bad-debt early warning and feeds the ECL provision matrix.

## Early-Payment Discount APR Rule
"2/10 net 45": `APR = 0.02/0.98 × 365/35 = 21.3%`.
Take the discount if 21.3% > your marginal cost of funds; otherwise pay day 45. Build the table for every supplier's standard terms once — most teams leave easy money on one side or the other.

## Peak vs. Average Working Capital
Month-end WC understates the intra-month peak (payroll dates, VAT/tax payment days, inventory builds before sales spikes). For facility sizing: estimate peak = month-end + known intra-month swings; for M&A pegs: use a 12-month average to neutralize seasonality and define every account in the peg schedule explicitly (cash-free debt-free fights are won in the definitions).

## Growth's WC Tax
`ΔWC ≈ (CCC/365) × Δrevenue` (revenue-margin adjusted). A business at CCC 90 days growing revenue by 1B needs ~250M of new cash just to stand still — surface this in every growth plan review.

## Quarter-End Window Dressing Tells
DPO spikes every quarter-end then normalizes; receivables factored in the last week; inventory cut by delaying receipts. Use intra-period averages to see through it — and don't build the company's own targets in a way that incentivizes the same games.
