---
name: test-quality-auditor
description: Detect skipped, vacuous, over-mocked, implementation-mirroring, and nondeterministic tests that create false confidence. Use when a suite is green but quality is uncertain.
---

# Purpose

Assess whether tests would actually fail for meaningful defects.

# When to activate

A test suite exists and confidence in its signal matters.

# When not to activate

The task only needs a quick known-good smoke command and test quality is outside scope.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Test files and runner configuration
- Recent test output
- Changed production behavior

# Workflow

1. Inspect test discovery configuration and executed counts so disabled/skipped tests are visible.
2. Flag assertions that only check status/non-null without important behavior, assertions computed with the same logic as production, and tests with no assertion/effect verification.
3. Identify mocks that replace the exact integration boundary whose behavior is under test.
4. Check shared state, ordering assumptions, time/random/network dependencies, and cleanup.
5. Use a small mutation thought experiment or actual safe mutation: state what defect each critical test would catch.
6. Improve the highest-risk tests with negative/boundary behavior rather than multiplying shallow cases.
7. Run tests in a clean/reordered context when the framework supports it.

# Relevant tools

Test runner, coverage/mutation tools when available, this library's skipped-test helper.

## Deterministic helper

For a dependency-free skipped-test inventory, run python scripts/find_skipped_tests.py <root>. Treat results as review targets; an intentional skip is not automatically a defect.

# Safety restrictions

Do not delete, unskip blindly, or weaken assertions solely to make the suite green.

# Validation

- Critical tests are actually discovered and executed.
- Representative defects would make the relevant test fail.
- Known skipped/xfail tests are accounted for rather than hidden by a green summary.

# Expected output

- Executed/skipped inventory
- Weak-test findings
- Improved assertions/fixtures
- Remaining signal limitations

# Failure handling

If mutation or reordering tooling is unavailable, perform the defect-to-assertion analysis manually and report it as such.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P022, P023, P026. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
