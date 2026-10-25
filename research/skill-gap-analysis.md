# Skill gap analysis

## High-value gaps

| Gap | Evidence-backed failure | Existing tooling gap | Library response |
|---|---|---|---|
| Evidence-bound completion | plausible wrong output and low trust for unverifiable work | agents can run tests but do not consistently bind each claim to observed evidence | completion-claims-auditor plus requirement-traceability-auditor |
| Progress-aware loop control | repeated tool/API retries and debugging loops | naive repetition detection can miss infinite loops or stop legitimate repeated progress | loop-breaker with progress markers and retry classification |
| Existing-work preservation | hard-to-review diffs, destructive rewrites, scope drift | diff viewers show changes after the fact | pre-edit baseline plus scope ledger plus post-edit regression guard |
| Dependency grounding | hallucinated packages and versions | package managers fail after the guess rather than enforcing pre-change grounding | dependency-grounding-auditor |
| Product completeness | placeholder UI and mocked integrations | component/unit tests can pass while a visible feature is inert | dead-feature-detector plus UI/API flow evidence |
| Test execution integrity | disabled, skipped, or shallow tests | file presence and green status can hide missing execution | test-quality-auditor |
| Multi-agent integration | concurrent agents overlap or make inconsistent assumptions | clean Git merges do not detect semantic conflict | multi-agent-integration-reviewer |
| MCP reliability/security | slow startup, retries, process proliferation, broad permissions | MCP exposes tools but does not guarantee client-side supervision or least privilege | mcp-reliability-auditor plus agent-tool-trust-auditor |
| Release evidence | version/tag/artifact mismatch, builds that are not runnable | artifact upload alone is not runtime verification | release-verification-agent |
| Context recovery | session continuity and context-window loss | conversational memory is product-dependent | repository-evidence-first project-context-recovery |

## Candidates intentionally combined

- Runtime error investigation and build failure investigation share evidence-first diagnosis mechanics with root-cause-debugger.
- Retry/no-progress behavior remains separate in loop-breaker because its completion criteria are different.
- Generic safe-refactoring planning is folded into architecture, scope, and preservation skills.
- Generic repository onboarding is folded into project-context-recovery and documentation accuracy.
- Deployment readiness, smoke verification, and environment configuration remain distinct only where evidence and tools differ.

## Only partially solvable by skills

- model hallucinations can be reduced by grounding and verification, not eliminated;
- prompt injection requires platform and tool security boundaries in addition to instructions;
- hosted runner, registry, or production outages need external observability and credentials;
- security scanners have false negatives;
- architecture and UX contain domain judgments that cannot be fully automated;
- cross-platform behavior ultimately needs target-platform execution.
