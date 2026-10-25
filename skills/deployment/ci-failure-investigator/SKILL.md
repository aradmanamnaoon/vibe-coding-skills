---
name: ci-failure-investigator
description: Diagnose failing CI jobs from the exact failing step, logs, environment, and reproducible local checks. Use when a pipeline fails or an agent proposes speculative workflow edits.
---

# Purpose

Turn a red CI run into a localized cause and verified repair.

# When to activate

A CI workflow, build, test, lint, packaging, or permission job fails.

# When not to activate

The failure is an acknowledged external provider outage with no repository change to make.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Workflow/run URL or logs
- Commit/ref under test
- Relevant CI configuration

# Workflow

1. Identify the first failing job and first causally relevant failing step, not only the final job status.
2. Extract the exact command, exit code, environment/runner, and error output.
3. Classify the cause: repository code/test, dependency, workflow syntax, permission/secret, cache/artifact, platform, or external service.
4. Reproduce the command locally/containerized when the environment permits; otherwise isolate the workflow condition.
5. Make the smallest code/configuration change that addresses the classified cause.
6. Re-run the narrow check and then the affected workflow when accessible.
7. Confirm no required step was skipped or changed to continue-on-error merely to obtain green status.

# Relevant tools

CI logs, workflow files, local runner/container, GitHub Actions APIs when available.

# Safety restrictions

Do not expose secrets from logs or broaden token permissions as a convenience fix.

# Validation

- The original failing command/job passes or the external blocker is independently confirmed.
- Required tests remain enabled and failure propagation remains intact.
- Workflow permissions are no broader than required.

# Expected output

- Failing job/step and evidence
- Cause classification
- Patch rationale
- Local and hosted validation status

# Failure handling

When hosted CI cannot be rerun, report local verification separately and leave hosted status pending rather than claiming success.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P042. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
