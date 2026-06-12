# Skill Categorization & Dependencies

Complete overview of all FinanceSkills organized by category, complexity, and interdependencies.

## Quick Reference Matrix

| Skill | Category | Complexity | Standards | Dependencies | Common Use Cases |
|-------|----------|------------|-----------|--------------|------------------|
| **Financial Analysis & Reporting** |
| [financial-analysis](./skills/financial-analysis) | Analysis | Beginner | IFRS, GAAP | None | Ratio analysis, trend analysis, performance evaluation |
| [budget-forecast](./skills/budget-forecast) | Planning | Beginner | General | financial-analysis | Annual budgets, rolling forecasts, variance analysis |
| [statement-preparation](./skills/statement-preparation) | Reporting | Intermediate | IFRS, GAAP | financial-analysis | Monthly/quarterly/annual financial statements |
| [investment-analysis](./skills/investment-analysis) | Valuation | Intermediate | General | financial-analysis, wacc-computation | Capital budgeting, project evaluation, M&A |
| [product-profitability](./skills/product-profitability) | Analysis | Intermediate | Management Accounting | financial-analysis, variance-analysis | Product line decisions, pricing strategy |
| **Audit & Compliance** |
| [audit-checklist](./skills/audit-checklist) | Compliance | Beginner | ISA, PCAOB | None | Internal audits, external audit prep, SOX compliance |
| [forensic-accounting](./skills/forensic-accounting) | Investigation | Advanced | General | audit-checklist, ai-anomaly-detection | Fraud detection, litigation support, investigations |
| [automated-reconciliation](./skills/automated-reconciliation) | Automation | Intermediate | General | None | Month-end close, bank recs, intercompany eliminations |
| [ai-anomaly-detection](./skills/ai-anomaly-detection) | Analytics | Advanced | General | financial-analysis | Continuous monitoring, fraud detection, outlier analysis |
| **Tax & Regulatory** |
| [tax-planning](./skills/tax-planning) | Compliance | Intermediate | Local Tax Laws | financial-analysis | Tax optimization, transfer pricing, deferred tax |
| [revenue-recognition](./skills/revenue-recognition) | Compliance | Advanced | IFRS 15, ASC 606 | statement-preparation | Contract accounting, performance obligations, SaaS revenue |
| [esg-reporting](./skills/esg-reporting) | Disclosure | Intermediate | GRI, SASB, TCFD | None | Sustainability reports, ESG ratings, stakeholder reporting |
| [banking-compliance](./skills/banking-compliance) | Compliance | Advanced | Basel III, IFRS 9 | risk-assessment, ecl-computation | Capital adequacy, stress testing, regulatory reporting |
| **Risk & Treasury** |
| [risk-assessment](./skills/risk-assessment) | Risk | Intermediate | COSO ERM, ISO 31000 | financial-analysis | Risk identification, heat maps, mitigation strategies |
| [treasury-management](./skills/treasury-management) | Treasury | Intermediate | General | financial-analysis | Cash forecasting, working capital, liquidity management |
| [ecl-computation](./skills/ecl-computation) | Compliance | Advanced | IFRS 9 | financial-analysis, risk-assessment | Loan loss provisioning, credit risk, impairment testing |
| **Corporate Finance** |
| [corporate-consolidation](./skills/corporate-consolidation) | Reporting | Advanced | IFRS 10, ASC 810 | statement-preparation | Group financial statements, business combinations |
| [lbo-modeling](./skills/lbo-modeling) | Valuation | Advanced | General | investment-analysis, wacc-computation | Private equity, leveraged transactions, returns analysis |
| [startup-valuation](./skills/startup-valuation) | Valuation | Intermediate | General | investment-analysis | VC/PE valuations, fundraising, 409A valuations |
| [debt-restructuring](./skills/debt-restructuring) | Advisory | Advanced | General | financial-analysis, investment-analysis | Workouts, turnarounds, distressed M&A |
| [wacc-computation](./skills/wacc-computation) | Valuation | Intermediate | General | financial-analysis | Cost of capital, hurdle rates, valuation inputs |
| [venture-debt](./skills/venture-debt) | Financing | Advanced | General | startup-valuation, debt-restructuring | Alternative financing, warrant analysis, covenant modeling |
| [aro-computation](./skills/aro-computation) | Compliance | Advanced | IAS 37, ASC 410 | financial-analysis | Decommissioning liabilities, environmental obligations |
| **Industry-Specific** |
| [oil-gas-valuation](./skills/oil-gas-valuation) | Valuation | Advanced | IFRS 6, SEC | investment-analysis, aro-computation | Reserve valuation, RBL, asset acquisitions |
| [insurance-reserving](./skills/insurance-reserving) | Actuarial | Advanced | IFRS 17, SAP | risk-assessment, ecl-computation | Loss reserves, IBNR, reserve adequacy testing |
| [crypto-accounting](./skills/crypto-accounting) | Compliance | Advanced | Emerging | financial-analysis | Digital asset accounting, DeFi, NFT valuation |
| [variance-analysis](./skills/variance-analysis) | Manufacturing | Intermediate | Management Accounting | budget-forecast | Cost control, production efficiency, overhead analysis |
| [earned-value-mgmt](./skills/earned-value-mgmt) | Project Finance | Intermediate | PMI EVM | budget-forecast, variance-analysis | Project cost control, schedule performance, forecasting |
| **Advanced Analytics** |
| [nlp-earnings-sentiment](./skills/nlp-earnings-sentiment) | Analytics | Advanced | General | financial-analysis | Earnings call analysis, disclosure mining, sentiment tracking |
| [predictive-burn-rate](./skills/predictive-burn-rate) | Forecasting | Advanced | General | budget-forecast, treasury-management | Runway analysis, funding requirements, scenario planning |

| **Accounting Operations** |
| [close-management](./skills/close-management) | Operations | Beginner | General | journal-entry, automated-reconciliation | Close calendars, task sequencing, fast close |
| [journal-entry](./skills/journal-entry) | Operations | Beginner | IFRS, GAAP | None | Accruals, prepaids, payroll, corrections |
| [fixed-asset-accounting](./skills/fixed-asset-accounting) | Operations | Intermediate | IAS 16, IAS 36, ASC 360 | journal-entry, aro-computation | Capitalization, depreciation, impairment, disposals |
| [inventory-costing](./skills/inventory-costing) | Operations | Intermediate | IAS 2, ASC 330 | variance-analysis | FIFO/weighted average, absorption, NRV write-downs |
| [intercompany-accounting](./skills/intercompany-accounting) | Operations | Intermediate | IFRS 10, TP rules | corporate-consolidation, automated-reconciliation | IC matching, eliminations, netting, TP entries |
| [lease-accounting](./skills/lease-accounting) | Compliance | Intermediate | IFRS 16, ASC 842 | journal-entry, deferred-tax | ROU assets, lease liabilities, modifications |
| [deferred-tax](./skills/deferred-tax) | Compliance | Advanced | IAS 12, ASC 740 | tax-planning, fixed-asset-accounting | Temporary differences, DTA recognition, ETR bridge |
| [sox-compliance](./skills/sox-compliance) | Compliance | Intermediate | SOX 404, PCAOB | audit-checklist, risk-assessment | Control testing, sampling, deficiency classification |
| **Financial Analysis (Extended)** |
| [company-valuation](./skills/company-valuation) | Valuation | Advanced | General | wacc-computation, financial-analysis | DCF, comps, precedent transactions, EV bridges |
| [credit-analysis](./skills/credit-analysis) | Analysis | Intermediate | General | financial-analysis, ecl-computation | Debt capacity, DSCR, covenant design |
| [working-capital-analysis](./skills/working-capital-analysis) | Analysis | Intermediate | General | treasury-management, financial-analysis | CCC, DSO/DIO/DPO, cash release programs |
| [three-statement-modeling](./skills/three-statement-modeling) | Analysis | Intermediate | General | budget-forecast, company-valuation | Integrated models, revolver plugs, balance checks |
| [cvp-breakeven](./skills/cvp-breakeven) | Analysis | Beginner | Management Accounting | product-profitability | Breakeven, contribution margin, special orders |

## Complexity Levels

### Beginner (10 skills)
**Time to proficiency**: 1-2 weeks  
**Prerequisites**: Basic accounting knowledge

- financial-analysis
- budget-forecast
- audit-checklist
- None required for these core skills

**Recommended learning order**:
1. financial-analysis → Learn ratio analysis and financial statement reading
2. budget-forecast → Apply analysis to planning and forecasting
3. audit-checklist → Understand control frameworks and testing

### Intermediate (20 skills)
**Time to proficiency**: 2-4 weeks  
**Prerequisites**: Beginner skills + industry experience

- statement-preparation
- investment-analysis
- product-profitability
- automated-reconciliation
- tax-planning
- esg-reporting
- risk-assessment
- treasury-management
- startup-valuation
- wacc-computation
- variance-analysis
- earned-value-mgmt

**Recommended learning order**:
1. statement-preparation → Master financial reporting
2. risk-assessment → Understand risk frameworks
3. treasury-management → Apply to cash management
4. Choose industry path (valuation, tax, manufacturing, etc.)

### Advanced (13 skills)
**Time to proficiency**: 4-8 weeks  
**Prerequisites**: Intermediate skills + specialized knowledge

- forensic-accounting
- ai-anomaly-detection
- revenue-recognition
- banking-compliance
- ecl-computation
- corporate-consolidation
- lbo-modeling
- debt-restructuring
- venture-debt
- aro-computation
- oil-gas-valuation
- insurance-reserving
- crypto-accounting
- nlp-earnings-sentiment
- predictive-burn-rate

**Recommended learning order**:
1. Master your industry-specific skills first
2. Add compliance/regulatory skills for your sector
3. Layer in advanced analytics capabilities

## Skill Dependencies Map

```
Core Foundation Skills (No Dependencies)
├── financial-analysis
├── audit-checklist
└── automated-reconciliation

Level 1: Built on Core Skills
├── budget-forecast [requires: financial-analysis]
├── statement-preparation [requires: financial-analysis]
├── risk-assessment [requires: financial-analysis]
├── treasury-management [requires: financial-analysis]
└── tax-planning [requires: financial-analysis]

Level 2: Specialized Applications
├── investment-analysis [requires: financial-analysis, wacc-computation]
├── wacc-computation [requires: financial-analysis]
├── product-profitability [requires: financial-analysis, variance-analysis]
├── variance-analysis [requires: budget-forecast]
├── earned-value-mgmt [requires: budget-forecast, variance-analysis]
└── esg-reporting [standalone]

Level 3: Advanced Compliance & Regulation
├── revenue-recognition [requires: statement-preparation]
├── corporate-consolidation [requires: statement-preparation]
├── ecl-computation [requires: financial-analysis, risk-assessment]
├── banking-compliance [requires: risk-assessment, ecl-computation]
└── aro-computation [requires: financial-analysis]

Level 4: Specialized Valuation & Modeling
├── startup-valuation [requires: investment-analysis]
├── lbo-modeling [requires: investment-analysis, wacc-computation]
├── debt-restructuring [requires: financial-analysis, investment-analysis]
├── venture-debt [requires: startup-valuation, debt-restructuring]
├── oil-gas-valuation [requires: investment-analysis, aro-computation]
└── insurance-reserving [requires: risk-assessment, ecl-computation]

Level 5: Emerging & Advanced Analytics
├── forensic-accounting [requires: audit-checklist, ai-anomaly-detection]
├── ai-anomaly-detection [requires: financial-analysis]
├── nlp-earnings-sentiment [requires: financial-analysis]
├── predictive-burn-rate [requires: budget-forecast, treasury-management]
└── crypto-accounting [requires: financial-analysis]
```

## Skills by Use Case

### Monthly Close & Reporting
1. automated-reconciliation → Reconcile accounts
2. statement-preparation → Prepare financials
3. variance-analysis → Analyze variances
4. financial-analysis → Calculate KPIs

### Audit Preparation
1. audit-checklist → Plan audit procedures
2. automated-reconciliation → Ensure accounts reconciled
3. forensic-accounting → Review unusual items
4. ai-anomaly-detection → Identify outliers

### Budgeting & Planning
1. budget-forecast → Build annual budget
2. financial-analysis → Analyze historical trends
3. variance-analysis → Compare actuals to budget
4. predictive-burn-rate → Forecast cash needs

### Investment Evaluation
1. financial-analysis → Analyze target company
2. wacc-computation → Determine discount rate
3. investment-analysis → Build DCF model
4. risk-assessment → Identify key risks

### M&A Transactions
1. financial-analysis → Due diligence
2. corporate-consolidation → Post-acquisition reporting
3. lbo-modeling → Financing structure (if leveraged)
4. debt-restructuring → If distressed

### Startup Finance
1. startup-valuation → Fundraising valuations
2. predictive-burn-rate → Runway planning
3. venture-debt → Alternative financing
4. revenue-recognition → SaaS revenue accounting

### Tax & Compliance
1. tax-planning → Optimize tax position
2. revenue-recognition → Revenue compliance
3. esg-reporting → Sustainability disclosures
4. banking-compliance → If regulated

### Industry-Specific Workflows

#### Oil & Gas
1. oil-gas-valuation → Reserve valuation
2. aro-computation → Decommissioning liabilities
3. financial-analysis → Performance metrics
4. esg-reporting → Environmental disclosures

#### Banking & Financial Institutions
1. banking-compliance → Regulatory compliance
2. ecl-computation → Loan loss provisioning
3. risk-assessment → Credit risk management
4. treasury-management → Liquidity management

#### Insurance
1. insurance-reserving → Loss reserves
2. risk-assessment → Underwriting risk
3. financial-analysis → Combined ratio analysis
4. banking-compliance → Solvency II (if applicable)

#### Manufacturing
1. variance-analysis → Production cost variance
2. product-profitability → Product line analysis
3. budget-forecast → Production planning
4. earned-value-mgmt → Project cost control

## Skills by Accounting Standard

### IFRS-Focused Skills
- statement-preparation (IAS 1)
- revenue-recognition (IFRS 15)
- ecl-computation (IFRS 9)
- corporate-consolidation (IFRS 10)
- banking-compliance (IFRS 9, 7)
- aro-computation (IAS 37, IFRS 16)
- oil-gas-valuation (IFRS 6)
- insurance-reserving (IFRS 17)
- esg-reporting (emerging IFRS Sustainability)

### US GAAP-Focused Skills
- statement-preparation (ASC 205-220)
- revenue-recognition (ASC 606)
- corporate-consolidation (ASC 810)
- aro-computation (ASC 410)

### Standards-Neutral Skills
- financial-analysis
- budget-forecast
- audit-checklist
- tax-planning
- risk-assessment
- treasury-management
- investment-analysis
- lbo-modeling
- startup-valuation
- All analytics skills

## Recommended Learning Paths

### Path 1: Corporate Accountant
**Goal**: Master financial reporting and compliance

1. **Month 1**: financial-analysis, budget-forecast
2. **Month 2**: statement-preparation, automated-reconciliation
3. **Month 3**: audit-checklist, revenue-recognition
4. **Month 4**: corporate-consolidation, tax-planning

### Path 2: Financial Analyst
**Goal**: Excel at analysis and valuation

1. **Month 1**: financial-analysis, budget-forecast
2. **Month 2**: investment-analysis, wacc-computation
3. **Month 3**: startup-valuation, risk-assessment
4. **Month 4**: lbo-modeling, debt-restructuring

### Path 3: Audit Professional
**Goal**: Master audit and forensic techniques

1. **Month 1**: audit-checklist, financial-analysis
2. **Month 2**: automated-reconciliation, risk-assessment
3. **Month 3**: forensic-accounting, ai-anomaly-detection
4. **Month 4**: Industry-specific compliance skill

### Path 4: Oil & Gas Specialist (Nigeria)
**Goal**: Master petroleum accounting

1. **Month 1**: financial-analysis, aro-computation
2. **Month 2**: oil-gas-valuation, investment-analysis
3. **Month 3**: revenue-recognition, tax-planning
4. **Month 4**: esg-reporting, risk-assessment

### Path 5: Startup CFO
**Goal**: Master startup finance

1. **Month 1**: financial-analysis, budget-forecast
2. **Month 2**: startup-valuation, predictive-burn-rate
3. **Month 3**: venture-debt, treasury-management
4. **Month 4**: revenue-recognition, tax-planning

### Path 6: Data-Driven Finance Professional
**Goal**: Master AI and analytics

1. **Month 1**: financial-analysis, automated-reconciliation
2. **Month 2**: ai-anomaly-detection, predictive-burn-rate
3. **Month 3**: nlp-earnings-sentiment, risk-assessment
4. **Month 4**: Industry-specific advanced skill

## Cross-Functional Skill Combinations

### Financial Planning & Analysis (FP&A)
- financial-analysis + budget-forecast + variance-analysis
- predictive-burn-rate + treasury-management
- product-profitability + investment-analysis

### Corporate Development
- investment-analysis + lbo-modeling + startup-valuation
- corporate-consolidation + debt-restructuring
- risk-assessment + financial-analysis

### Internal Audit
- audit-checklist + forensic-accounting + ai-anomaly-detection
- automated-reconciliation + risk-assessment
- financial-analysis + variance-analysis

### Treasury & Risk Management
- treasury-management + risk-assessment + ecl-computation
- predictive-burn-rate + budget-forecast
- banking-compliance (if in banking)

### Tax & Compliance
- tax-planning + revenue-recognition + esg-reporting
- banking-compliance (if regulated)
- Industry-specific compliance skill

## Skill Combinations for Common Projects

### IPO Readiness
1. statement-preparation → Clean financial statements
2. revenue-recognition → Ensure compliance
3. corporate-consolidation → Group reporting
4. audit-checklist → Internal controls
5. esg-reporting → ESG disclosures

### Fundraising (Equity)
1. financial-analysis → Historical performance
2. startup-valuation → Valuation analysis
3. budget-forecast → Projections
4. risk-assessment → Risk factors
5. revenue-recognition → Revenue model

### Debt Financing
1. financial-analysis → Credit metrics
2. budget-forecast → Repayment capacity
3. treasury-management → Liquidity analysis
4. risk-assessment → Covenant compliance
5. venture-debt (if startup)

### Digital Transformation
1. automated-reconciliation → Process automation
2. ai-anomaly-detection → Continuous monitoring
3. nlp-earnings-sentiment → Document analysis
4. predictive-burn-rate → Predictive analytics

## Next Steps

1. **Assess Your Level**: Review the complexity levels and identify where you are
2. **Choose Your Path**: Select a learning path aligned with your career goals
3. **Start Simple**: Begin with beginner skills even if you're experienced
4. **Build Systematically**: Follow dependency chains to build strong foundations
5. **Practice Daily**: Use skills in your actual work, not just study them

## Support

Questions about which skills to learn or in what order?

- 💬 [Ask in Discussions](https://github.com/GAJETOso/financeskills/discussions)
- 📧 [Open an Issue](https://github.com/GAJETOso/financeskills/issues)
- 📚 [Read the Full Documentation](./README.md)
