---
name: release-verification-agent
description: Cross-check version metadata, changelog, tags, packaged artifacts, install/start behavior, and publication workflow before or after a release. Use for release preparation or audit.
---

# Purpose

Prove a release artifact corresponds to the intended commit and can actually be consumed.

# When to activate

A version/tag/package/installer/release is being prepared or claimed published.

# When not to activate

Normal development changes with no release artifact or versioning impact.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Target version and commit
- Version files/changelog
- Build/package workflow
- Release artifacts or draft

# Workflow

1. Identify the canonical version and enumerate every metadata location that must agree.
2. Confirm changelog/release notes describe actual changes and do not claim unverified features.
3. Build artifacts from a clean tree/CI path and record their names, hashes, sizes, and source commit where feasible.
4. Install or unpack the actual artifact in an isolated destination and run a minimal start/import/version smoke check.
5. Verify tags/releases point to the intended commit and publication workflow actually publishes, rather than only uploading CI artifacts.
6. Check platform-specific artifacts only on environments that can genuinely build/run them; leave others pending.
7. After publication, fetch remote release metadata and compare it with local expectations.

# Relevant tools

Version control, build/package tools, checksum tool, isolated install, GitHub release/CI APIs.

# Safety restrictions

Never overwrite tags, force-push release history, or publish without authorization already established for the project.

# Validation

- Version/tag/changelog/artifact metadata agree.
- At least one clean artifact consumption smoke test is observed for each locally supportable artifact.
- Remote publication is verified from the remote service, not inferred from a local commit.

# Expected output

- Release evidence matrix
- Artifact hashes/smoke results
- Remote tag/release state
- Platform gaps

# Failure handling

If signing/notarization/other-platform runners are unavailable, report those as release blockers or pending checks rather than simulating them.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P053, P027. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
