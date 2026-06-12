# Present Value Mathematics for Provisions

## Core Formulas
- Future cost with inflation: `FV = C0 × (1 + i)^n`
- Present value: `PV = FV / (1 + r)^n`
- Combined: `PV = C0 × ((1+i)/(1+r))^n ≈ C0 / (1 + real rate)^n` where `real ≈ (r − i)/(1 + i)` (Fisher).

## Accretion Schedule (example: PV = 1,000, r = 8%, n = 3)
| Year | Opening | Accretion 8% | Closing |
|---|---|---|---|
| 1 | 1,000.00 | 80.00 | 1,080.00 |
| 2 | 1,080.00 | 86.40 | 1,166.40 |
| 3 | 1,166.40 | 93.31 | 1,259.71 |
Closing equals the future settlement amount — always prove this tie-out.

## Revision Mechanics (IFRIC 1, cost model)
New PV computed with revised estimate/rate; Δ adjusts asset and liability:
`Dr/Cr Provision  ↔  Cr/Dr PP&E (ARO asset)` — then prospective depreciation over remaining life. If decrease exceeds asset carrying amount → excess to P&L.

## Multiple Cash Flow Timings
`PV = Σ CFt / (1+r)^t` — decommissioning often phases (wells P&A in year n, facilities n+2, monitoring n+2..n+10). Build per-component schedules, don't lump.

## Rate Selection Discipline
- Match rate currency to cash flow currency.
- Government bond yield of matching tenor is the usual IFRS proxy (risk-free, since cash flows already risk-adjusted).
- Probability-weight scenarios BEFORE discounting, not after.
- Sensitivity: report ±1% rate and ±10% cost impacts; long-dated AROs are violently rate-sensitive.
