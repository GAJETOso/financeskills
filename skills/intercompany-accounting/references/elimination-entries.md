# Intercompany Elimination Entries (worked)

## 1. Balance Elimination
Parent due-from Sub 40M; Sub due-to Parent 40M:
`Dr IC Payable (Sub) 40M / Cr IC Receivable (Parent) 40M` — at consolidation level only; never touch entity books.
If they DON'T match, fix the entity books first. Eliminating a mismatch hides an error.

## 2. IC Sales and Unrealized Profit in Inventory
Sub sold goods to Parent for 30M (cost 22M); Parent resold 75%, holds 25%.
- Eliminate trading gross: `Dr IC Revenue 30M / Cr IC COGS 30M` (then true COGS adjustments)
- Unrealized profit = 25% × 8M = 2M: `Dr COGS 2M / Cr Inventory 2M`
- Deferred tax (buyer's rate 30%): `Dr DTA 0.6M / Cr Tax Expense 0.6M`
- NCI note: if the SELLER is a partly-owned sub (upstream), allocate the 2M elimination against NCI's profit share proportionately.

## 3. Fixed Asset Transfer With Gain
Sub sells machine to Parent: proceeds 15M, carrying 10M, remaining life 5 years, transfer at start of year.
- Eliminate gain: `Dr Gain on Disposal 5M / Cr PP&E 5M`
- Depreciation correction (parent depreciates 15M/5 = 3M; group basis 10M/5 = 2M): `Dr Accumulated Depreciation 1M / Cr Depreciation Expense 1M` — repeat annually until life ends.
- Deferred tax on the net 4M difference at buyer's rate.

## 4. IC Loan and Interest
Parent lends Sub $1M at 8%; half-year elapsed.
- Eliminate balance: `Dr Loan Payable 1M / Cr Loan Receivable 1M`
- Eliminate interest: `Dr Interest Income 40k / Cr Interest Expense 40k`
- WHT withheld by Sub on interest paid stays in the consolidated tax accounts (real cash to the tax authority).
- Check: both sides accrued? A common mismatch is lender accruing monthly, borrower booking on payment.

## 5. Management Fees / Royalties
`Dr Management Fee Income (Parent) / Cr Management Fee Expense (Sub)` — gross elimination. Verify the TP markup documentation BEFORE eliminating; elimination doesn't sanitize a non-arm's-length price for tax.

## 6. IC Dividend
Sub declares 20M dividend to Parent: `Dr Dividend Income (Parent) 20M / Cr Retained Earnings adjustment` at consolidation (the sub's RE reduction already flows through). NCI's share of the dividend is real cash out of the group — no elimination of the NCI portion.

## Settlement Netting Cycle (monthly)
Build the obligation matrix → net bilaterally (or multilaterally via a netting center) → single payment per pair → book settlements same day both sides → revalue residual FX stubs. Netting cuts wire costs and FX spread, and ages nothing.
