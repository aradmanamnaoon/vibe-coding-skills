---
name: migration-safety-reviewer
description: Audit database migrations for destructive changes, locking, backfill, rollback, and mixed-version rollout safety. Use before applying schema/data migrations.
---

# Purpose

Prevent data loss and unsafe one-step migrations.

# When to activate

A migration changes persisted schema/data or a deploy requires coordinated DB/application versions.

# When not to activate

The change only adds isolated development fixture data with no persistent production path.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Migration files
- Database engine/version
- Deployment sequence
- Data size/criticality assumptions

# Workflow

1. Classify every operation as additive, transformative, destructive, or potentially locking/long-running.
2. Identify drops, renames, type narrowing, not-null changes, uniqueness, rewrites, backfills, and index creation that need staged rollout.
3. Use expand-migrate-contract when old and new application versions can overlap.
4. Define backup/recovery and rollback semantics; distinguish reversible schema from irreversible data transformation.
5. Test forward migration on representative data plus rollback where rollback is claimed.
6. Verify old/new application compatibility at the intended deployment boundary.
7. Document operations that require production-specific online/lock behavior verification.

# Relevant tools

Migration tool, isolated database/container, schema diff/query tools.

# Safety restrictions

Never apply destructive migrations to production or user data as part of an audit without explicit authorization.

# Validation

- No destructive operation is hidden inside a supposedly additive deploy.
- Claimed rollback is actually executable on test data.
- Mixed-version assumptions are explicit and tested where relevant.

# Expected output

- Operation classification
- Staged rollout plan
- Forward/rollback evidence
- Production-only risks

# Failure handling

If production data volume/engine behavior is unknown, flag locking/runtime risk instead of estimating it as safe.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P033. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
