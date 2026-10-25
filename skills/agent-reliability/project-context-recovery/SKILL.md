---
name: project-context-recovery
description: Reconstruct an interrupted project's goals, current state, completed work, and next safe actions from repository evidence. Use after context loss, compaction, session changes, or handoff.
---

# Purpose

Resume without restarting or duplicating completed work.

# When to activate

A coding session was interrupted or the current agent lacks reliable project history.

# When not to activate

The repository is new and no prior work exists.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Repository instructions
- Git status/log/branches
- Plans/issues/docs
- Recent tests/artifacts

# Workflow

1. Read repository instructions and current Git status before making changes.
2. Inspect recent commits/diffs and task/plan files to infer what has actually been completed.
3. Locate authoritative prompt/spec/issue references in the repository or supplied context.
4. Build a concise state ledger: objective, completed evidence, in-progress uncommitted work, blockers, pending requirements.
5. Run a cheap health check only when it helps distinguish stale documentation from current behavior.
6. Continue from the first unsupported requirement; do not recreate files/features already present and validated.
7. Persist a compact handoff artifact when the project explicitly benefits from portable continuity.

# Relevant tools

Git, repository search, task docs/issues, test commands.

# Safety restrictions

Do not reset/clean or overwrite ambiguous uncommitted work during recovery.

# Validation

- Recovered state matches observable Git/files/test evidence.
- No completed work is redundantly reimplemented.
- Pre-existing uncommitted changes remain preserved.

# Expected output

- Recovered objective/state
- Completed evidence
- Uncommitted ownership notes
- Next ordered actions

# Failure handling

If a decision existed only in an unavailable prior conversation, state that it cannot be recovered from repository evidence and avoid guessing destructive changes.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P047. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
