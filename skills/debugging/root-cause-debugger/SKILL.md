---
name: root-cause-debugger
description: Diagnose recurring software failures from reproducible evidence, logs, failing tests, and causal hypotheses. Use when a bug fix is uncertain, repeated, or risks treating symptoms.
---

# Purpose

Find the smallest falsifiable explanation for a failure before changing code.

# When to activate

A bug, runtime failure, flaky behavior, or repeated unsuccessful fix needs diagnosis.

# When not to activate

The root cause is already proven by a minimal failing test and the requested task is only to implement the known fix.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Failure report or expected/actual behavior
- Relevant logs, stack traces, and commands
- Repository state and recent changes

# Workflow

1. Reproduce the failure with the narrowest command or test available.
2. Capture the exact failing assertion, frame, request, or observable symptom before editing.
3. List at most three causal hypotheses and state what evidence would falsify each.
4. Inspect the code paths and recent changes that connect the symptom to each hypothesis.
5. Run the cheapest discriminating check first; discard hypotheses contradicted by evidence.
6. Implement the smallest fix that addresses the supported cause.
7. Run the original reproducer, focused regression tests, and one adjacent unaffected path.

# Relevant tools

Repository search, test runner, logs, debugger, version-control history when available.

# Safety restrictions

Do not delete data, weaken assertions, suppress exceptions, or broaden retries merely to hide the symptom.

# Validation

- The original failure changes from red to green for the expected reason.
- A regression test fails before the fix and passes after it when feasible.
- No unrelated behavior or files changed without a dependency rationale.

# Expected output

- Root-cause statement with evidence
- Changed files and why they are necessary
- Commands/tests executed with observed results
- Remaining uncertainty

# Failure handling

If the failure cannot be reproduced, stop code edits and report the missing environment, inputs, or observability needed to discriminate hypotheses.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P006, P008, P011. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
