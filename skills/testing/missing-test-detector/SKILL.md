---
name: missing-test-detector
description: Map changed or critical behavior to automated checks and identify meaningful untested paths. Use after feature work, bug fixes, or when coverage appears misleading.
---

# Purpose

Find behavior with no durable automated evidence, not merely uncovered lines.

# When to activate

Production behavior changes or a review asks whether testing is sufficient.

# When not to activate

Documentation-only change with no generated/runtime behavior.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Changed files and diff
- Existing test inventory
- Acceptance criteria or bug reproducer

# Workflow

1. Translate each externally observable requirement/change into testable behaviors and failure modes.
2. Locate existing tests by behavior/API rather than filename similarity.
3. Build a requirement-to-test map: covered directly, covered indirectly, or missing.
4. Prioritize missing tests for security boundaries, persistence, errors, concurrency, and regression-prone behavior over trivial getters/setters.
5. Add the smallest durable tests needed for high-risk gaps.
6. Run the focused suite and confirm the new test would fail against the relevant pre-fix defect when practical.
7. Do not use coverage percentage as the only completion criterion.

# Relevant tools

Repository/test discovery, coverage when available, diff analysis.

# Safety restrictions

Do not create tests that merely assert mocked success for the same implementation being tested.

# Validation

- Every high-risk changed behavior is either tested or explicitly justified as not automatable here.
- New regression tests target behavior rather than implementation details.
- Focused tests pass after the implementation.

# Expected output

- Behavior-to-test map
- High-risk gaps
- Added tests
- Justified exclusions

# Failure handling

If the environment cannot execute a test class, still identify the gap and mark execution not performed.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P021. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
