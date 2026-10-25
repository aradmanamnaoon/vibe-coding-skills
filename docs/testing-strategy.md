# Testing strategy

## Test layers

### Structural

Every skill is checked for:

- valid front matter;
- required name/description;
- unique name;
- directory/name agreement;
- required operational sections;
- resolvable local references.

### Installer and CLI

Unit tests cover:

- discovery and malformed metadata;
- dry-run behavior;
- existing-install conflicts;
- path traversal rejection;
- managed-only removal;
- update of unchanged managed skills;
- refusal to overwrite locally modified installed skills.

### Deterministic helper fixtures

Current helpers have seeded fixtures for:

- secret patterns while verifying matched values are not emitted;
- skipped or disabled tests across multiple frameworks;
- UI placeholder/no-op signals;
- Python and JavaScript environment-key discovery;
- Python import cycles.

### Functional skill evaluation

A full behavioral evaluation requires executing a compatible coding agent on fixed fixture repositories. The active host does not expose Codex CLI, and worker-agent startup failed during this run. The initial release therefore distinguishes:

- structurally validated;
- helper-functionally tested;
- workflow fixture reviewed;
- agent-tested only when an actual compatible agent run and independent verification were observed.

Structural validation must never be converted into an agent-tested claim.

## Baseline experiments

Future agent benchmarks use the same repository snapshot, prompt, model/configuration, fixture, and acceptance tests for control and skill conditions. Report task success, defect detection, false positives, regressions, tool calls, elapsed time, and intervention count only when the harness can record them comparably.

