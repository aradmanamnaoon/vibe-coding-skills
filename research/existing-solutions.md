# Existing solutions

The problems in the research corpus already have useful partial solutions. The library composes those controls into repeatable agent workflows rather than replacing mature engineering tools.

| Problem class | Existing controls | What a skill can add | What a skill cannot guarantee |
|---|---|---|---|
| Hallucinated APIs/dependencies | package registries, lockfiles, compiler/type checker, official docs | require live/local grounding before accepting names or versions; record evidence | availability or correctness of an external registry |
| Security defects | SAST, DAST, dependency scanners, threat modeling, secure frameworks | choose checks from the change surface; trace findings to exploitable paths; verify fixes independently | complete vulnerability discovery |
| Missing/weak tests | unit/integration/E2E frameworks, mutation testing, coverage | map changed behavior and requirements to tests; detect skipped/vacuous checks; insist on negative paths | semantic correctness for requirements the agent cannot observe |
| Debugging loops | logs, debuggers, test runners, git bisect | require reproduction, hypotheses, evidence, progress markers, and a bounded retry budget | deterministic reproduction of inherently intermittent or external failures |
| Scope drift | Git diffs, protected branches, CODEOWNERS, review | tie each changed file to a requirement or necessary dependency; flag unrelated rewrites | organizational ownership policy |
| Fake completeness | E2E tests, smoke tests, screenshots, API probes | build a requirement-to-evidence ledger before completion claims | subjective UX quality without human criteria |
| Architecture decay | dependency graphs, static analysis, code review | evaluate coupling and change fan-out before refactors; prevent metric-driven fragmentation | a universally optimal architecture |
| Frontend quality | design systems, accessibility tools, visual/E2E tests | define representative states/viewports and combine automated with manual checks | full WCAG conformance from automation alone |
| Deployment drift | containers, lockfiles, CI matrices, IaC, health checks | compare local/CI/prod assumptions and require post-deploy smoke evidence | access to hosted infrastructure that is not available |
| Agent/tool security | least privilege, sandboxing, approvals, content isolation | classify data versus authority, constrain tools, require approval for high-impact actions | elimination of prompt injection |
| MCP reliability | timeouts, lazy startup, health checks, process supervision | inventory startup cost, retry budgets, permissions and failure coupling | fixes for a client/server implementation bug |
| Documentation drift | docs tests, executable examples, generated API docs | verify commands, paths, APIs, screenshots and claims against repository state | future external-service changes |

The most valuable skills act as orchestration and evidence contracts: they state which tools to use, in what order, what evidence is sufficient, when to stop, and how to report uncertainty.
