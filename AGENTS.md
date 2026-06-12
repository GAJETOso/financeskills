# AGENTS.md - Instructions for AI Agents

Guidelines for AI agents working in this repository.

## Repository Overview

This repository contains **Agent Skills** for AI agents following the [Agent Skills specification](https://agentskills.io/specification.md). Skills install to `.agents/skills/` (the cross-agent standard). This repo also serves as a **Claude Code plugin marketplace** via `.claude-plugin/marketplace.json`.

- **Name**: Finance Skills
- **GitHub**: [GAJETOso/financeskills](https://github.com/GAJETOso/financeskills)
- **Creator**: KOMVIA
- **License**: MIT

## Repository Structure

```
financeskills/
├── .claude-plugin/
│   ├── plugin.json        # Claude Code plugin manifest
│   └── marketplace.json   # Claude Code plugin marketplace manifest
├── skills/                # Agent Skills
│   └── skill-name/
│       ├── SKILL.md       # Required skill file
│       └── evals/         # Required evaluation suite
├── tools/
│   ├── finance_helpers.py # Shared python utilities
│   └── REGISTRY.md        # Tool index with capabilities
├── foundations/           # Core technical guides
├── compliance/            # Regulatory mapping (IFRS/GAAP)
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Build / Lint / Test Commands

**Skills** are content-only (no build step). Verify manually:
- YAML frontmatter is valid
- `name` field matches directory name exactly
- `name` is 1-64 chars, lowercase alphanumeric and hyphens only
- `description` is 1-1024 characters

**Validation** - run before committing:
- `python3 validate_skills.py` - enforces this spec: frontmatter constraints, name-dir match, evals.json schema, fixture existence, dead-link detection, <500-line limit, script self-tests, marketplace sync, no compiled artifacts. (`./validate-skills.sh` wraps it.)

**Evals** (`skills/*/evals/evals.json`) are runnable benchmarks:
- `python3 tools/evals/run_evals.py --dry-run` - schema + fixture check (no model calls)
- `python3 tools/evals/run_evals.py --skill <name>` - run one skill's evals against a model (needs `ANTHROPIC_API_KEY`, or `--backend cli` for the Claude Code CLI)
- `python3 tools/evals/run_evals.py --all` - full regression run; reports land in `tools/evals/results/`
- Eval `files` entries are paths relative to the skill directory (fixtures live in `evals/files/`)

**Scripts** (`skills/*/scripts/calculate.py`): 38 of 43 skills ship deterministic calculators with self-tests. Always import these for computations instead of doing mental math - per CLAUDE.md, calculations must be verified with code. The 5 skills without scripts (audit-checklist, sox-compliance, close-management, esg-reporting, nlp-earnings-sentiment) are judgment-based by design.

**Standards summaries** (`standards/`) carry an `as_of` date and a verification footer. Treat them as orientation, not authority - verify against the issuing body's current text for decision-grade output.

## Agent Skills Specification

Skills follow the [Agent Skills spec](https://agentskills.io/specification.md).

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it. Include trigger phrases.
---
```

### Frontmatter Field Constraints

| Field         | Required | Constraints                                                      |
|---------------|----------|------------------------------------------------------------------|
| `name`        | Yes      | 1-64 chars, lowercase `a-z`, numbers, hyphens. Must match dir.   |
| `description` | Yes      | 1-1024 chars. Describe what it does and when to use it.          |
| `license`     | No       | License name (default: MIT)                                      |
| `metadata`    | No       | Key-value pairs (author, version, etc.)                          |

### Name Field Rules

- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- No consecutive hyphens (`--`)
- Must match parent directory name exactly

**Valid**: `tax-planning`, `financial-analysis`, `risk-assessment`
**Invalid**: `Tax-Planning`, `-tax`, `tax--planning`

### Optional Skill Directories

```
skills/skill-name/
├── SKILL.md        # Required - main instructions (<500 lines)
├── evals/          # Required - evaluation suite
│   ├── evals.json  # Prompts, expected outputs, assertions
│   └── files/      # Fixture data (CSVs etc.) referenced by evals
├── references/     # Optional - detailed docs loaded on demand
├── scripts/        # Optional - executable code (calculate.py with self-tests)
└── assets/         # Optional - output templates, data files
```

## Writing Style Guidelines

### Structure

- Keep `SKILL.md` under 500 lines (move details to `references/`)
- Use H2 (`##`) for main sections, H3 (`###`) for subsections
- Use bullet points and numbered lists liberally
- Short paragraphs (2-4 sentences max)

### Tone

- Direct and instructional
- Second person ("You are a senior financial analyst")
- Professional but approachable

### Formatting

- Bold (`**text**`) for key terms
- Code blocks for examples and templates
- Tables for reference data
- No excessive emojis

### Clarity Principles

- Clarity over cleverness
- Specific over vague
- Active voice over passive
- One idea per section

### Description Field Best Practices

The `description` is critical for skill discovery. Include:
1. What the skill does
2. When to use it (trigger phrases)
3. Related skills for scope boundaries

```yaml
description: When the user wants to analyze corporate financials. Use when the user says "financial analysis," "10-K review," "earnings audit." For risk assessments, see risk-assessment.
```

## Claude Code Plugin

This repo also serves as a plugin marketplace. The manifest at `.claude-plugin/marketplace.json` lists all skills for installation.


## Interfaces Beyond Skills

- **Slash commands**: `commands/*.md` - workflow entry points with `$ARGUMENTS`.
- **MCP server**: `python3 tools/mcp/server.py` - exposes every `calculate.py`
  function as `<skill>__<function>` tools plus `list_skills`/`get_skill`/
  `get_standard`/`get_template`. Stdlib-only.
- **Connectors**: `tools/connectors/` (Stripe, Plaid) - the only networked tool
  code, opt-in, env-var credentials, `--mock` for testing.
- **Provenance**: `python3 tools/security/manifest.py --verify` checks all
  content against MANIFEST.sha256. Regenerate (no --verify) after intentional
  edits; the validator warns when it is stale.

## Ethical Boundaries
- Do not provide financial advice.
- Always include a disclaimer that AI outputs should be reviewed by a human professional.
- Focus on automation and analysis, not speculation.

## Core Principles
- **Integrity**: Audit trails must be clear in every output.
- **Precision**: Round to appropriate decimal places for the currency being used.
- **Verification**: If a skill involves data extraction, verify the sources.

## Checking for Updates

When using any skill from this repository:

1. **Once per session**, on first skill use, check for updates:
   - Fetch `VERSIONS.md` from GitHub: https://raw.githubusercontent.com/GAJETOso/financeskills/main/VERSIONS.md
   - Compare versions against local skill files

2. **Non-blocking notification** at end of response:
   ```
   ---
   Skills update available: X finance skills have updates.
   Say "update skills" to update automatically, or run `git pull` in your financeskills folder.
   ```
