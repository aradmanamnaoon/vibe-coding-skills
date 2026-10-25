---
name: dead-feature-detector
description: Trace visible controls, routes, commands, and integrations to real handlers and observable effects to find placeholders or hardcoded demos. Use before declaring a product feature complete.
---

# Purpose

Distinguish implemented features from convincing UI scaffolding.

# When to activate

A visible feature, button, menu, route, integration, or demo is claimed working.

# When not to activate

Explicitly labeled prototypes/placeholders are allowed by the current requirement.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- User-visible feature list or changed UI
- Routes/handlers/services
- Acceptance criteria

# Workflow

1. Enumerate visible actions in the changed/claimed scope and map each to its event/route handler.
2. Trace each handler through business logic to a real observable effect: state, persistence, API call, navigation, file/artifact, or external action.
3. Search for TODO/placeholder/not-implemented branches, hardcoded success, demo-only data, no-op callbacks, and handlers that only log.
4. Check loading/error/permission branches so failure does not masquerade as success.
5. Exercise the highest-value features end to end and verify the effect independently.
6. Remove or clearly label intentionally unavailable controls rather than leaving deceptive affordances.
7. Update the feature-status report from observed evidence only.

# Relevant tools

Repository search, route graph, browser/API tests; this library includes a placeholder scanner helper.

## Deterministic helper

For a dependency-free placeholder signal scan, run python scripts/scan_placeholders.py <root>. Every match requires contextual review and the end-to-end effect check in this workflow.

# Safety restrictions

Never perform an external publish/payment/destructive action merely to prove a UI button is wired unless explicitly authorized.

# Validation

- Every claimed complete visible action has a real handler and verified effect.
- No hidden hardcoded success or placeholder remains in claimed scope.
- Unavailable features are visibly/documentationally marked as such.

# Expected output

- Feature-to-handler map
- Placeholder findings
- Executed effects
- Honest completion status

# Failure handling

If an external integration cannot be exercised, verify the local contract and mark the external effect unverified rather than simulating success.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P039, P044. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
