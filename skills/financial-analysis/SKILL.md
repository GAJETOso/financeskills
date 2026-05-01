# Skill: Financial Analysis

## When to use
Use this skill when you need to perform a deep dive into a company's financial performance based on their financial statements (10-K, 10-Q, or custom internal reports).

## Inputs
- **Primary**: Balance Sheet, Income Statement, Cash Flow Statement (PDF, CSV, or Text).
- **Secondary**: Market data (Stock Price, Beta), Industry Benchmarks.

## Steps
1.  **Data Extraction**: Extract key metrics (Revenue, COGS, OpEx, Net Income, Total Assets, Total Liabilities).
2.  **Ratio Calculation**:
    - Liquidity (Current Ratio, Quick Ratio)
    - Profitability (Gross Margin, Net Margin, ROE)
    - Leverage (Debt-to-Equity, Interest Coverage)
3.  **Trend Analysis**: Compare the last 3 periods to identify growth or contraction patterns.
4.  **Anomaly Detection**: Highlight any significant swings (>15%) that lack a clear explanation in the footnotes.
5.  **Synthesis**: Summarize the financial health of the entity.

## Output Format
```markdown
### Financial Health Report: [Company Name]
- **Period**: [Q/Year]
- **Key Findings**:
  1. [Finding 1]
  2. [Finding 2]

| Metric | Value | Trend |
|--------|-------|-------|
| Revenue| $X | Up/Down |
| Net Income | $Y | Up/Down |

**Analyst Note**: [Summary recommendation or concern]
```
