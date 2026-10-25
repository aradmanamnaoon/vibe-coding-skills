---
name: loop-breaker
description: Detect and stop no-progress debugging, retry, and tool-call loops while preserving repeated actions that make measurable progress. Use when the same action or error is recurring.
---

# Purpose

Prevent wasted iterations by measuring progress and changing strategy when repeated actions stop producing new evidence.

# When to activate

The agent has repeated similar commands, edits, retries, or hypotheses, or the same error returns after multiple attempts.

# When not to activate

Repeated calls are expected and each iteration has an explicit changing state, counter, page, batch, or new evidence.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Recent actions and results
- Current objective and completion criteria
- Any retry/backoff policy

# Workflow

1. Define a progress marker tied to the objective: new evidence, changed failing set, reduced error, processed item count, or state transition.
2. Summarize the last three relevant attempts as action, result, and new information.
3. Classify the repetition as progress-making, transient retry, or no-progress loop.
4. For transient failures, apply the documented bounded retry/backoff policy; never invent unlimited retries.
5. For no-progress loops, stop repeating the action and choose one materially different diagnostic strategy.
6. If two materially different strategies fail to add evidence, escalate with the exact blocker instead of continuing.
7. Record the stop condition so a later agent does not restart the same loop.

# Relevant tools

Command/tool history, error classification, task plan, logs.

# Safety restrictions

Never terminate a legitimate batch solely because command names repeat; judge progress from state/evidence.

# Validation

- A repeated action is allowed only when its progress marker changes or a bounded transient retry policy justifies it.
- No permanent/structural error is retried indefinitely.
- The final report lists attempts already exhausted.

# Expected output

- Progress marker
- Loop classification
- Next distinct action or explicit escalation
- Exhausted attempts

# Failure handling

When it is unclear whether state is changing, collect one explicit state snapshot before deciding; do not keep retrying to discover that implicitly.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P007, P050. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
