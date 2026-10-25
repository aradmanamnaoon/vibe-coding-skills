---
name: api-contract-auditor
description: Compare API producers, consumers, schemas, types, status codes, and error shapes to detect contract drift. Use for client/server changes or API versioning.
---

# Purpose

Keep independently changed API layers compatible.

# When to activate

An API endpoint/schema/client/type changes or integration errors suggest drift.

# When not to activate

Internal function refactor with no serialized/public boundary.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Server routes/schema
- Client calls/types
- OpenAPI/GraphQL/protobuf or docs
- Relevant tests

# Workflow

1. Identify changed request/response fields, types, requiredness, status codes, headers, and error envelopes.
2. Compare authoritative schema to server implementation and every in-repo consumer.
3. Check serialization details such as casing, nullability, dates, enums, pagination, and unknown fields.
4. Check backward compatibility for existing clients unless the change is explicitly breaking/versioned.
5. Add/repair contract tests at the serialization boundary.
6. Run server and client type/build tests plus the narrow contract suite.
7. Update docs/generated clients only from the confirmed contract source.

# Relevant tools

Schema tooling, type checker, API tests, generated-client tooling.

# Safety restrictions

Do not silently make all fields optional to suppress compatibility failures.

# Validation

- Producer and in-repo consumers agree on the serialized contract.
- Intentional breaking changes are explicit/versioned.
- Contract tests exercise both success and representative error behavior.

# Expected output

- Contract diff
- Producer/consumer mismatches
- Compatibility decision
- Test evidence

# Failure handling

If the authoritative schema is unclear, identify the source-of-truth conflict before editing multiple layers.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P025, P003. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
