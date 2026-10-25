---
name: architecture-complexity-auditor
description: Find modules whose coupling, size, responsibility mix, or change fan-out makes AI-assisted maintenance fragile. Use before major refactors or when files keep growing.
---

# Purpose

Identify architecture risk with concrete dependencies and change patterns, then propose minimal seams.

# When to activate

A module is difficult to change safely, oversized, or repeatedly touched across unrelated features.

# When not to activate

A small cohesive module is merely long because the domain itself is data-heavy/generated.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Repository/module graph
- Recent change history if available
- Architectural constraints

# Workflow

1. Identify responsibilities of the target module from its public interfaces, imports, data ownership, and callers.
2. Measure practical signals: dependency fan-in/fan-out, reasons-to-change, cyclic edges, repeated cross-layer knowledge, and test setup cost.
3. Separate size from incohesion; do not recommend splitting solely by line count.
4. Find the smallest stable seam where data/control ownership can move without duplicating state.
5. Propose incremental extraction order with compatibility points and regression checks.
6. Prefer deleting duplicated abstractions over adding a new layer.
7. Validate the first seam with tests/build before recommending further decomposition.

# Relevant tools

Repository graph/search, version history, tests, language static-analysis tools when available.

# Safety restrictions

Do not rewrite whole subsystems to satisfy a metric or aesthetic preference.

# Validation

- Every proposed boundary names the responsibility and dependency it isolates.
- The plan reduces a concrete coupling/change-fan-out problem.
- No abstraction is added without a current consumer/problem.

# Expected output

- Architecture evidence
- Risk hotspots
- Incremental refactor seams
- Validation plan

# Failure handling

If dependency information is incomplete because of dynamic loading/code generation, report the blind spot and avoid precise coupling claims.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P028, P032. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
