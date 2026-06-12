# LBO Modeling Best Practices

## Model Architecture (order matters)
1. Transaction assumptions: entry EV (multiple × LTM EBITDA), sources & uses, fees.
2. Debt schedule with mandatory amortization + cash sweep.
3. Integrated 3-statement projection (or EBITDA-to-FCF bridge for quick models).
4. Exit: exit multiple × exit-year EBITDA → equity proceeds → IRR/MoM.
5. Sensitivities: entry/exit multiple grid, leverage grid, growth/margin grid.

## Sources & Uses Discipline
- Uses: equity purchase price + refinanced debt + transaction fees (2–3% of EV) + financing fees (2–3% of debt, capitalized and amortized).
- Sources: each debt tranche + sponsor equity + management rollover. Must balance to the dollar.
- Minimum cash to balance sheet — never fund the deal to zero cash.

## Cash Sweep Mechanics
`FCF available = EBITDA − cash interest − cash taxes − capex − ΔNWC − mandatory amort`
Sweep order: revolver first, then tranches by seniority (check covenants — some TLBs have 50%/25%/0% ECF sweep tiers by leverage).

## Returns Math
- `MoM = Exit equity / Entry equity`; `IRR = MoM^(1/years) − 1` for single-flow deals.
- Value creation bridge at exit: EBITDA growth + multiple expansion + debt paydown = total equity gain. Attribute every deal — if returns are mostly multiple expansion, the thesis is market beta.
- Target: 20–25% IRR / 2.0–3.0x MoM over 5 years.

## Sanity Checks
- Leverage: 4–6x total debt/EBITDA typical; interest coverage (EBITDA/cash interest) ≥ 2x in all projection years.
- Credit stats improve over hold or the model has a problem.
- Circularity (interest ↔ cash) — use opening-balance interest convention or iterative solve; document which.
