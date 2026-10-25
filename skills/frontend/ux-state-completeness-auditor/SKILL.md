---
name: ux-state-completeness-auditor
description: Audit user flows for loading, empty, success, validation, partial, permission, offline, and error states. Use when async UI or data-driven workflows are added.
---

# Purpose

Ensure the product remains understandable outside the happy path.

# When to activate

A UI fetches/submits data, depends on permissions, or has zero/error conditions.

# When not to activate

Static content has no asynchronous/conditional state.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Flow and data sources
- Known API/error semantics
- Product copy/design conventions

# Workflow

1. Create a state matrix for each async/conditional step: initial, loading, success, empty, validation error, server/network error, permission/auth, retry/recovery, and partial/stale where relevant.
2. Trace which application state produces each UI state and find impossible/unhandled branches.
3. Check loading prevents duplicate/destructive actions without freezing unrelated navigation.
4. Check empty state explains why there is no data and provides the next useful action when appropriate.
5. Check errors preserve user input/state where safe, expose a recovery path, and avoid leaking internals.
6. Exercise representative states with controlled fixtures or network stubs that model real contracts.
7. Verify transitions between states, not only isolated screenshots.

# Relevant tools

Component/integration tests, browser network controls, product design system.

# Safety restrictions

Do not expose raw stack traces, tokens, or sensitive backend details in user-facing errors.

# Validation

- Every relevant matrix state has an intentional rendering/behavior.
- Error and retry transitions preserve safe user state.
- Critical controls do not double-submit during pending operations.

# Expected output

- State matrix
- Missing/ambiguous states
- Transition tests
- Copy/recovery observations

# Failure handling

If product copy or desired recovery behavior is unspecified, identify the design decision instead of inventing business messaging.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P038. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
