#!/usr/bin/env python3
"""Generate or verify MANIFEST.sha256 - checksums of all skill-facing content.

Covers: skills/, standards/, commands/, tools/ (.py, .md, .json, .csv, .txt, .xlsx, .sh).
Lets installers and scanners verify the content they fetched matches what the
maintainer published.

  python3 tools/security/manifest.py            # (re)generate MANIFEST.sha256
  python3 tools/security/manifest.py --verify   # exit 1 on any mismatch
"""
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / "MANIFEST.sha256"
ROOTS = ["skills", "standards", "commands", "tools", "foundations", "compliance"]
EXTS = {".py", ".md", ".json", ".csv", ".txt", ".xlsx", ".sh", ".yml"}


def iter_files():
    for root in ROOTS:
        base = REPO / root
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.suffix in EXTS and "__pycache__" not in p.parts \
                    and "results" not in p.parts:
                yield p


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def generate() -> None:
    lines = [f"{digest(p)}  {p.relative_to(REPO).as_posix()}" for p in iter_files()]
    MANIFEST.write_text("\n".join(lines) + "\n")
    print(f"MANIFEST.sha256: {len(lines)} files")


def verify() -> None:
    if not MANIFEST.exists():
        sys.exit("MANIFEST.sha256 missing - run without --verify to generate")
    want = {}
    for line in MANIFEST.read_text().splitlines():
        h, _, rel = line.partition("  ")
        want[rel] = h
    have = {p.relative_to(REPO).as_posix(): digest(p) for p in iter_files()}
    bad = [r for r in want if want[r] != have.get(r)]
    new = [r for r in have if r not in want]
    for r in bad:
        print(f"  MISMATCH/MISSING: {r}")
    for r in new:
        print(f"  UNTRACKED: {r}")
    if bad or new:
        sys.exit(f"{len(bad)} mismatched, {len(new)} untracked. Regenerate if changes are intentional.")
    print(f"All {len(want)} files verified.")


if __name__ == "__main__":
    verify() if "--verify" in sys.argv else generate()
