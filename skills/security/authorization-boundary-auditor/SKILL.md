---
name: authorization-boundary-auditor
description: Audit object, action, role, and tenant authorization boundaries after identity is established. Use for permissions, ownership, admin, organization, or multi-user features.
---

# Purpose

Prevent horizontal and vertical privilege escalation.

# When to activate

Code decides whether an authenticated identity may read/change a resource or perform an action.

# When not to activate

The change only establishes identity and does not gate resources/actions.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Permission model
- Roles/tenants/ownership rules
- Protected operations and data model

# Workflow

1. List protected resources/actions and the policy expected for each role or relationship.
2. Trace each server-side entry point to an authorization decision made with authoritative resource data.
3. Look for IDOR/object-ownership gaps, admin-only actions, tenant boundary leaks, and client-supplied role/owner fields.
4. Verify collection/list queries enforce the same scope as individual-object endpoints.
5. Test allowed and denied combinations using at least two ordinary users plus privileged roles where relevant.
6. Check background jobs, exports, websocket/subscription paths, and indirect endpoints that bypass the main handler.
7. Verify denial has no side effect and returns a non-sensitive response.

# Relevant tools

Repository/data-model search, API/integration tests, policy engine if present.

# Safety restrictions

Never test against real users or production data without explicit authorization.

# Validation

- Every protected operation has an explicit policy path.
- Cross-user/cross-tenant denied cases are tested.
- Client-controlled authorization fields cannot override authoritative policy.

# Expected output

- Authorization matrix
- Entry-point mapping
- Escalation findings
- Executed allow/deny tests

# Failure handling

If business policy is ambiguous, identify the exact undecidable cases and do not invent permissions.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P015. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
