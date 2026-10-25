---
name: existing-work-preservation
description: Establish a known-good baseline and protect unrelated working behavior before AI edits an established project. Use before risky fixes, refactors, or broad feature work.
---

# Purpose

Make preservation an explicit acceptance criterion for modifications to existing software.

# When to activate

Work occurs in a nontrivial existing repository with known working behavior or uncommitted changes.

# When not to activate

A brand-new isolated project has no prior behavior to preserve.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Git status and baseline ref
- Relevant existing tests/flows
- Requested change surface

# Workflow

1. Inspect status/branches and identify pre-existing uncommitted files before editing.
2. Run the smallest relevant baseline checks for behavior that must stay working.
3. Identify stable public interfaces/data formats and high-risk adjacent flows touched by the requested change.
4. Prefer additive/minimal patches and existing patterns over regeneration of whole modules.
5. After edits, compare diff size/ownership and run the same baseline checks plus new acceptance checks.
6. Investigate every baseline regression before expanding scope.
7. Record pre-existing failures separately from new failures.

# Relevant tools

Git status/diff/history, test/build/browser smoke checks.

# Safety restrictions

Never reset, clean, mass-reformat, or regenerate files as a shortcut when it can destroy unrelated work.

# Validation

- Pre-existing user changes are untouched unless required and authorized by the task.
- Relevant baseline checks do not newly regress.
- Public/serialized contracts change only when required and documented.

# Expected output

- Baseline state
- Protected behavior list
- Diff preservation findings
- Before/after validation

# Failure handling

If baseline tests already fail, record their exact pre-change failures and use them to distinguish new regressions.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P048, P010. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
