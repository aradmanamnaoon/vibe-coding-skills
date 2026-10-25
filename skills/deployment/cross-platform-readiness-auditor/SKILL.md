---
name: cross-platform-readiness-auditor
description: Find shell, path, case, newline, permission, encoding, and runtime assumptions that break on Windows, macOS, or Linux. Use for cross-platform projects or platform-specific failures.
---

# Purpose

Catch portability defects before they appear only on another developer/runner machine.

# When to activate

A project targets multiple desktop/server OSes or a platform-specific failure is reported.

# When not to activate

The software intentionally targets one documented OS only.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Supported OS/runtime matrix
- Build/test scripts
- Filesystem/process code
- CI matrix

# Workflow

1. Identify scripts and code paths that invoke shells, binaries, paths, permissions, symlinks, signals, encodings, line endings, or case-sensitive filenames.
2. Replace shell-specific composition with language/package-manager APIs where practical or provide explicit platform branches.
3. Check path joining/quoting, executable extensions, environment-variable syntax, temp/home directories, and newline/encoding handling.
4. Check filename case collisions and assumptions about symlinks/permissions.
5. Run the narrow cross-platform tests locally for the current OS and inspect/execute CI matrices for other OSes.
6. Add fixtures for spaces, Unicode, long paths, and line endings where they touch changed code.
7. Report unsupported platforms explicitly rather than claiming parity from static inspection.

# Relevant tools

CI matrix, shell/process tests, path fixtures, target OS runners when available.

# Safety restrictions

Do not weaken filesystem permissions or security controls solely for cross-platform convenience.

# Validation

- Current-host tests pass with portability fixtures.
- CI or real target-host results are observed for claimed supported platforms where accessible.
- Remaining static-only platform claims are labeled unverified.

# Expected output

- Platform assumption list
- Portability fixes
- Local/CI matrix evidence
- Unsupported/unverified targets

# Failure handling

If a target OS runner is unavailable, do not claim runtime validation for it; provide the exact CI/host check needed.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P054. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
