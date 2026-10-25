# Research methodology

## Question

Which recurring problems in AI-assisted software development can be reduced by reusable Agent Skills, deterministic repository tooling, or carefully scoped MCP integrations?

## Evidence strategy

The corpus combines:

- current 2026 developer survey data,
- security and software-delivery research,
- official product limitations and security guidance,
- public issue reports from coding-agent projects,
- current Agent Skills and plugin documentation.

The generated evidence table contains 115 traceable evidence items across 27 named sources. Evidence types include industry research, official documentation, official security guidance, public bug report, randomized field study, research paper, research update, security study, supply-chain study, survey.

Survey percentages are copied as reported and are never converted into defect rates. A high usage percentage means a workflow is common, not that the workflow fails at that rate. Public issue reports demonstrate concrete failure modes but do not establish prevalence.

## Inclusion criteria

1. Directly relevant to AI-assisted coding, software quality, security, testing, agent reliability, deployment, maintainability, or developer workflow.
2. Prefer evidence published in the last 12 months relative to 2026-10-25.
3. Older evidence is retained when it provides a foundational controlled study or a still-relevant security result.
4. Every quantitative claim must link to a source that reports the value.
5. Product issue reports are labeled as issue evidence and are not generalized into population-level frequency estimates.

## Deduplication

Reports are grouped by underlying failure pattern. For example, repeated-tool-call bugs from different agents support one broader no-progress-loop pattern rather than becoming separate candidate problems.

## Corroboration

A problem is treated as independently corroborated when it has support from at least two materially different evidence sources or evidence types, such as a developer survey plus a security study, or an official limitation plus public issue evidence.

## Mapping to skills

Candidate skills are favored when the workflow can define:

- a recognizable trigger,
- required evidence or inputs,
- a bounded procedure,
- deterministic checks where available,
- an observable output,
- explicit failure handling,
- testable completion criteria.

Problems that require privileged infrastructure, proprietary telemetry, organizational policy decisions, or guaranteed prevention of model-level failures are documented as partially solvable rather than presented as fully solved by instructions.
