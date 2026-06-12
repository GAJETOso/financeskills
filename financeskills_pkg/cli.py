"""Entry points for pipx/pip installs.

Resolution order for the FinanceSkills content directory:
1. $FINANCESKILLS_HOME if set
2. the repo this package was installed from (editable installs / clones)
3. ~/.financeskills/repo - auto-downloaded from GitHub on first run (asks first)
"""
from __future__ import annotations

import io
import os
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

TARBALL = "https://github.com/GAJETOso/financeskills/archive/refs/heads/main.tar.gz"


def repo_root() -> Path:
    env = os.environ.get("FINANCESKILLS_HOME")
    if env and (Path(env) / "skills").exists():
        return Path(env)
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "skills").exists() and (parent / "AGENTS.md").exists():
            return parent
    cache = Path.home() / ".financeskills" / "repo"
    if (cache / "skills").exists():
        return cache
    print("FinanceSkills content not found locally.")
    ans = input(f"Download it from GitHub to {cache}? [y/N] ").strip().lower()
    if ans != "y":
        sys.exit("Aborted. Clone the repo and set FINANCESKILLS_HOME instead.")
    cache.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading...")
    with urllib.request.urlopen(TARBALL, timeout=120) as r:
        buf = io.BytesIO(r.read())
    with tarfile.open(fileobj=buf, mode="r:gz") as tf:
        top = tf.getmembers()[0].name.split("/")[0]
        tf.extractall(cache.parent, filter="data")
    (cache.parent / top).rename(cache)
    print(f"Installed content at {cache}")
    return cache


def _run(rel: str, *extra: str) -> None:
    root = repo_root()
    sys.exit(subprocess.run([sys.executable, str(root / rel), *extra,
                             *sys.argv[1:]]).returncode)


def mcp() -> None:
    _run("tools/mcp/server.py")


def mcp_http() -> None:
    _run("tools/mcp/http_server.py")


def validate() -> None:
    _run("validate_skills.py")


def evals() -> None:
    _run("tools/evals/run_evals.py")
