---
name: requirement-traceability-auditor
description: Map a large prompt, specification, or issue into stable requirements and verify each against implementation and evidence. Use for complex multi-requirement work or final audits.
---

# Purpose

Prevent silent requirement omission and make final audits reproducible.

# When to activate

A task has many requirements, later corrections, or several implementation phases.

# When not to activate

A tiny one-step change has an obvious single acceptance criterion.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Authoritative prompt/spec
- Later corrections/overrides
- Current implementation and validation evidence

# Workflow

1. Extract atomic requirements with stable IDs, preserving later overrides and explicit exclusions.
2. Classify each as functional, quality, security, compatibility, documentation, validation, publication, or constraint.
3. Map each requirement to implementation files/behavior and the evidence needed to call it satisfied.
4. Mark status as satisfied, partial, blocked, not applicable, or missing; require a reason/evidence reference for every non-missing status.
5. Resolve contradictions using the task's authority and chronology; do not silently keep superseded requirements.
6. Use the matrix to drive remaining work in priority order rather than rereading the full prompt repeatedly.
7. Re-run the traceability audit before final reporting after material changes.

# Relevant tools

Prompt/spec text, repository search, plan, tests, this library may include a traceability helper.

# Safety restrictions

Do not downgrade or reinterpret requirements merely to make the matrix green.

# Validation

- Every authoritative requirement has one current status and evidence/blocker.
- Superseded requirements are clearly identified rather than double-counted.
- No completion percentage is invented from subjective weights.

# Expected output

- Requirement matrix
- Missing/partial requirements
- Evidence references
- Remaining ordered work

# Failure handling

If requirement wording is ambiguous, use repository/context evidence to progress safe work and record the ambiguity for the smallest necessary clarification.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P045, P044. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
