---
name: scope-drift-guard
description: Detect edits outside the requested change surface and require a dependency rationale for every additional file. Use during or after autonomous code changes.
---

# Purpose

Keep agent edits reviewable and prevent opportunistic unrelated cleanup.

# When to activate

A task has a defined scope or an agent has produced a broad diff.

# When not to activate

A deliberately repository-wide migration explicitly authorizes broad edits.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Task requirements
- Baseline commit/status
- Changed-file diff
- Repository instructions/ownership

# Workflow

1. Define the expected change surface from requirements and known dependency paths before broad editing.
2. List changed files against the baseline and classify each as direct requirement, necessary dependency, generated artifact, validation/documentation, or unrelated.
3. For necessary dependency files, state the concrete caller/contract reason.
4. Flag drive-by formatting, renames, dependency upgrades, cleanup, or refactors with no requirement/dependency justification.
5. Revert or split unrelated changes while preserving other authors' pre-existing working-tree changes.
6. Re-run focused tests after narrowing because removing incidental changes can expose hidden coupling.
7. Report the final classified changed-file set.

# Relevant tools

Version control, repository dependency/caller search; this library includes a scope helper.

# Safety restrictions

Never use reset/clean/blanket formatting to remove drift when it could destroy unrelated user work.

# Validation

- Every changed file has a defensible category tied to the task.
- No pre-existing unrelated working-tree change is overwritten/reverted.
- The narrowed patch still passes relevant checks.

# Expected output

- Changed-file scope table
- Flagged drift
- Files removed/split from scope
- Post-narrowing validation

# Failure handling

If the baseline includes pre-existing uncommitted work, identify it first and exclude it from the agent-owned diff rather than resetting it.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P046, P010. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
