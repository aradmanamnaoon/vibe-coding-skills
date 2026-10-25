---
name: production-readiness-auditor
description: Audit a service or application for deployability, health/readiness, logging, failure behavior, backup/recovery assumptions, and critical smoke checks. Use before a release or production handoff.
---

# Purpose

Require operational evidence in addition to a successful build.

# When to activate

A service/application is approaching production deployment or a readiness review is requested.

# When not to activate

A library/package has no running service or production operation surface.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Deployment architecture
- Build/start process
- Critical user/API flows
- Observability/health configuration

# Workflow

1. Verify reproducible build and production-mode startup from declared dependencies/configuration.
2. Check liveness/readiness semantics distinguish process alive from dependencies ready when appropriate.
3. Identify critical dependency failures and ensure startup/runtime behavior is observable rather than silently degraded.
4. Check structured logs/error reporting avoid secrets and contain enough correlation/context to diagnose critical flows.
5. Review persistence backup/restore, migration, queue/retry, and data-loss assumptions relevant to this service.
6. Define and run the smallest post-deploy smoke set that proves critical paths without destructive external effects.
7. Record monitoring/alerts/SLIs that require platform access as external checks, not inferred evidence.

# Relevant tools

Build/runtime, container, smoke probes, logs, deployment config, platform tools when authorized.

# Safety restrictions

Do not deploy or mutate production merely because a readiness audit was requested unless deployment is explicitly authorized.

# Validation

- Production-mode artifact starts in a clean environment where feasible.
- Health/readiness and critical smoke checks have observed results.
- Operational dependencies and unverified external controls are explicit.

# Expected output

- Readiness checklist with evidence
- Smoke results
- Operational risks
- Platform checks pending

# Failure handling

If production/platform access is unavailable, finish repository/local readiness and clearly separate unexecuted production controls.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P027, P043. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
