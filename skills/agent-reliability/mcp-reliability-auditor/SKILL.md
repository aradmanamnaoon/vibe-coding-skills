---
name: mcp-reliability-auditor
description: Audit MCP/plugin tool integrations for startup cost, health, retries, timeouts, process leaks, permission scope, and failure isolation. Use when agents stall, spawn processes, or load many MCP servers.
---

# Purpose

Keep external tool integrations observable, bounded, and isolated from unrelated work.

# When to activate

An agent uses one or more MCP/plugin servers or tool startup/retry behavior is problematic.

# When not to activate

No external tool server is used in the workflow.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- MCP/client config
- Server inventory and launch commands
- Observed process/log/latency data
- Permission roots/scopes

# Workflow

1. Inventory configured servers and record which are actually needed for the current workflow.
2. For each needed server, record transport, startup command/URL, permissions, credential source by name only, expected startup timeout, and retry policy.
3. Start/check servers individually where safe to isolate failures before testing the full client.
4. Measure/observe startup failure behavior and ensure permanent configuration errors do not trigger unbounded retries/process spawning.
5. Check cancellation/timeouts and whether a failed server blocks unrelated chat/tool operations.
6. Reduce filesystem/network/account permissions and disable unused servers for the task when configuration is project-scoped and authorized.
7. Record versions because protocol/server behavior changes quickly.

# Relevant tools

MCP config/server logs, process list, client logs, health/tool listing.

# Safety restrictions

Do not expose MCP credentials in reports or disable sandbox/host restrictions merely to make a connection succeed.

# Validation

- Each required server has an observed or explicitly unverified health state.
- Permanent errors have bounded retries and no runaway descendant-process growth in the test.
- Unused/high-impact permissions are removed or documented.

# Expected output

- MCP inventory
- Health/startup evidence
- Retry/timeout/process findings
- Permission-scope recommendations

# Failure handling

If client internals cannot expose process/queue state, test externally observable startup/timeouts and state the telemetry limitation.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P055, P007. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
