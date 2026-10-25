# Research limitations

The current corpus contains 117 evidence items and 55 candidate problems. It is intentionally broad, but it is not a prevalence meta-analysis.

## Main limitations

- The Stack Overflow 2026 survey is large and current, but it is self-reported and its percentages should not be interpreted as causal defect rates.
- Public GitHub issues demonstrate real failure modes but are subject to reporting bias, duplicate reports, incomplete root-cause analysis, and product-specific behavior.
- Security reports differ in task selection, languages, models, scanners, and definitions of a failure. Their absolute percentages are not directly comparable.
- AI coding tools change quickly. Findings from 2025 are retained only when the study design or failure pattern remains informative.
- METR's early-2025 randomized study was deliberately narrow. The authors explicitly caution against generalizing its 19% slowdown result, and their 2026 update reports selection effects in newer measurements.
- The automated GitHub issue collector hit the authenticated Search API rate limit on 2026-10-25 before completing all configured queries. Public issue pages already retrieved remain cited, and the repository records the collector so the corpus can be refreshed later without hiding this blocker.
- Codex CLI is not installed on the active Windows PATH, so official Codex skill-installer behavior could not be tested locally in this session.
- PyPI DNS resolution failed while fetching optional development tools. The project therefore keeps core validation dependency-free and does not claim those optional tools were installed.

## Interpretation rule

The repository uses three evidence labels:

- **strong:** large current survey, repeated independent findings, official limitation plus independent evidence, or strong benchmark evidence.
- **moderate:** credible but narrower study, indirect evidence, or multiple concrete issue reports.
- **issue evidence / context:** useful concrete example or adoption context without a prevalence inference.

The prioritization phase uses evidence strength as one input rather than turning every reported issue into a separate skill.
