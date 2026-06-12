# FinanceSkills MCP Server

A zero-dependency stdio MCP server that turns this repo into a **connector**:
155+ tools (every deterministic calculator across 38 skills) plus meta tools
for reading skill instructions, standards summaries, and output templates —
callable from any MCP client.

## Run
```bash
python3 tools/mcp/server.py
```
Requires Python 3.10+. No pip installs, no network access, no API keys.

## Configure

**Claude Code / Cowork** — add to `.mcp.json` in your project (or `claude mcp add`):
```json
{
  "mcpServers": {
    "financeskills": {
      "command": "python3",
      "args": ["/path/to/financeskills/tools/mcp/server.py"]
    }
  }
}
```

**Cursor** — `.cursor/mcp.json`, same shape. **Codex CLI** — `~/.codex/config.toml`:
```toml
[mcp_servers.financeskills]
command = "python3"
args = ["/path/to/financeskills/tools/mcp/server.py"]
```

## Tools

- `<skill>__<function>` — e.g. `lease_accounting__lease_liability`,
  `investment_analysis__irr`, `forensic_accounting__benford_test`,
  `banking_compliance__lcr`. Arguments mirror the Python signatures in
  `skills/*/scripts/calculate.py` (dataclass params are passed as JSON objects).
- `list_skills` / `get_skill` — discover and load full SKILL.md instructions.
- `list_standards` / `get_standard` — 203 standards summaries (IFRS, IAS, ASC,
  IPSAS, ISA, Basel, ESG). Each carries an `as_of` date; verify before
  decision-grade use.
- `get_template` — output templates (memos, workpapers) from skill assets.

## Security
Read-only against repo content; executes only the repo's own self-tested
calculators; no network calls; no execution of caller-supplied code.
