---
name: ui-flow-verifier
description: Verify real user flows in a browser across navigation, forms, async states, and errors. Use when a visible frontend feature is added or claimed complete.
---

# Purpose

Prove that a user-visible flow works end to end rather than only rendering components.

# When to activate

Frontend changes affect navigation, input, network requests, persistence, or visible outcomes.

# When not to activate

Pure styling/token changes with no interaction and existing visual checks are sufficient.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Acceptance flow
- Runnable app and test data
- Browser automation capability

# Workflow

1. Start the application in the closest supported test configuration and confirm the correct URL/build is under test.
2. Execute the critical flow using semantic roles/labels or stable test IDs, not fragile pixel coordinates.
3. Verify navigation, enabled/disabled states, validation, loading, success, empty, and at least one failure path as relevant.
4. Assert the real visible/URL/data outcome after each meaningful action rather than only click success.
5. Inspect console/network errors that occur during the flow.
6. Repeat at one representative narrow viewport if the flow is user-facing and responsive.
7. Capture deterministic test evidence; screenshots may supplement but not replace assertions.

# Relevant tools

Playwright or equivalent CLI/MCP/browser harness, app logs, network inspection.

# Safety restrictions

Use local/sandbox accounts and data. Do not publish or submit real external actions unless authorized.

# Validation

- The critical user flow reaches the specified final outcome through real handlers.
- No unexpected console/runtime error occurs in the verified flow.
- Failure/validation behavior is observed, not inferred.

# Expected output

- Executed flow steps
- Assertions and browser evidence
- Console/network findings
- Unverified flows

# Failure handling

If no browser harness is available, run lower-level checks and explicitly mark browser verification not executed.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P024, P039. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
