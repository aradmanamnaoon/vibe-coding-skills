# Research hub

<div align="center">

### 117 evidence rows → 55 problem patterns → 20 corroborated patterns → 42 selected skills

[Methodology](research-methodology.md) · [Evidence CSV](problem-evidence.csv) · [Problems](vibe-coding-problems.md) · [Opportunities](skill-opportunities.md) · [Limitations](research-limitations.md)

</div>

## Research pipeline

~~~mermaid
flowchart LR
    A[Surveys & studies] --> E[Evidence rows]
    B[Official docs & evaluations] --> E
    C[GitHub issues & incident reports] --> E
    D[Existing tools & skill ecosystems] --> E
    E --> P[55 normalized problem patterns]
    P --> T[Taxonomy + corroboration]
    T --> S[100-point opportunity score]
    S --> K[42 selected skills]
~~~

## Current corpus

| Measure | Observed count | Meaning |
|---|---:|---|
| Curated evidence rows | **117** | traceable entries in problem-evidence.csv |
| Candidate problem patterns | **55** | normalized recurring failure modes considered |
| Independently corroborated patterns | **20** | patterns supported by at least two distinct source titles under the current criterion |
| Selected original skills | **42** | workflows chosen after scoring/consolidation |
| GitHub issue records observed during collection | **537** | public records seen before rate limiting; **not** treated as prevalence |

These counts describe this repository's evidence corpus. They are not population estimates for all developers or AI coding tools.

## Evidence strength

The research deliberately separates different kinds of support:

- **surveys/studies** can support population-level statements only within their sampled populations and methods;
- **official documentation/evaluations** establish product behavior, standards, or measured benchmark results under stated conditions;
- **issue reports/incidents** demonstrate concrete failure modes but do not establish prevalence;
- **developer discussions** can expose recurring friction but are qualitative unless independently measured;
- **existing tools** show that a problem has attracted engineering effort, not how frequently it occurs.

When evidence is heterogeneous or incomplete, the repository records limitations rather than inflating confidence.

## Navigate the evidence

| Question | File |
|---|---|
| How was evidence collected and normalized? | [research-methodology.md](research-methodology.md) |
| What sources were used? | [sources.md](sources.md) |
| What are the 55 candidate problems? | [vibe-coding-problems.md](vibe-coding-problems.md) |
| How are problems grouped? | [problem-taxonomy.md](problem-taxonomy.md) |
| What is the row-level evidence? | [problem-evidence.csv](problem-evidence.csv) |
| What already exists? | [existing-solutions.md](existing-solutions.md) |
| Which gaps remain? | [skill-gap-analysis.md](skill-gap-analysis.md) |
| How were skills prioritized? | [skill-opportunities.md](skill-opportunities.md) |
| Which existing Agent Skills were reviewed? | [existing-skills.md](existing-skills.md) |
| Which MCP options were reviewed? | [mcp-evaluation.md](mcp-evaluation.md) |
| What should not be inferred? | [research-limitations.md](research-limitations.md) |

## 100-point prioritization

| Criterion | Weight |
|---|---:|
| Severity | 20 |
| Recurrence | 15 |
| Skill solvability | 20 |
| Expected benefit | 15 |
| Feasibility | 10 |
| Uniqueness | 10 |
| Testability | 10 |
| **Total** | **100** |

The score is a prioritization aid, not a scientific estimate of prevalence. Closely related workflows were consolidated rather than split to inflate the library count.

## Research boundaries

> **Do not read “117 evidence rows” as “117 independent findings.”**

> **Do not read 537 observed public issue records as a defect rate.**

> **Do not read vendor-documented compatibility as behavioral validation in this repository.**

The GitHub collection phase hit Search API rate limits on three configured searches. Raw third-party issue bodies are intentionally not retained in the current repository; the collector uses a metadata-only ignored checkpoint to reduce prompt-injection, credential-copying, and licensing risk.
