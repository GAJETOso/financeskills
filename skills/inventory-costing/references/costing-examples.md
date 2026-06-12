# Inventory Costing Worked Examples

## 1. FIFO vs. Weighted Average (same data)
Purchases: 100 units @ 10; 100 @ 12; 100 @ 15. Sold: 220 units.
- **FIFO**: COGS = 100×10 + 100×12 + 20×15 = 2,500. Ending inventory = 80×15 = 1,200.
- **Periodic weighted avg**: avg = 3,700/300 = 12.333. COGS = 220 × 12.333 = 2,713. Ending = 80 × 12.333 = 987.
- Check: COGS + ending = 3,700 total cost in both methods. Always prove this identity.

## 2. Moving Average With Interleaved Sales
Start 100 @ 10 (avg 10). Sell 50 → COGS 500, remain 50 @ 10. Buy 100 @ 13 → avg = (500 + 1,300)/150 = 12.00. Sell 100 → COGS 1,200, remain 50 @ 12.
Moving average is path-dependent — recomputation must follow transaction order, which is why backdated transactions corrupt it.

## 3. Fixed Overhead Absorption at Normal Capacity
Budgeted FOH 1,200,000; normal capacity 100,000 units → rate 12/unit.
Actual production 80,000 units → absorbed 960,000; **240,000 unabsorbed → straight to COGS/P&L**, units still carry 12 each. Producing 130,000 units → rate drops to 1,200,000/130,000 = 9.23; never absorb more than actual FOH.

## 4. NRV Test
Finished good: cost 50; selling price 54; selling costs 6 → NRV 48 → **write down 2/unit**.
Raw material feeding it: cost 20, replacement 17. Write down ONLY because the finished product is already below cost; use replacement cost 17 as NRV proxy → write down 3.

## 5. Obsolescence Matrix (calibrate to actual outcomes)
| Last movement | Provision % |
|---|---|
| < 6 months | 0 |
| 6–12 months | 25 |
| 12–24 months | 50 |
| > 24 months | 100 |
Overrides: contracted future use → release; engineering change notices → 100% immediately regardless of age. Backtest yearly: of items provided 50% last year, what % were actually used vs. scrapped?

## 6. Goods in Transit Cut-Off
FOB shipping point, shipped Dec 28, received Jan 3 → BUYER's inventory at Dec 31 (and the payable). FOB destination → seller's until delivery. Match the freight terms report to the cut-off accrual every close.
