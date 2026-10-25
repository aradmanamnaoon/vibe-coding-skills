---
name: secret-leakage-detector
description: Detect likely credentials, private keys, tokens, and secret-bearing configuration before commit or publication. Use for security review, pre-push checks, or suspicious configuration changes.
---

# Purpose

Prevent accidental credential publication while keeping false positives reviewable.

# When to activate

Files, diffs, logs, or generated configuration may contain secrets.

# When not to activate

Only public test fixtures are present and a trusted scanner has already covered the exact diff.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Git diff or target paths
- Repository ignore rules
- Known test-secret conventions

# Workflow

1. Scan the changed files and relevant tracked configuration for high-signal credential patterns and private-key markers.
2. Review entropy-like findings in context; distinguish synthetic fixtures, public identifiers, and actual secrets.
3. Check environment/example files for secret values rather than variable names only.
4. Inspect staged/tracked files, not only the working tree, before publication.
5. For a real secret, stop publication, remove it from current files, and tell the user that rotation/revocation is required outside the repository.
6. Re-scan after remediation.
7. Report findings without printing full secret values.

# Relevant tools

Secret scanner if installed, version control, repository search; this skill includes a deterministic helper script.

## Deterministic helper

For a dependency-free first pass, run python scripts/scan_secrets.py <root>. It reports only file, line, and pattern type and deliberately does not print matched secret values.

# Safety restrictions

Never print, copy, validate by authenticating, or commit a suspected secret.

# Validation

- No unresolved high-confidence secret is present in files intended for commit/push.
- Reports redact secret values.
- A real exposed credential is treated as compromised rather than merely deleted.

# Expected output

- Redacted finding list
- Files/line locations
- Remediation status
- Rotation/revocation action needed

# Failure handling

If a value cannot be classified safely, report a redacted potential secret for human review rather than echoing it.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P013. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
