---
name: reproduction-builder
description: Create the smallest reliable reproducer for a reported software failure before attempting a fix. Use when a bug is intermittent, environment-sensitive, or not covered by a failing test.
---

# Purpose

Convert an ambiguous bug report into an executable failing case with controlled inputs.

# When to activate

A defect is reported without a stable failing test or command.

# When not to activate

The task is purely explanatory or the existing test already reproduces the failure deterministically.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Bug report and environment details
- Candidate entry point
- Relevant data/configuration

# Workflow

1. Write down expected behavior, observed behavior, and the minimum trigger conditions separately.
2. Start from the nearest existing test or executable path rather than a new harness.
3. Remove unrelated inputs and dependencies while checking that the failure remains.
4. Control random seeds, time, network, filesystem, locale, and concurrency where they affect determinism.
5. Turn the minimized case into a test/fixture when appropriate.
6. Run it at least twice or across the relevant boundary to confirm reliability.
7. Only then hand off to diagnosis or fixing.

# Relevant tools

Test framework, temporary fixtures, logs, environment inspection.

# Safety restrictions

Use synthetic or already-authorized test data; never copy production secrets or personal data into a fixture.

# Validation

- The reproducer fails before the fix with the reported symptom.
- Unrelated setup has been removed without losing the failure.
- Known nondeterministic dependencies are controlled or explicitly documented.

# Expected output

- Minimal reproduction command/test
- Required fixture/input
- Expected and observed result
- Uncontrolled environmental factors

# Failure handling

If the bug cannot be reproduced, provide a capture plan for the missing logs/state rather than fabricating a local failure.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P012. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
