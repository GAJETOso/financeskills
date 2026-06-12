# Model Integrity Checklist

## When the Balance Sheet Doesn't Balance — Debug Sequence
Work in this order; stop when the imbalance first appears.
1. **Find the first broken period.** The error is THERE, not where it's biggest (imbalances compound).
2. **Opening balance sheet**: does period 0 balance? If not, nothing downstream can.
3. **Retained earnings**: RE_close = RE_open + NI − dividends. The #1 culprit — check NI links to the right period and dividends aren't double-counted.
4. **Cash**: BS cash must equal CFS ending cash. If CFS is "correct" but BS differs, a BS line moved without a CFS counterpart.
5. **Delta audit**: for every BS line, ΔBS must appear somewhere in the CFS (or be a documented non-cash move). Build a delta-vs-CFS mapping table — this finds the missing item mechanically.
6. **Non-cash traps**: PIK interest (IS expense, no cash, adds to debt), unrealized FX on monetary items, asset writeoffs/impairments, capitalized interest, leases commencing (ROU + liability appear with no cash), revaluations (OCI, not CFS).
7. **Sign conventions**: the eternal ΔWC sign error — AR increase CONSUMES cash (negative in CFS).

## Circularity Management
Interest → cash → revolver → interest. Options:
- **Opening balance convention**: interest on opening debt/cash balances. Slight inaccuracy, total stability. Recommended default.
- **Average balance + iteration**: more precise; in Excel requires iterative calc (risk: silent convergence failures); in Python, loop until |Δinterest| < tolerance.
- Never mix conventions across tranches.

## Hardcode Hygiene
- Inputs only on the assumptions sheet.
- No constants inside formulas.
- Color convention if spreadsheet-based.
- In code: a single CONFIG dict/dataclass, statements as functions of it.

## Pre-Delivery Test Battery
1. Balance check = 0 every period.
2. CFS ending cash = BS cash every period.
3. Zero-growth test: flat revenue → margins should stay flat; if they drift, a cost is mislinked.
4. Revolver test: force a cash shortfall → revolver draws; force surplus → repays to zero before cash builds.
5. Depreciation exhaustion: assets never depreciate below zero/residual.
6. Ratio reasonableness vs. history: margins, days, capex/revenue, leverage.
7. Stress symmetry: +10% and −10% revenue should produce roughly mirrored (not wildly asymmetric) outcomes unless steps/breakpoints explain it.
