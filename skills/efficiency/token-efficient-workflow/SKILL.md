---
name: token-efficient-workflow
description: Reduce repeated context, research, tool calls, and overengineering while preserving verification quality. Use when an agent is rereading the same material or spending heavily on low-value exploration.
---

# Purpose

Optimize total work-to-evidence rather than minimizing tokens at the expense of correctness.

# When to activate

A long coding task shows repeated searches/reads, large redundant context, or unnecessary tool invocations.

# When not to activate

The task is small or additional context is necessary to resolve a real uncertainty.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Task objective and acceptance criteria
- Recent tool/search history
- Known repository map/evidence

# Workflow

1. Define the decision that each next read/search/tool call must inform.
2. Cache verified facts in a short task ledger with source/path and freshness so they are not repeatedly rediscovered.
3. Batch independent reads/searches and narrow large files to relevant regions after orientation.
4. Prefer deterministic local commands for facts such as test discovery, manifests, diffs, and file existence instead of asking an LLM to infer them.
5. Stop research when the acceptance decision is supported; do not collect sources solely to reach a count.
6. Choose the cheapest model/tool appropriate for routine transformation only when the surrounding product permits routing and quality remains adequate.
7. Keep validation gates even when optimizing; remove redundant checks only when no code/evidence changed.

# Relevant tools

Task plan, repository index/search, deterministic CLI tools, usage metrics when the platform exposes them.

# Safety restrictions

Do not omit security/tests or use stale cached facts simply to reduce token/tool counts.

# Validation

- Repeated identical searches/reads decrease without missing required evidence.
- The final task still meets all acceptance/verification criteria.
- Saved context records sources rather than unsupported summaries.

# Expected output

- Reusable context ledger
- Redundant calls removed
- Verification retained
- Remaining expensive dependencies

# Failure handling

If uncertainty affects correctness, spend the additional context/tool call and record why; efficiency never overrides required evidence.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P050. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
