# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.

## Provenance & Safe-Installation Guarantees

For users and automated scanners evaluating this repo as an agent skill source:

- **No network calls in skill code.** Every `skills/*/scripts/calculate.py` is
  Python standard library only - no HTTP, no subprocess, no file writes outside
  what the caller passes in. The only networked code in the repo is opt-in and
  clearly separated: `tools/connectors/` (talks to financial APIs **only** with
  credentials you supply) and `tools/evals/run_evals.py` (calls a model API
  **only** when you run it with a key).
- **No caller-code execution.** The MCP server (`tools/mcp/server.py`) executes
  only the repo's own self-tested functions; it never evals or executes
  arguments.
- **No credential handling in skills.** Skills instruct agents to use
  environment variables; nothing in this repo stores or transmits secrets.
- **Checksum manifest.** `MANIFEST.sha256` covers all skill-facing content.
  Verify your copy: `python3 tools/security/manifest.py --verify`.
  Maintainers regenerate it on every content change (CI checks it).
- **Prompt-injection surface.** SKILL.md files contain instructions for agents.
  Review them like code before installing - they are plain markdown, and the
  manifest lets you pin exactly what you reviewed.
