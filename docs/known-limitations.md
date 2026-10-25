# Known limitations

- Codex CLI was not available on the active Windows PATH, so native Codex skill installation and agent-driven behavioral tests were not executed.
- The available host worker path did not provide a usable deterministic agent benchmark session. No failed startup is counted as validation.
- PyPI DNS resolution failed while resolving optional development tools during this run. Core runtime and validation therefore remain standard-library only.
- GitHub Search API rate limiting interrupted three configured issue searches. The curated evidence corpus records the limitation and does not infer prevalence from issue counts.
- Raw third-party issue bodies are not retained in the current repository. The refresh script stores metadata-only output in an ignored local checkpoint.
- Five skills have deterministic helper scripts with fixture tests. The remaining skills are instruction workflows whose full behavioral value requires agent-level experiments.
- Browser-dependent UI skills were not executed against a live sample application in this repository. They define evidence requirements but remain agent/browser unverified.
- Package-vulnerability freshness, production smoke tests, hosted CI diagnosis, and other live-service checks require target-system access and cannot be guaranteed offline.
- Compatibility rows describe vendor-documented skill support. They do not imply every workflow has been tested on every listed agent.
- Research percentages come from heterogeneous sources and are not directly comparable defect rates.
