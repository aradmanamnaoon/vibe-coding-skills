---
name: dependency-grounding-auditor
description: Verify proposed packages, versions, imports, and upgrade claims against project state and authoritative package metadata. Use before adding or changing a dependency.
---

# Purpose

Prevent invented, stale, redundant, or unjustified dependency changes.

# When to activate

An agent proposes a new package, version, import path, or dependency upgrade.

# When not to activate

No dependency change is proposed and the task can be completed with existing project capabilities.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Dependency manifest and lockfile
- Proposed package/import/version
- Runtime/toolchain version

# Workflow

1. Check whether the needed capability already exists in direct or transitive dependencies or the standard library.
2. Verify the package name and import/module mapping using the local environment, lockfile, registry, or official docs.
3. Verify the proposed version exists and supports the project's runtime/toolchain constraints.
4. Check maintenance, license, security/advisory status, and whether the package is actually necessary for the task.
5. Prefer pinned/locked reproducible changes consistent with the repository's package manager.
6. Install/update only through the repository's package manager and regenerate its lockfile when authorized.
7. Run import/build/tests that prove the dependency is usable.

# Relevant tools

Package manager, lockfile, local environment, official registry/docs, advisory scanner when available.

# Safety restrictions

Never execute an unreviewed install script outside the package manager or commit registry credentials.

# Validation

- Every added name/version is grounded in an observed local or authoritative source.
- Manifest and lockfile remain consistent.
- The dependency is used by the implementation and passes the relevant runtime/build check.

# Expected output

- Dependency evidence table
- Manifest/lockfile changes
- Compatibility/security notes
- Executed verification

# Failure handling

If registry/network access is unavailable, do not invent a version; use already-locked/local metadata or mark external verification pending.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P002, P003, P052. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
