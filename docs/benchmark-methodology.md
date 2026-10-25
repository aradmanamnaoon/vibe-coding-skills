# Benchmark methodology

## Current release scope

The initial benchmark is deliberately limited to deterministic helper behavior and repository tooling. It does not report an agent-with-skill versus agent-without-skill improvement because no controlled compatible-agent harness was available on the active host.

## Fixed fixture principles

Each helper test uses a temporary repository-like directory with a seeded target condition and an independently asserted expected result:

1. secret scanner: seed a credential-shaped value and verify a finding is returned without exposing the value;
2. skipped-test scanner: seed Python and JavaScript skip constructs and verify both frameworks are detected;
3. dead-feature scanner: seed an empty click handler and implementation marker and verify both signals are detected;
4. environment-key discovery: seed Python and JavaScript environment reads and verify exact key-to-file mapping;
5. Python import-cycle scanner: seed a two-module cycle and verify the cycle is returned.

Installer fixtures independently exercise traversal rejection, managed-only removal, update of an unchanged skill, and refusal to overwrite a locally modified installed skill.

## Metrics

The deterministic release gate records fixture pass/fail counts. Precision, recall, token usage, tool-call counts, elapsed agent time, and human intervention are intentionally not reported until a controlled agent harness can collect comparable control and treatment runs.

## Future agent comparison

An agent benchmark must pin the repository snapshot, model/configuration, prompt, fixture, tool permissions, and acceptance tests. Control and skill conditions must use the same task and independent verifier. See ROADMAP.md for the behavioral-harness phase.
