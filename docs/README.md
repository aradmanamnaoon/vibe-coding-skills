# Documentation hub

<div align="center">

### Architecture · security · testing · compatibility · validation · release evidence

[Root README](../README.md) · [Skills](../skills/README.md) · [Research](../research/README.md) · [Roadmap](../ROADMAP.md)

</div>

## Find the right document

| Goal | Start here |
|---|---|
| Understand repository boundaries and data flow | [architecture.md](architecture.md) |
| Understand the skill format and catalog contract | [skill-catalog-design.md](skill-catalog-design.md) and [skill-standard-notes.md](skill-standard-notes.md) |
| Understand tests and release gates | [testing-strategy.md](testing-strategy.md) |
| Review threat model and installer safety | [security-model.md](security-model.md) |
| Inspect vendor compatibility evidence | [compatibility-research.md](compatibility-research.md) |
| See the concise compatibility status | [compatibility-matrix.md](compatibility-matrix.md) |
| See per-skill validation status | [validation-report.md](validation-report.md) |
| Understand benchmark design | [benchmark-methodology.md](benchmark-methodology.md) |
| See deterministic benchmark results | [benchmark-results.md](benchmark-results.md) |
| Reproduce the observed host setup | [development-environment.md](development-environment.md) |
| Review release caveats | [known-limitations.md](known-limitations.md) |

## Evidence flow

~~~mermaid
flowchart TD
    A[Source skills] --> B[Structural validation]
    A --> C[Helper fixture tests]
    A --> D[Installer smoke test]
    B --> E[Generated validation report]
    C --> F[Benchmark results]
    D --> G[Doctor / install evidence]
    E --> H[Cross-platform GitHub Actions]
    F --> H
    G --> H
    H --> I[Release claims]
    J[Agent behavioral comparison] -. not executed .-> I
~~~

## Current release gates

| Gate | Observed status |
|---|---|
| Skill structural validation | **42/42 pass** |
| Local unit/fixture suite | **22/22 pass** |
| Deterministic helper benchmark | **5/5 pass** |
| Repository lint | **pass** |
| Documentation link check | **pass** |
| Repository credential-pattern scan | **clean at release audit** |
| Full-library smoke install | **42/42 installed and validated** |
| Hosted CI | **6/6 matrix jobs pass** on last published release state |
| Controlled agent-with-skill vs control | **not executed** |

The last published CI evidence before this documentation refresh covered Windows, macOS, and Ubuntu on Python 3.10 and 3.13. A new push must be re-verified before these docs are treated as release-current.

## Compatibility at a glance

| Ecosystem | Format support researched | Repository-specific runtime behavior |
|---|:---:|---|
| OpenAI Agent Skills / Codex | yes | structural only; Codex CLI 0.164.0 installed but unauthenticated |
| Claude Code | yes | not executed |
| Cursor | yes | not executed |
| GitHub Copilot | yes | not executed |

Compatibility means the format/discovery model is documented, not that all 42 workflows have been behaviorally exercised on every product.

## Release philosophy

The documentation intentionally distinguishes what is **implemented**, **structurally validated**, **deterministically fixture-tested**, **hosted-CI tested**, and **agent-tested**. Missing runtime evidence stays visible instead of being converted into a percentage or implied success.
