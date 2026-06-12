# Journal Entry Patterns Cookbook

All examples balance and state their reversal behavior.

## 1. AP Accrual (service received, no invoice)
Dr Professional Fees 5,000 / Cr Accrued Liabilities 5,000 — auto-reverse WD1 next period.

## 2. Payroll (gross-to-net)
Dr Salaries Expense 10,000; Dr Employer Pension Expense 1,000
Cr Net Pay Payable 7,800; Cr PAYE Payable 2,200; Cr Pension Payable (employee 8% + employer 10% on relevant emoluments under Nigerian PRA 2014, adjust per jurisdiction) 1,000

## 3. Prepaid Insurance (annual premium 12,000 paid 1 March)
At payment: Dr Prepaid Insurance 12,000 / Cr Cash 12,000
Monthly: Dr Insurance Expense 1,000 / Cr Prepaid Insurance 1,000

## 4. Depreciation (asset 60,000, 5-yr straight line, no residual)
Monthly: Dr Depreciation Expense 1,000 / Cr Accumulated Depreciation 1,000

## 5. Deferred Revenue Release (annual SaaS 24,000 billed upfront)
At billing: Dr AR 24,000 / Cr Deferred Revenue 24,000
Monthly: Dr Deferred Revenue 2,000 / Cr Revenue 2,000

## 6. Unbilled (Accrued) Revenue
Dr Contract Asset–Unbilled AR 8,000 / Cr Revenue 8,000; reclass to AR on invoicing.

## 7. Bad Debt / ECL Provision Top-Up
Dr Impairment Loss 3,500 / Cr Allowance for ECL 3,500. Write-off: Dr Allowance / Cr AR (P&L only if allowance insufficient).

## 8. FX Revaluation (USD payable, NGN books, rate moved against you)
Dr FX Loss 150,000 / Cr Accounts Payable 150,000 — monetary items at closing rate (IAS 21).

## 9. Inventory Adjustment After Count
Shortage: Dr Inventory Shrinkage Expense / Cr Inventory. NRV write-down: Dr COGS (or separate line) / Cr Inventory Allowance.

## 10. Accrued Interest on Borrowing
Dr Interest Expense (EIR basis) / Cr Accrued Interest Payable; payment clears the payable.

## 11. Lease (IFRS 16, monthly)
Dr Interest Expense X; Dr Lease Liability Y / Cr Cash (X+Y). Separately: Dr ROU Depreciation / Cr Accumulated Depreciation–ROU.

## 12. Correction (expense posted to wrong cost center, same P&L account)
Dr Expense (CC-200) / Cr Expense (CC-100) — memo references original JE number.

## 13. Reclass Short-Term Portion of Debt
Dr Long-Term Debt / Cr Current Portion of LTD — every close.

## 14. Bonus Accrual (estimated, year-to-date true-up method)
Dr Bonus Expense / Cr Accrued Bonus = (expected annual bonus × months elapsed/12) − accrued to date.

## 15. Dividend Declaration
Dr Retained Earnings / Cr Dividends Payable at declaration; payment clears the liability. (Withholding tax: Cr WHT Payable for the withheld portion at payment.)
