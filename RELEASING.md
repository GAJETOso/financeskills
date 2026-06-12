# Releasing

1. Update VERSIONS.md and version strings (pyproject.toml, .claude-plugin/plugin.json, both marketplace.json, tools/mcp/server.py).
2. `python3 tools/security/manifest.py && python3 validate_skills.py`
3. Commit, then tag: `git tag v1.0.2 && git push --tags`
4. The Release workflow validates, builds a checksummed tarball, attaches
   MANIFEST.sha256, and signs build provenance via GitHub attestations
   (verify with `gh attestation verify financeskills-v1.0.2.tar.gz -R GAJETOso/financeskills`).

Installers should pin a release tag, verify the sha256, and may verify the
attestation - never track `main` in production agents.
