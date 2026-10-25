---
name: data-consistency-auditor
description: Review multi-step writes, retries, concurrency, and idempotency for lost updates, duplicates, partial state, and race conditions. Use for payments, jobs, counters, workflows, or shared records.
---

# Purpose

Preserve invariants under retries and concurrent execution, not only the happy path.

# When to activate

A workflow writes multiple records/services or can run concurrently/retry.

# When not to activate

A pure read-only operation has no state transition.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- State transitions and invariants
- Transaction/locking semantics
- Retry/queue behavior

# Workflow

1. Write the invariant that must remain true after success, failure, retry, and concurrent execution.
2. Identify the transaction boundary and all side effects that fall outside it.
3. Look for read-modify-write races, duplicate message/job handling, check-then-act windows, lost updates, and non-idempotent external calls.
4. Choose an appropriate control: atomic update, transaction, unique/idempotency key, optimistic version, lock, outbox/saga, or compensating action.
5. Create deterministic or repeated concurrency tests for the highest-risk interleavings.
6. Inject a failure between steps to verify partial state can recover or is prevented.
7. Verify retries converge on the same intended result.

# Relevant tools

Database/queue docs, integration tests, concurrency/stress harness.

# Safety restrictions

Use isolated test data; do not induce races or duplicate effects in production.

# Validation

- The invariant holds after success, injected failure, duplicate request, and tested concurrency interleavings.
- Controls match the actual storage/message semantics.
- Residual nondeterministic risk is documented.

# Expected output

- Invariant and transition model
- Race/partial-state findings
- Chosen consistency control
- Failure/concurrency test evidence

# Failure handling

If concurrency cannot be reproduced reliably, add invariant instrumentation/stress testing guidance and report the limitation.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P034. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
