# Actuarial Reserving Methods

## Chain Ladder (development triangle)
1. Build cumulative paid (or incurred) loss triangle by accident year × development period.
2. Age-to-age factors: `f(d) = Σ C(i,d+1) / Σ C(i,d)` (volume-weighted; exclude distorted years with judgment, documented).
3. Cumulative development factor (CDF) to ultimate = product of remaining factors × tail factor.
4. `Ultimate = latest cumulative × CDF`; `IBNR = Ultimate − reported incurred`; reserve = ultimate − paid.
Weakness: leveraged by latest diagonal — bad for immature/volatile years.

## Bornhuetter-Ferguson (the stabilizer)
`Ultimate = Reported + Expected ultimate × (1 − 1/CDF)`
Blends an a priori loss ratio (pricing or historical, adjusted) with actual emergence. Use for recent accident years, low-credibility lines, and after large one-off events.

## Expected Loss Ratio Method
`Ultimate = Premium × a priori loss ratio` — for brand-new lines with no credible development data.

## Frequency-Severity & Cape Cod
- Freq-sev: project claim counts and average severities separately — better insight into drivers (inflation vs. claim volume).
- Cape Cod: like BF but derives the a priori loss ratio from the data itself, weighted by used-up premium.

## Method Selection Matrix
| Accident year maturity | Preferred |
|---|---|
| Mature (CDF < 1.1) | Chain ladder |
| Mid (CDF 1.1–2.0) | Weighted CL/BF |
| Green (CDF > 2.0) | BF or ELR |

## Diagnostics Before Signing Off
- Calendar-year diagonals for inflation/process change distortions.
- Paid vs. incurred method divergence — investigate case reserve adequacy drift.
- Actual vs. expected emergence since last review.
- Tail factor sensitivity (long-tail liability: ±0.02 on tail swings reserves materially).
- IFRS 17: add risk adjustment + discounting (locked-in vs. current rates per measurement model); reserve ranges, not points.
