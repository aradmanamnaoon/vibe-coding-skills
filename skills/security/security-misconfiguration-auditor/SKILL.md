---
name: security-misconfiguration-auditor
description: Inspect runtime, web, container, and deployment configuration for unsafe production defaults. Use before release or when CORS, cookies, debug mode, network exposure, TLS, or headers change.
---

# Purpose

Catch secure-code deployments made unsafe by configuration.

# When to activate

Deployment/runtime configuration changes or a production-readiness review is requested.

# When not to activate

Pure library code has no runtime/service configuration surface.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Deployment manifests/config
- Environment designation
- Network/auth architecture

# Workflow

1. Identify configurations whose safe value changes between development and production.
2. Check debug/dev modes, wildcard CORS, cookie/session flags, TLS assumptions, exposed admin/metrics ports, default credentials, verbose errors, host binding, and security headers where applicable.
3. Compare duplicate settings across application, proxy, container, and platform layers for contradictory values.
4. Check secrets are references/variables rather than committed values.
5. Verify fail-closed behavior for missing security-critical configuration.
6. Run configuration validation or local production-mode startup when feasible.
7. Record environment-specific controls that cannot be observed from the repository.

# Relevant tools

Config search, container/runtime start, headers/probes, IaC tooling.

# Safety restrictions

Do not disable TLS/sandbox/security headers merely to make a local check pass.

# Validation

- Production-mode configuration starts with intended security settings.
- Missing critical configuration fails visibly/safely.
- Findings cite the exact configuration source and environment scope.

# Expected output

- Configuration findings
- Production-mode check
- Unverifiable platform controls
- Remediation evidence

# Failure handling

If managed-platform settings are inaccessible, report them as external verification items rather than inferring defaults.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P019, P040. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
