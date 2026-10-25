---
name: regression-detector
description: Detect behavior regressions introduced by a change by comparing baselines, requirements, tests, and adjacent flows. Use after a fix, refactor, dependency change, or generated patch.
---

# Purpose

Prove the requested behavior improved without silently breaking preserved behavior.

# When to activate

A patch changes executable behavior or crosses module/API boundaries.

# When not to activate

Documentation-only changes with no executable behavior and no generated artifacts.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Diff or changed-file list
- Baseline tests/behavior
- Requested acceptance criteria

# Workflow

1. Map each changed production file to the behaviors or interfaces it can affect.
2. Identify the narrow regression suite plus at least one adjacent preserved path for each high-impact change.
3. Run the relevant baseline before editing when practical, then run the same checks after the change.
4. Compare failures, warnings, snapshots, API shapes, persisted data, and performance guardrails that are part of the contract.
5. Investigate every new failure; do not update snapshots/fixtures until the behavior change is confirmed intentional.
6. Add a regression test for the fixed defect when it provides durable value.
7. Report preserved behaviors separately from newly validated requirements.

# Relevant tools

Version control, test runners, build/type/lint checks, API/schema comparison.

# Safety restrictions

Never weaken or delete a failing test to make the regression report green without proving the contract changed.

# Validation

- No previously passing relevant check fails after the patch without an accepted contract change.
- The original defect is covered when feasible.
- Snapshot/golden changes are justified by an explicit behavior change.

# Expected output

- Regression matrix
- Before/after command evidence
- New or changed tests
- Unresolved regressions

# Failure handling

If a baseline cannot run in the current environment, mark that check not executed and identify the clean environment or CI target needed.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P009, P048. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
