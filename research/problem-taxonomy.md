# Problem taxonomy

The taxonomy separates the underlying engineering failure from the product or agent where it was observed. One skill may address several related failures when they share the same trigger and verification workflow.

## Agent Reliability

- **P004 — Missing codebase context**
- **P007 — Infinite or circular agent loops**
- **P010 — Unnecessary full-project rewrites**
- **P044 — Agent claims completion without evidence**
- **P045 — Agent silently ignores requirements**
- **P046 — Agent modifies unrelated files**
- **P047 — Project context is lost across sessions**
- **P048 — Working code is destroyed while fixing another area**
- **P049 — Parallel agents create conflicting or duplicate work**
- **P055 — MCP/plugin integration overload or failure blocks the agent**

## Architecture

- **P028 — Generated architecture accumulates oversized modules**
- **P029 — Circular dependencies and import tangles**
- **P032 — Tight coupling makes AI changes cascade**

## Backend

- **P025 — API contracts drift across client/server boundaries**
- **P031 — Database schema relationships are incorrect**
- **P033 — Database migrations risk data loss or lockups**
- **P034 — Transactions and concurrency invariants are missing**

## Code Quality

- **P001 — Plausible but wrong code**
- **P003 — Outdated or nonexistent APIs**

## Debugging

- **P006 — Poor debugging paths**
- **P008 — Symptom patching instead of root-cause fixes**
- **P011 — Logs and stack traces are ignored**
- **P012 — Failure is not reproduced before editing**

## Dependencies

- **P002 — Hallucinated packages, versions, and configuration**
- **P052 — Dead or redundant dependencies accumulate**

## Deployment

- **P027 — Deployment is declared successful without runtime verification**
- **P040 — Local environment differs from production**
- **P041 — Environment variables are missing, stale, or undocumented**
- **P042 — CI failures are patched without understanding the failing stage**
- **P043 — Production has no meaningful health or smoke checks**
- **P054 — Cross-platform assumptions break builds or runtime**

## Documentation

- **P051 — Documentation is missing or inaccurate**

## Efficiency

- **P050 — AI workflows waste tokens and repeat research**

## Frontend

- **P024 — UI flows are broken despite component success**
- **P030 — State management becomes fragile and duplicated**
- **P035 — AI-generated UI is visually inconsistent**
- **P036 — Responsive behavior breaks across viewports**
- **P037 — Accessibility requirements are missed**
- **P038 — Loading, empty, and error states are incomplete**

## Maintainability

- **P005 — Generated changes are hard to review**

## Product Completeness

- **P039 — Buttons, routes, or integrations are placeholders**

## Release

- **P053 — Release artifacts and version metadata are inconsistent**

## Security

- **P013 — Secrets are exposed in code or commits**
- **P014 — Authentication is incomplete or bypassable**
- **P015 — Authorization boundaries are incorrect**
- **P016 — Unsafe database and command queries**
- **P017 — Missing server-side input validation**
- **P018 — Vulnerable or malicious dependencies**
- **P019 — Security misconfiguration and insecure defaults**
- **P020 — Prompt injection changes tool-using agent behavior**

## Testing

- **P009 — Regressions introduced by fixes**
- **P021 — Important behavior has no automated tests**
- **P022 — Tests are superficial or assertion-poor**
- **P023 — Mocks create false confidence about integrations**
- **P026 — Tests leak state or contaminate each other**

## Cross-cutting distinctions

- **AI-specific failures:** hallucinated dependencies, false completion claims, prompt injection against tool-using agents, context loss, runaway tool loops, and MCP/plugin failure coupling.
- **General engineering failures amplified by AI:** weak tests, insecure configuration, schema mistakes, oversized modules, deployment drift, stale documentation, and release inconsistency.
- **Nontechnical-user risks:** fake completeness, placeholder UI, weak authentication, missing deployment verification, and inability to distinguish plausible output from working software.
- **Experienced-developer risks:** review overhead, change-volume instability, multi-agent conflicts, context-selection errors, and excessive tool/cost usage.
- **Not fully solvable by skills alone:** model hallucination elimination, guaranteed prompt-injection prevention, platform runtime bugs, hosted CI outages, and privileged production observability.
