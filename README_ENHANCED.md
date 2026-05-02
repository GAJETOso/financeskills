# Finance Skills for AI Agents

A comprehensive collection of AI agent skills for financial professionals, accountants, and finance teams. Built for technical finance professionals who want AI coding agents to help with financial analysis, auditing, compliance, reporting, and financial engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the [Agent Skills spec](https://agentskills.io).

Built by [Ayotunde Oso (aka GAJETOso)](https://github.com/GAJETOso) for accountants in oil & gas, banking, insurance, and corporate finance. Need specific help? Open an issue — this is a community-driven resource.

**Contributions welcome!** Found a way to improve a skill or have a new one to add? [Open a PR](#contributing).

Run into a problem or have a question? [Open an issue](https://github.com/GAJETOso/financeskills/issues) — we're happy to help.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific financial tasks. When you add these to your project, your agent can recognize when you're working on a financial task and apply the right accounting standards, compliance frameworks, and best practices.

## How Skills Work Together

Skills reference each other and build on shared financial context. Most skills check for foundational knowledge (accounting standards, regulatory requirements) before executing specialized tasks.

```
                            ┌──────────────────────────────────────┐
                            │      Compliance & Standards          │
                            │    (IFRS, GAAP, Local Regulations)   │
                            └──────────────┬───────────────────────┘
                                           │
    ┌──────────────┬────────────┬──────────┼──────────┬──────────────┬──────────────┐
    ▼              ▼            ▼          ▼          ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│ Financial│ │  Audit & │ │  Tax &   │ │ Risk │ │Corporate │ │  Industry   │ │ Advanced  │
│ Analysis │ │Compliance│ │Regulatory│ │      │ │ Finance  │ │  Specific   │ │ Analytics │
├──────────┤ ├──────────┤ ├──────────┤ ├──────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│fin-anlys │ │audit-chk │ │tax-plan  │ │risk  │ │corp-cons │ │oil-gas-val  │ │ai-anomaly │
│budget-fc │ │forensic  │ │revenue-  │ │treasury││lbo-model │ │insurance-res│ │nlp-sent   │
│statement │ │auto-recon│ │ recog    │ │      │ │startup-  │ │banking-comp │ │predictive │
│  -prep   │ │          │ │          │ │      │ │ valuation│ │crypto-acct  │ │           │
│invest-   │ │          │ │          │ │      │ │debt-restr│ │variance-ana │ │           │
│ analysis │ │          │ │          │ │      │ │wacc-comp │ │product-prof │ │           │
│          │ │          │ │          │ │      │ │ecl-comp  │ │earned-value │ │           │
│          │ │          │ │          │ │      │ │aro-comp  │ │             │ │           │
│          │ │          │ │          │ │      │ │esg-report│ │             │ │           │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └──┬───┘└────┬─────┘ └──────┬──────┘ └─────┬─────┘
     │            │            │           │         │              │              │
     └────────────┴─────┬──────┴───────────┴─────────┴──────────────┴──────────────┘
                        │
         Skills cross-reference:
           financial-analysis ↔ budget-forecast ↔ risk-assessment
           audit-checklist ↔ forensic-accounting ↔ ai-anomaly-detection
           statement-preparation ↔ corporate-consolidation ↔ revenue-recognition
           oil-gas-valuation ↔ aro-computation ↔ ecl-computation
```

## Available Skills

### Financial Analysis & Reporting

| Skill | Description |
| --- | --- |
| [financial-analysis](./skills/financial-analysis) | Comprehensive financial statement analysis using ratio analysis, trend analysis, and performance metrics... |
| [budget-forecast](./skills/budget-forecast) | Build budgets, forecasts, and variance analysis models with rolling forecasts and scenario planning... |
| [statement-preparation](./skills/statement-preparation) | Prepare financial statements (Income Statement, Balance Sheet, Cash Flow) following IFRS/GAAP standards... |
| [investment-analysis](./skills/investment-analysis) | Evaluate investment opportunities using NPV, IRR, payback period, and sensitivity analysis... |
| [product-profitability](./skills/product-profitability) | Analyze product-line profitability, contribution margins, and cost allocation for decision-making... |

### Audit & Compliance

| Skill | Description |
| --- | --- |
| [audit-checklist](./skills/audit-checklist) | Generate comprehensive audit checklists, working papers, and test procedures for internal/external audits... |
| [forensic-accounting](./skills/forensic-accounting) | Detect fraud, analyze suspicious transactions, and conduct forensic investigations with data analytics... |
| [automated-reconciliation](./skills/automated-reconciliation) | Automate bank reconciliations, intercompany eliminations, and account reconciliations at scale... |
| [ai-anomaly-detection](./skills/ai-anomaly-detection) | Use machine learning to detect unusual transactions, outliers, and potential fraud in financial data... |

### Tax & Regulatory

| Skill | Description |
| --- | --- |
| [tax-planning](./skills/tax-planning) | Optimize tax positions, plan tax strategies, and ensure compliance with local tax regulations... |
| [revenue-recognition](./skills/revenue-recognition) | Apply IFRS 15 / ASC 606 revenue recognition standards for contracts and performance obligations... |
| [esg-reporting](./skills/esg-reporting) | Prepare ESG (Environmental, Social, Governance) reports and sustainability disclosures... |
| [banking-compliance](./skills/banking-compliance) | Navigate Basel III, capital adequacy requirements, and banking regulatory compliance frameworks... |

### Risk & Treasury

| Skill | Description |
| --- | --- |
| [risk-assessment](./skills/risk-assessment) | Identify, quantify, and manage financial risks including credit, market, operational, and liquidity risks... |
| [treasury-management](./skills/treasury-management) | Optimize cash management, working capital, liquidity forecasting, and funding strategies... |
| [ecl-computation](./skills/ecl-computation) | Calculate Expected Credit Loss (ECL) under IFRS 9 for financial instruments and loan portfolios... |

### Corporate Finance

| Skill | Description |
| --- | --- |
| [corporate-consolidation](./skills/corporate-consolidation) | Prepare consolidated financial statements for group entities with elimination entries... |
| [lbo-modeling](./skills/lbo-modeling) | Build leveraged buyout (LBO) models with sources & uses, debt schedules, and returns analysis... |
| [startup-valuation](./skills/startup-valuation) | Value early-stage companies using DCF, comparables, venture capital method, and scorecard approaches... |
| [debt-restructuring](./skills/debt-restructuring) | Analyze debt restructuring scenarios, workout agreements, and distressed company turnarounds... |
| [wacc-computation](./skills/wacc-computation) | Calculate Weighted Average Cost of Capital (WACC) for valuation and capital budgeting decisions... |
| [venture-debt](./skills/venture-debt) | Analyze venture debt facilities, warrants, and alternative financing structures for startups... |
| [aro-computation](./skills/aro-computation) | Compute Asset Retirement Obligations (ARO) for decommissioning and environmental liabilities... |

### Industry-Specific

| Skill | Description |
| --- | --- |
| [oil-gas-valuation](./skills/oil-gas-valuation) | Value oil & gas reserves using NPV of future cash flows, reserve-based lending, and production forecasts... |
| [insurance-reserving](./skills/insurance-reserving) | Calculate insurance loss reserves, IBNR (Incurred But Not Reported), and actuarial estimates... |
| [crypto-accounting](./skills/crypto-accounting) | Account for cryptocurrency transactions, digital assets, NFTs, and DeFi protocols under emerging standards... |
| [variance-analysis](./skills/variance-analysis) | Analyze manufacturing cost variances (material, labor, overhead) for production cost control... |
| [earned-value-mgmt](./skills/earned-value-mgmt) | Track project financial performance using Earned Value Management (EVM) metrics and variance analysis... |

### Advanced Analytics

| Skill | Description |
| --- | --- |
| [nlp-earnings-sentiment](./skills/nlp-earnings-sentiment) | Extract sentiment and key insights from earnings calls, annual reports, and financial disclosures using NLP... |
| [predictive-burn-rate](./skills/predictive-burn-rate) | Forecast cash burn rates, runway, and funding requirements for startups and high-growth companies... |

## Installation

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install skills directly:

```bash
# Install all skills
npx skills add GAJETOso/financeskills

# Install specific skills
npx skills add GAJETOso/financeskills --skill financial-analysis audit-checklist

# List available skills
npx skills add GAJETOso/financeskills --list
```

This automatically installs to your `.agents/skills/` directory (and symlinks into `.claude/skills/` for Claude Code compatibility).

### Option 2: Claude Code Plugin

Install via Claude Code's built-in plugin system:

```bash
# Add the marketplace
/plugin marketplace add GAJETOso/financeskills

# Install all finance skills
/plugin install finance-skills
```

### Option 3: Clone and Copy

Clone the entire repo and copy the skills folder:

```bash
git clone https://github.com/GAJETOso/financeskills.git
cp -r financeskills/skills/* .agents/skills/
```

### Option 4: Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/GAJETOso/financeskills.git .agents/financeskills
```

Then reference skills from `.agents/financeskills/skills/`.

### Option 5: Fork and Customize

1. Fork this repository
2. Customize skills for your specific industry/regulatory needs
3. Clone your fork into your projects

### Option 6: SkillKit (Multi-Agent)

Use [SkillKit](https://github.com/rohitg00/skillkit) to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):

```bash
# Install all skills
npx skillkit install GAJETOso/financeskills

# Install specific skills
npx skillkit install GAJETOso/financeskills --skill financial-analysis audit-checklist

# List available skills
npx skillkit install GAJETOso/financeskills --list
```

## Usage

Once installed, just ask your agent to help with financial tasks:

```
"Analyze these financial statements and calculate key ratios"
→ Uses financial-analysis skill

"Prepare IFRS 15 revenue recognition journal entries for this contract"
→ Uses revenue-recognition skill

"Build a 5-year DCF model for this company"
→ Uses investment-analysis skill

"Calculate Expected Credit Loss for this loan portfolio"
→ Uses ecl-computation skill

"Prepare consolidated financial statements for our group"
→ Uses corporate-consolidation skill
```

You can also invoke skills directly:

```
/financial-analysis
/audit-checklist
/tax-planning
```

## Skill Categories

### 📊 Financial Analysis & Reporting
* `financial-analysis` - Ratio analysis, trend analysis, performance metrics
* `budget-forecast` - Budgeting, forecasting, variance analysis
* `statement-preparation` - Income Statement, Balance Sheet, Cash Flow
* `investment-analysis` - NPV, IRR, investment evaluation
* `product-profitability` - Product-line profitability analysis

### 🔍 Audit & Compliance
* `audit-checklist` - Audit procedures and working papers
* `forensic-accounting` - Fraud detection and investigation
* `automated-reconciliation` - Account reconciliation automation
* `ai-anomaly-detection` - ML-based anomaly detection

### 📋 Tax & Regulatory
* `tax-planning` - Tax optimization and compliance
* `revenue-recognition` - IFRS 15 / ASC 606 compliance
* `esg-reporting` - Sustainability and ESG disclosures
* `banking-compliance` - Basel III and banking regulations

### ⚠️ Risk & Treasury
* `risk-assessment` - Financial risk identification and management
* `treasury-management` - Cash and liquidity management
* `ecl-computation` - IFRS 9 Expected Credit Loss

### 🏢 Corporate Finance
* `corporate-consolidation` - Group consolidation
* `lbo-modeling` - Leveraged buyout models
* `startup-valuation` - Early-stage company valuation
* `debt-restructuring` - Workout and restructuring analysis
* `wacc-computation` - Cost of capital calculations
* `venture-debt` - Alternative financing structures
* `aro-computation` - Asset retirement obligations

### 🏭 Industry-Specific
* `oil-gas-valuation` - Reserve valuation for energy sector
* `insurance-reserving` - Insurance loss reserves and IBNR
* `crypto-accounting` - Digital asset accounting
* `variance-analysis` - Manufacturing cost variance analysis
* `earned-value-mgmt` - Project financial performance tracking

### 🤖 Advanced Analytics
* `nlp-earnings-sentiment` - NLP for financial documents
* `predictive-burn-rate` - Cash runway forecasting

## Compliance & Regulatory Support

This repository includes dedicated compliance mapping for:
* **IFRS Standards** - International Financial Reporting Standards
* **US GAAP** - Generally Accepted Accounting Principles
* **African Frameworks** - Local regulatory requirements (Nigeria, South Africa, Kenya, Ghana)
* **Industry Regulations** - Banking (Basel III), Insurance (IFRS 17), Oil & Gas (IFRS 6)

See [Regulatory Compliance Mapping](./compliance/REGULATORY_MAPPING.md) for detailed standard-to-skill mappings.

## Learning Path

### 🚀 Phase 1: Foundations
Get comfortable with the technical basics:
* **Python**: Master Pandas, NumPy, and OpenPyXL for data manipulation
* **APIs**: Connect to financial data sources (Yahoo Finance, Bloomberg, Alpha Vantage)
* **Git**: Version control for financial models and collaboration

📚 Resources in [`/foundations`](./foundations)

### 🚀 Phase 2: AI Usage
Learn to work effectively with AI agents:
* **Prompt Engineering**: Craft precise instructions for complex financial reasoning
* **AI Tools**: Leverage ChatGPT, Claude, GitHub Copilot, and Cursor for development

📚 Resources in [`/ai-usage`](./ai-usage)

### 🚀 Phase 3: Skill Building
Apply specialized financial skills:
* Start with foundational skills (financial-analysis, budget-forecast)
* Progress to compliance skills (audit-checklist, revenue-recognition)
* Master advanced topics (corporate-consolidation, predictive analytics)

📚 All skills available in [`/skills`](./skills)

### 🚀 Phase 4: Real Projects
Build end-to-end financial systems:
* **AI-powered Finance Assistant**: Natural language interface for financial queries
* **Automated Reporting Tool**: Dynamic generation of financial statements
* **Smart Audit System**: AI-driven anomaly detection in transaction logs

📚 Project templates in [`/projects`](./projects)

## Repository Structure

```
financeskills/
├── foundations/         # Phase 1: Python, APIs, Git basics
├── ai-usage/           # Phase 2: Prompt engineering guides
├── skills/             # Phase 3: Modular skill definitions
│   ├── financial-analysis/
│   │   ├── SKILL.md           # Skill instructions
│   │   ├── evals/             # Test cases
│   │   └── references/        # Accounting standards
│   ├── audit-checklist/
│   ├── tax-planning/
│   └── [30+ other skills]/
├── compliance/         # Regulatory mapping (IFRS, GAAP, local)
├── projects/          # Phase 4: Full-scale applications
└── tools/             # Helper utilities and integrations
```

## Contributing

Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding or improving skills.

### Skill Improvement Ideas
- Add more industry-specific skills (real estate, healthcare, manufacturing)
- Expand compliance coverage (SOX, GDPR, local African regulations)
- Create more advanced analytics skills (time series forecasting, Monte Carlo simulation)
- Build integration skills (QuickBooks, Xero, SAP, Oracle)

## For AI Agents

If you are an AI agent (Claude, Cursor, etc.), please refer to [AGENTS.md](./AGENTS.md) for interaction guidelines and [CLAUDE.md](./CLAUDE.md) for project rules.

## License

[MIT](./LICENSE) - Use these however you want.

## About the Author

Built by **Ayotunde Oso (aka GAJETOso)** — Accountant in the oil & gas industry (Nigeria), with experience across IFRS, corporate finance, audit, and financial systems. Currently building AI-powered finance tools for accounting professionals in emerging markets.

Connect: [GitHub](https://github.com/GAJETOso)

## Roadmap

### ✅ Completed
- [x] 30+ core financial skills
- [x] IFRS/GAAP compliance mapping
- [x] Industry-specific skills (oil & gas, banking, insurance)
- [x] AI agent integration (Claude Code, Cursor)

### 🚧 In Progress
- [ ] Interactive skill tutorials with Python notebooks
- [ ] Integration with accounting software APIs (QuickBooks, Xero)
- [ ] Video walkthroughs for each skill
- [ ] Mobile app for on-the-go financial analysis

### 🔮 Future
- [ ] Community skill marketplace
- [ ] Certification program for AI-powered accounting
- [ ] Multi-language support (French, Portuguese for African markets)
- [ ] Real-time collaboration features

## Support

Having issues? Questions? Want to contribute?

- 📧 **Issues**: [Open an issue](https://github.com/GAJETOso/financeskills/issues)
- 💬 **Discussions**: [Start a discussion](https://github.com/GAJETOso/financeskills/discussions)
- 🤝 **Contributing**: See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 🤖 For AI Agents
If you are an AI agent (Claude, Cursor, etc.), please refer to [AGENTS.md](./AGENTS.md) for interaction guidelines and [CLAUDE.md](./CLAUDE.md) for project rules.

---

**Built for accountants, by an accountant. Let's revolutionize financial analysis with AI.**
