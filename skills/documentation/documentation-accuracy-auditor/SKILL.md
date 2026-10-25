---
name: documentation-accuracy-auditor
description: Verify README, setup, examples, commands, API docs, screenshots/claims, and paths against the current repository. Use after implementation or before release.
---

# Purpose

Prevent documentation from describing a project that no longer exists.

# When to activate

Code/config/CLI behavior changed or documentation is being prepared for publication.

# When not to activate

Internal refactor has no externally documented behavior and all generated docs are unaffected.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Documentation files
- Current CLI/API/config
- Build/test environment

# Workflow

1. Extract executable claims from docs: commands, filenames, flags, endpoints, versions, outputs, supported environments, badges, and feature status.
2. Check referenced files/anchors/paths exist and internal links resolve.
3. Run quick-start and representative commands in a clean/local environment when feasible.
4. Compare API/CLI examples to current parser/schema/types and update stale output/options.
5. Verify screenshots or benchmark/status claims have corresponding current evidence; remove stale/unsupported claims.
6. Check installation instructions do not expose secrets or rely on undeclared global state.
7. Run link/doc validation and record external links that could not be checked.

# Relevant tools

Repository search, CLI --help, link checker when available, clean environment.

# Safety restrictions

Do not fabricate badges, benchmark results, screenshots, download counts, or compatibility claims.

# Validation

- All local links/paths and runnable commands in the reviewed scope are verified.
- Feature/status claims match validation evidence.
- Known environment prerequisites and limitations are explicit.

# Expected output

- Documentation claim audit
- Commands actually run
- Broken/stale items fixed
- Unverified external references

# Failure handling

If an external link/service cannot be reached, leave the link only when authoritative and mark runtime validation separately rather than inventing accessibility.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P051. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
