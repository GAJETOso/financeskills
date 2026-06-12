# WACC Computation Memo

**Target:** {entity} | **Valuation date:** {date} | **Currency:** {ccy}

## Result
| Component | Value | Weight | Contribution |
|---|---|---|---|
| Cost of equity | {Re}% | {We}% | {x.xx}% |
| After-tax cost of debt | {Rd_at}% | {Wd}% | {x.xx}% |
| **WACC** | | | **{wacc}%** |

## Cost of Equity Build (CAPM)
| Input | Value | Source |
|---|---|---|
| Risk-free rate | | {govt benchmark, tenor} |
| Beta (relevered) | | {peer set, median unlevered x target D/E} |
| Equity risk premium | | |
| Country risk premium | | {if applicable} |
| Size premium | | {if applicable} |

## Beta Workpaper
| Peer | Levered beta | D/E | Tax | Unlevered beta |
|---|---|---|---|---|

Median unlevered: {x.xx} -> relevered at target D/E {x.xx}, tax {xx}%: **{x.xx}**

## Sensitivity
| WACC | ERP -1% | Base | ERP +1% |
|---|---|---|---|
| Beta -0.2 | | | |
| Base | | | |
| Beta +0.2 | | | |

## Consistency Checks
- [ ] Rate currency matches cash-flow currency
- [ ] Market-value weights (not book)
- [ ] Marginal (not historical) cost of debt; tax shield usable

---
*Computed with scripts/calculate.py. AI-prepared - review before use in a transaction.*
