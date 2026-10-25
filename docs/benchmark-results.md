# Benchmark results

Observed locally on 2026-10-25 using Python 3.10.10 on the active Windows host.

Deterministic helper fixtures passed: **5/5**.

| Fixture | Result | Evidence | Local elapsed time |
|---|:---:|---|---:|
| secret leakage helper | pass | detected 2 redacted finding(s) | 9.644 ms |
| skipped-test helper | pass | detected Python and JavaScript skipped-test signals | 2.66 ms |
| dead-feature helper | pass | detected empty handler and implementation-marker signals | 1.673 ms |
| environment-config helper | pass | mapped two environment keys to their source files | 3.088 ms |
| dependency-cycle helper | pass | detected the seeded two-module import cycle | 4.663 ms |

## Interpretation

These measurements establish that the bundled deterministic helpers recognize their seeded fixture conditions and that the secret scanner does not echo its seeded credential value. The elapsed times are informational local observations, not cross-machine performance claims.

No agent-versus-agent or agent-with-skill versus agent-without-skill success-rate claim is reported. Agent-level benchmark status is **not executed** for this release.
