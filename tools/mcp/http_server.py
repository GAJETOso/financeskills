#!/usr/bin/env python3
"""FinanceSkills MCP over Streamable HTTP - host it anywhere, add by URL.

Wraps the same handler as server.py (stdlib only). Clients POST JSON-RPC to
/mcp and receive JSON responses (stateless streamable-HTTP mode; no session
persistence is required for this server since it is read-only).

  python3 tools/mcp/http_server.py --port 8080
  curl -X POST localhost:8080/mcp -H 'Content-Type: application/json' \
       -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'

Deploy: see tools/mcp/DEPLOY.md (Dockerfile included).
Security: read-only repo content + deterministic calculators; no secrets;
set FINANCESKILLS_TOKEN to require a Bearer token.
"""
from __future__ import annotations

import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import server as core   # same directory


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: dict | None, extra: dict | None = None) -> None:
        data = json.dumps(body).encode() if body is not None else b""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, Mcp-Session-Id, MCP-Protocol-Version")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if data:
            self.wfile.write(data)

    def _authorized(self) -> bool:
        token = os.environ.get("FINANCESKILLS_TOKEN")
        if not token:
            return True
        return self.headers.get("Authorization", "") == f"Bearer {token}"

    def do_OPTIONS(self):  # CORS preflight
        self._send(204, None)

    def do_GET(self):
        if self.path in ("/", "/healthz"):
            self._send(200, {"ok": True, "server": "financeskills",
                             "tools": len(core.CALC) + len(core.META)})
        else:
            self._send(405, {"error": "POST JSON-RPC to /mcp"})

    def do_POST(self):
        if self.path.rstrip("/") not in ("/mcp", ""):
            return self._send(404, {"error": "use /mcp"})
        if not self._authorized():
            return self._send(401, {"error": "missing or invalid bearer token"})
        try:
            length = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(length))
        except (ValueError, json.JSONDecodeError):
            return self._send(400, {"jsonrpc": "2.0", "id": None,
                                    "error": {"code": -32700, "message": "parse error"}})
        if isinstance(req, list):   # batch
            resp = [r for r in (core.handle(x) for x in req) if r is not None]
            return self._send(200, resp if resp else None) if resp else self._send(202, None)
        resp = core.handle(req)
        if resp is None:            # notification
            return self._send(202, None)
        self._send(200, resp)

    def log_message(self, fmt, *args):  # quiet
        pass


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8080)))
    args = ap.parse_args()
    print(f"financeskills MCP on http://{args.host}:{args.port}/mcp "
          f"({len(core.CALC) + len(core.META)} tools)")
    ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
