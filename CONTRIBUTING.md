# Contributing

Contributions should improve a concrete developer workflow, evidence base, deterministic helper, compatibility adapter, or validation fixture.

## Before proposing a new skill

1. Search `catalog/SKILLS.md` for overlapping workflows.
2. Link the proposal to an observed problem in `research/` or provide new traceable evidence.
3. Explain why a standalone skill is better than extending an existing skill or using an existing tool.
4. Define an activation trigger, boundaries, expected output, failure handling, and testable completion criteria.

## Local validation

From the repository root:

    $env:PYTHONPATH = "src"   # PowerShell
    py -m unittest discover -s tests -v
    py -m vibe_skills validate
    py -m vibe_skills catalog
    py scripts/check_docs.py .
    py skills/security/secret-leakage-detector/scripts/scan_secrets.py .

On macOS/Linux, use `PYTHONPATH=src python ...` for the package commands.

## Skill requirements

Use lowercase hyphenated names. Every SKILL.md must include the operational sections enforced by the validator. Keep deterministic tasks in small reviewed scripts when that makes results more reproducible. Do not vendor third-party skill content without a license review and required attribution.

## Pull requests

Keep changes focused. Explain the problem and resulting behavior, include relevant evidence links, list validation that actually ran, and identify any environment-dependent checks that remain unexecuted.

