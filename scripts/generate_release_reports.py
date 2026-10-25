from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOG = ROOT / "catalog" / "skills.json"


def load_catalog() -> list[dict[str, object]]:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("catalog/skills.json must contain a list")
    return payload


def write_validation_report(rows: list[dict[str, object]]) -> None:
    total = len(rows)
    structural = sum(bool(row["structurally_valid"]) for row in rows)
    helper_tested = sum(bool(row["has_scripts"]) for row in rows)
    lines = [
        "# Validation report",
        "",
        "Generated from catalog/skills.json and the observed validation strategy on 2026-10-25.",
        "",
        "## Summary",
        "",
        f"- Implemented skills: **{total}**",
        f"- Structurally validated: **{structural}**",
        f"- Skills with fixture-tested deterministic helpers: **{helper_tested}**",
        "- Agent-driven behavioral tests: **0**",
        f"- Skills without agent-level execution evidence: **{total}**",
        "",
        "The active Windows host did not expose Codex CLI, and the attempted parallel ChatGPT worker sessions failed to report back. Those environmental facts are recorded as limitations rather than being converted into inferred agent-test results.",
        "",
        "## Per-skill status",
        "",
        "| Skill | Category | Implemented | Structural | Helper functional | Agent tested | Security status |",
        "|---|---|:---:|:---:|:---:|:---:|---|",
    ]
    for row in rows:
        helper = "yes" if row["has_scripts"] else "n/a"
        structural_status = "yes" if row["structurally_valid"] else "no"
        lines.append(
            f"| {row['name']} | {row['category']} | yes | {structural_status} | {helper} | no | safety section validated; no independent product security certification |"
        )
    lines.extend(
        [
            "",
            "## What structural validation proves",
            "",
            "Structural validation checks metadata, names, descriptions, directory identity, required operational sections, duplicate descriptions, and local resource references. It does not prove an agent will follow the workflow correctly.",
            "",
            "## What helper functional testing proves",
            "",
            "The five helper-backed skills have deterministic fixture tests for secret redaction, skipped-test discovery, placeholder signals, environment-variable discovery, and Python import cycles. These tests exercise the helper code, not the full language-model workflow.",
        ]
    )
    (DOCS / "validation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_compatibility_matrix() -> None:
    text = """# Compatibility matrix

Checked against vendor documentation on 2026-10-25. Documented format support is distinct from repository-specific runtime testing.

| Environment | Documented support | Recommended project destination | Supporting files | Runtime test in this project | Notes |
|---|---|---|---|---|---|
| OpenAI Skills / agent surfaces | yes | environment-specific skill bundle or configured skill directory | yes | not executed with Codex CLI | Core format follows the open Agent Skills model documented by OpenAI. |
| Claude Code | yes | .claude/skills/<name>/ | yes | not executed | Requires copying each selected source bundle into Claude's discovery root. |
| Cursor | yes | .agents/skills/<name>/ or .cursor/skills/<name>/ | yes | not executed | Cursor also documents compatibility discovery for Claude and Codex skill roots. |
| GitHub Copilot | yes | .agents/skills/<name>/, .github/skills/<name>/, or .claude/skills/<name>/ depending on surface | yes | not executed | Copilot documents skills across cloud agent, code review, CLI, app, and IDE agent mode. |
| Other Agent Skills implementations | implementation-specific | implementation-specific | potentially | not executed | Treat as unverified until the target implementation is tested. |

## Official references

- OpenAI: https://developers.openai.com/api/docs/guides/tools-skills
- Claude: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude repository discovery: https://platform.claude.com/docs/en/managed-agents/skills
- Cursor: https://cursor.com/docs/skills
- GitHub Copilot: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

## Installation model

The repository keeps skills/ as the source of truth. The built-in installer targets .agents/skills by default because that location is documented by Cursor and GitHub Copilot and is a portable convention. Product-specific destinations can be selected with --destination. The repository does not claim that one discovery root is native to every agent.
"""
    (DOCS / "compatibility-matrix.md").write_text(text, encoding="utf-8")


def write_benchmark_methodology() -> None:
    text = """# Benchmark methodology

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
"""
    (DOCS / "benchmark-methodology.md").write_text(text, encoding="utf-8")


def write_known_limitations() -> None:
    text = """# Known limitations

- Codex CLI was not available on the active Windows PATH, so native Codex skill installation and agent-driven behavioral tests were not executed.
- Attempts to start parallel ChatGPT workers through the available host integration did not return usable worker sessions. No worker result is counted as validation.
- PyPI DNS resolution failed while resolving optional development tools during this run. Core runtime and validation therefore remain standard-library only.
- GitHub Search API rate limiting interrupted three configured issue searches. The curated evidence corpus records the limitation and does not infer prevalence from issue counts.
- Raw third-party issue bodies are not retained in the current repository. The refresh script stores metadata-only output in an ignored local checkpoint.
- Five skills have deterministic helper scripts with fixture tests. The remaining skills are instruction workflows whose full behavioral value requires agent-level experiments.
- Browser-dependent UI skills were not executed against a live sample application in this repository. They define evidence requirements but remain agent/browser unverified.
- Package-vulnerability freshness, production smoke tests, hosted CI diagnosis, and other live-service checks require target-system access and cannot be guaranteed offline.
- Compatibility rows describe vendor-documented skill support. They do not imply every workflow has been tested on every listed agent.
- Research percentages come from heterogeneous sources and are not directly comparable defect rates.
"""
    (DOCS / "known-limitations.md").write_text(text, encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    rows = load_catalog()
    write_validation_report(rows)
    write_compatibility_matrix()
    write_benchmark_methodology()
    write_known_limitations()
    print(f"Generated release reports for {len(rows)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
