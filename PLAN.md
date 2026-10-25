# Implementation plan

This plan is derived from the 2026 research corpus in research/ and is updated against the actual repository state.

## Scope selected

The first release contains 42 original skills. Selection scores and justifications are in research/skill-opportunities.md. The implementation is organized around six evidence-producing capabilities:

1. **Debug and preserve:** reproduce failures, diagnose root cause, stop no-progress loops, preserve working behavior, and detect regressions.
2. **Secure boundaries:** credentials, authentication, authorization, injection, validation, dependency risk, configuration, and tool-agent trust.
3. **Verify behavior:** missing/weak tests, real integrations, API contracts, browser flows, and dead features.
4. **Control architecture and data:** dependency cycles, schema/migration review, and consistency under retries/concurrency.
5. **Make deployment/release observable:** environment parity/configuration, CI diagnosis, production readiness, cross-platform checks, and release evidence.
6. **Make agents accountable:** requirement traceability, completion evidence, scope control, context recovery, multi-agent integration, MCP reliability, documentation accuracy, and efficiency.

## Delivery phases

| Phase | Deliverable | Acceptance criteria |
|---|---|---|
| Research | evidence corpus, taxonomy, source ledger, existing-solution/MCP review | at least 100 traceable evidence items, at least 50 candidate problems, explicit limitations |
| Foundation | dependency-free discovery/validation/installer CLI | list/search/install/update/remove/doctor/validate work; no destructive overwrite; traversal guarded |
| Skills | 42 source-of-truth skill bundles | valid metadata, unique names, required operational sections, no broken local references |
| Deterministic helpers | scanners/graph/config utilities for suitable skills | standalone, dependency-free, fixture-tested, outputs are reviewable signals rather than hidden mutations |
| Evaluation | structural tests plus representative functional fixtures | all deterministic tests green; each skill has recorded validation status; agent-level gaps explicitly marked |
| Documentation | README, catalog, architecture/testing/security/compatibility docs | commands are executable, status claims match evidence, navigation is usable |
| CI/publication | GitHub Actions and incremental pushed commits | remote main contains intended commits; CI state is observed rather than assumed |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Skill count encourages repetition | consolidate workflows by trigger/evidence contract; keep research IDs in every skill |
| Agent standard changes | keep portable core minimal and record dated compatibility research |
| MCP/plugin sprawl slows or weakens agents | make MCP optional; prefer CLI/scripts when persistent live state is unnecessary |
| Helper scanners create false positives | helpers only emit signals; SKILL.md requires contextual validation |
| Package/network outages block validation | core runtime/tests use Python standard library; external checks are separated |
| Cross-agent claims exceed testing | distinguish documented format support from behavior actually executed |
| Generated catalog/docs drift | generate catalog from validated source metadata in CI |

## Release gate

A release is blocked by any of:

- invalid skill metadata or duplicate names;
- broken local resource references;
- failing unit/helper tests;
- installer traversal or overwrite-safety regression;
- unresolved high-confidence secret finding in tracked content;
- README/catalog claims that contradict validation reports;
- unverified remote push or CI state being described as successful.

