# Changelog

## v1.0.1 (2026-06-12)
- feat: runnable eval harness (tools/evals/run_evals.py) with API/CLI backends, LLM-judge grading, and xlsx fixture rendering
- feat: file-based evals for ALL 43 skills (173 evals) with realistic fixtures (45 files incl. 4 .xlsx workbooks) and code-verified expected values
- feat: scripts/calculate.py with self-tests for 30 more skills (38/43 covered; remaining 5 judgment-only by design)
- feat: MCP server (tools/mcp/server.py) - 155 tools from the calculators + skill/standards/template readers; zero-dependency stdio, works with any MCP client
- feat: slash-command layer (commands/) - 8 workflow commands with argument handling
- feat: real validator (validate_skills.py) enforcing the Agent Skills spec end to end, incl. script self-tests and marketplace sync; wired into CI
- feat: eval baseline scaffold (tools/evals/BASELINE.md, make_baseline.py) + monthly/manual GitHub Action publishing the scorecard
- feat: output templates in assets/ for 6 skills; as_of dates + verification guardrails on all 203 standards summaries
- feat: live-data connectors (tools/connectors/ - Stripe, Plaid) with --mock mode; SECURITY.md provenance + MANIFEST.sha256
- fix: proper Claude Code plugin manifest; single canonical finance_helpers.py; no committed bytecode
- feat: slash commands for ALL 43 skills + /close-the-books orchestration (52 commands total)
- feat: hosted-MCP kit - streamable-HTTP server, Dockerfile, DEPLOY.md, optional bearer auth
- feat: pip/pipx packaging (pyproject.toml, financeskills-* CLI entry points)
- feat: ERP connectors - QuickBooks Online, Xero, and a locale-hardened generic csv_mapper
- feat: adversarial evals for 10 key skills (malformed data, multiple-IRR, book-value/flat-rate baits, oversold inventory, negative-amount JEs)
- feat: month-end-close multi-skill workflow; signed-release pipeline (checksums + GitHub build attestations)
- feat: parse_amount/parse_date locale-hardened helpers; llms.txt index; EXAMPLE.md in every skill
- fix: consolidated pre-release history into v1.0.0 so versioning is monotonic

## v1.0.0 (2026-04-20)
Initial public release:
- 43 finance skills across accounting operations, financial analysis, tax, audit/SOX, risk, treasury, and corporate finance
- AGENTS.md and CLAUDE.md interaction rules; all SKILL.md reference links resolving
- calculation scripts with self-tests for the first 8 computational skills
- evals (3 cases per skill) across the full catalog
- standards library (IFRS, IAS, US GAAP ASC, IPSAS, ISA, Basel, ESG and more)
- repository foundations, marketplace manifests, contributor docs
