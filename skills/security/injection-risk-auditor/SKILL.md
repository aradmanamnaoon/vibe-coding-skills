---
name: injection-risk-auditor
description: Trace untrusted input into SQL, shell, template, path, and other interpreter sinks. Use for security review or changes involving dynamic queries/commands.
---

# Purpose

Find controllable input reaching executable interpreters without safe parameterization or validation.

# When to activate

Code constructs queries, commands, templates, file paths, expressions, or dynamic code from external input.

# When not to activate

No interpreter-like sink or external input is involved.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Input entry points
- Potential interpreter sinks
- Framework/ORM/query APIs

# Workflow

1. Identify trust-boundary inputs and the interpreter-like sinks reachable from changed code.
2. Trace data transformations rather than matching sink names alone.
3. Check whether the sink uses parameterized/bound APIs appropriate to that interpreter.
4. Flag string concatenation/interpolation where attacker-controlled syntax can survive.
5. Build benign malicious test payloads that prove whether syntax crosses the boundary; do not target external systems.
6. Fix with binding, allowlists, or structural APIs before considering escaping.
7. Re-run positive and negative tests after remediation.

# Relevant tools

Static search/dataflow tool when available, local test harness, framework docs.

# Safety restrictions

Use non-destructive synthetic payloads only; never exploit systems outside the authorized project.

# Validation

- A finding includes source-to-sink evidence, not only a suspicious string.
- Remediation removes syntax control and preserves valid inputs.
- Test payloads remain local/synthetic.

# Expected output

- Source-to-sink trace
- Exploitability evidence
- Remediation
- Regression tests

# Failure handling

If framework behavior is uncertain, consult authoritative docs or create an isolated local test instead of assuming escaping semantics.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P016. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
