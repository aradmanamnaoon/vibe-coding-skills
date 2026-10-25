---
name: environment-parity-auditor
description: Compare local, CI, container, and production assumptions for runtime versions, dependencies, services, paths, and build/start commands. Use when software works locally but fails elsewhere.
---

# Purpose

Expose implicit machine state before it becomes a deployment-only failure.

# When to activate

A build/runtime differs across local, CI, container, or target deployment environments.

# When not to activate

A self-contained script has no deployment/runtime environment variance.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Runtime/version files
- Lockfiles/manifests
- CI/container/deployment config
- Local observed environment

# Workflow

1. Build a parity table for runtime versions, package manager, dependency lock mode, OS/shell, required services, filesystem/path assumptions, build command, start command, and environment variables.
2. Compare declared versions to actual local/CI/container configuration and find unconstrained defaults.
3. Identify dependencies on globally installed tools, writable current directory, case-insensitive paths, local ports, or undeclared services.
4. Run the build/start in the cleanest available environment, preferably a container or fresh environment matching declared config.
5. Remove or document hidden host assumptions and pin reproducible versions where appropriate.
6. Run a smoke check from the built artifact rather than development server only.
7. Separate verified parity from production settings that remain inaccessible.

# Relevant tools

Version managers, containers, CI configuration, build/start commands.

# Safety restrictions

Do not copy production secrets into a local parity environment.

# Validation

- Declared runtime/build requirements match the clean environment used for verification.
- The production-style artifact starts and passes its smoke check where feasible.
- Unverified platform assumptions are explicit.

# Expected output

- Environment parity table
- Hidden assumptions
- Clean-build/run evidence
- External production checks pending

# Failure handling

If target-platform execution is unavailable, use CI/config evidence and mark runtime parity unverified for that platform.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P040, P054. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
