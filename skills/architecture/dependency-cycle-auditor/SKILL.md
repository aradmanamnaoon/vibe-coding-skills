---
name: dependency-cycle-auditor
description: Detect direct and indirect module dependency cycles and choose the smallest safe boundary to break them. Use for circular imports, layering failures, or tangled module graphs.
---

# Purpose

Turn a circular dependency into an explicit acyclic ownership boundary.

# When to activate

Circular import/build errors occur or architecture review suspects dependency cycles.

# When not to activate

Mutual references are data-level associations that do not create module/runtime dependency cycles.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Module/import graph
- Layering rules
- Cycle error or affected modules

# Workflow

1. Build or obtain the module dependency graph for the relevant package/layer.
2. Report each strongly connected component/cycle with the exact edges that create it.
3. Classify the cause: misplaced ownership, shared contract, event direction, runtime import workaround, or convenience dependency.
4. Choose the smallest edge to invert/remove by moving the contract to the owning/stable layer or passing data/callbacks through an existing boundary.
5. Avoid creating a generic 'utils' dumping ground solely to break the cycle.
6. Apply one cycle-breaking change at a time and rebuild/import-test.
7. Recompute the graph and run affected tests.

# Relevant tools

Language import/dependency graph tools; this library includes a Python helper for static imports.

## Deterministic helper

For Python repositories, run python scripts/python_import_cycles.py <package-root> as a static import-graph signal. Dynamic imports and packaging aliases can require runtime confirmation.

# Safety restrictions

Do not move security-sensitive or domain ownership into a shared module merely to remove a cycle.

# Validation

- The reported cycle no longer exists in the recomputed graph/build.
- Layer direction is clearer and no equivalent hidden runtime import replaced the edge.
- Affected module tests pass.

# Expected output

- Cycle graph/edge list
- Chosen edge and ownership rationale
- Patch
- Post-change graph/test evidence

# Failure handling

If the language uses dynamic imports that static analysis cannot resolve, combine graph evidence with runtime/import tests and state uncertainty.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P029. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
