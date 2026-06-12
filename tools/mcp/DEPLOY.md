# Hosting the FinanceSkills MCP Endpoint

Once hosted, anyone adds FinanceSkills to Claude (web/desktop), ChatGPT, or any
remote-MCP client with just the URL: `https://your-host/mcp`.

## Any container host (Fly.io, Render, Railway, Cloud Run)
From the repo root:
```bash
docker build -f tools/mcp/Dockerfile -t financeskills-mcp .
docker run -p 8080:8080 financeskills-mcp
# e.g. fly launch / render.yaml / gcloud run deploy with this image
```

## Bare VM
```bash
git clone https://github.com/GAJETOso/financeskills && cd financeskills
PORT=8080 python3 tools/mcp/http_server.py
```

## Auth (optional)
Set `FINANCESKILLS_TOKEN=<secret>`; clients must send
`Authorization: Bearer <secret>`. Without it the endpoint is public read-only
(it only serves repo content and runs deterministic calculators - no secrets,
no writes, no caller code execution).

## Health check
`GET /healthz` returns `{"ok": true, "tools": N}`.
