---
name: multi-agent-integration-reviewer
description: Integrate parallel agent changes by detecting file overlap, incompatible assumptions, duplicated implementations, semantic conflicts, and missing combined tests. Use before merging worker branches or worktrees.
---

# Purpose

Ensure independently correct patches still form one coherent system.

# When to activate

Two or more agents/branches/worktrees changed related parts of a project.

# When not to activate

Only one patch exists or parallel changes are provably independent generated artifacts.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Base commit
- Agent branches/diffs
- Assigned scopes and requirements
- Validation from each worker

# Workflow

1. Verify all branches share the intended base and capture each worker's claimed scope/evidence.
2. Compare changed-file overlap and also dependency/API/schema overlap even when files differ.
3. Detect duplicated solutions, inconsistent names/types/config keys, conflicting migrations, version bumps, generated files, and tests that assume incompatible behavior.
4. Choose one canonical implementation per responsibility and integrate in dependency order.
5. Resolve semantic conflicts by the authoritative requirement and repository architecture, not by keeping both versions.
6. Run each worker's focused checks plus combined integration/build/E2E tests that cross their boundaries.
7. Review the final diff for lost changes and delete obsolete duplicate paths.

# Relevant tools

Git branches/worktrees/diff, dependency search, combined test suite.

# Safety restrictions

Do not merge merely because Git reports no textual conflicts; semantic conflicts require review.

# Validation

- No unresolved overlapping responsibility or schema/API mismatch remains.
- Combined tests pass after integration, not only branch-local tests.
- The final diff can trace each retained change to a requirement/worker rationale.

# Expected output

- Agent change matrix
- Conflict/duplication findings
- Integration decisions
- Combined validation

# Failure handling

If a worker's validation cannot be reproduced, mark that patch unverified and inspect/test it before relying on the claim.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P049. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
