---
name: input-validation-auditor
description: Audit server-side validation at trust boundaries for shape, type, range, format, size, and semantic constraints. Use for APIs, forms, uploads, imports, or external events.
---

# Purpose

Ensure malformed or adversarial inputs fail safely before reaching business logic or storage.

# When to activate

External/user-controlled data enters a server process or persistent model.

# When not to activate

Only trusted internal values are moved between already-validated components.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Input schemas/contracts
- Entry points
- Business constraints and persistence model

# Workflow

1. Enumerate each trust-boundary payload and its authoritative server-side schema.
2. Compare required/optional fields, types, ranges, formats, lengths, enum values, and unknown-field handling.
3. Identify semantic constraints that schemas alone cannot express, such as date ordering or cross-field invariants.
4. Check upload/file size, content type, decompression/parse limits, and collection bounds where relevant.
5. Test valid boundary values plus missing, malformed, oversized, unexpected, and semantically invalid cases.
6. Verify validation happens before side effects and produces consistent non-sensitive errors.
7. Confirm clients and documentation match the server contract.

# Relevant tools

Schema validators, API tests, model constraints, documentation.

# Safety restrictions

Do not rely on client-side validation as a server security control.

# Validation

- Malformed and boundary inputs are rejected before protected side effects.
- Valid boundary values remain accepted.
- Schema/documentation mismatch is resolved or reported.

# Expected output

- Validation matrix
- Missing constraints
- Test results
- Contract/documentation deltas

# Failure handling

If domain constraints are unknown, separate structural validation from the unresolved business-rule questions.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P017. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
