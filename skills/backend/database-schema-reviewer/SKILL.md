---
name: database-schema-reviewer
description: Review relational or document schemas for keys, relationships, constraints, nullability, indexes, and access-pattern fit. Use before schema creation or migration.
---

# Purpose

Make data invariants explicit in the storage layer where appropriate.

# When to activate

A data model/schema/migration is introduced or changed.

# When not to activate

An in-memory-only data structure has no persistence contract.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Schema/models/migrations
- Primary queries and write flows
- Business invariants

# Workflow

1. List entities/collections and the identities used to address them.
2. Check relationship cardinality, ownership, foreign keys/references, cascade behavior, and orphan policy.
3. Check nullability, uniqueness, checks/enums, defaults, timestamps/version fields, and server-generated identifiers against invariants.
4. Map representative read/write queries to indexes; flag indexes without a query and high-impact queries without support.
5. Check tenant/authorization scoping fields are representable and queryable where needed.
6. Review migration/rollout implications separately from steady-state schema quality.
7. Exercise constraints with valid and invalid fixture records.

# Relevant tools

Schema/migration tools, isolated database, query plans when available.

# Safety restrictions

Never run destructive schema experiments against production or irreplaceable data.

# Validation

- Important invariants are enforced either by storage constraints or explicitly justified application logic.
- Representative queries match index/relationship design.
- Schema tests/migrations run in an isolated database when available.

# Expected output

- Entity/relationship findings
- Missing/excess constraints
- Index rationale
- Executed schema tests

# Failure handling

If real access patterns or invariants are unknown, ask from existing product/spec evidence and mark unresolved design choices rather than guessing.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P031. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
