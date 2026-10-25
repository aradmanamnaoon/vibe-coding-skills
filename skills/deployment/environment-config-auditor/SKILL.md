---
name: environment-config-auditor
description: Derive required configuration keys from code and manifests, detect missing/unused/misspelled variables, and verify fail-fast behavior. Use for environment-variable or deployment configuration changes.
---

# Purpose

Make configuration requirements explicit and testable without exposing secret values.

# When to activate

Code reads environment/configuration or deployment manifests change.

# When not to activate

No runtime configuration is used in the changed scope.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Code/config sources
- Example environment file
- Deployment manifest/config schema

# Workflow

1. Discover configuration reads from code and framework config, then normalize them into a required/optional key inventory.
2. Compare the inventory to example files, container/IaC manifests, CI variables by name, and documentation without printing secret values.
3. Find misspellings, stale/unused keys, duplicated aliases, insecure defaults, and keys whose absence fails late.
4. Centralize/validate configuration at startup when consistent with the architecture.
5. Use placeholders in example files; never real secrets.
6. Test missing required keys, valid minimal configuration, and malformed non-secret values.
7. Update documentation from the validated inventory.

# Relevant tools

Repository search, configuration schema, container/local startup; this library includes a key-discovery helper.

## Deterministic helper

For a dependency-free inventory of common Python/JavaScript environment-variable reads, run python scripts/discover_env_keys.py <root>. Dynamic key construction still requires manual inspection.

# Safety restrictions

Never print, commit, or validate secret values by sending them to an external service.

# Validation

- Every required key is documented by name/purpose and provided by deployment configuration where observable.
- Missing critical keys fail clearly before partial startup.
- No secret value is committed in examples/reports.

# Expected output

- Configuration key inventory
- Missing/unused conflicts
- Startup validation results
- External secret-store items by name only

# Failure handling

If deployed secret/config stores are inaccessible, compare names from manifests/docs and mark values/existence externally unverified.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P041. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
