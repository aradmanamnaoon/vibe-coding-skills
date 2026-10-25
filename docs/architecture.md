# Architecture

## Principles

The repository separates portable workflow instructions from deterministic support tooling and installation/discovery.

    research evidence
          |
          v
    skill selection/scoring
          |
          v
    skills/<category>/<name>/
      SKILL.md
      scripts/ (optional)
          |
          +---------------------+
          |                     |
          v                     v
    validator/catalog       vibe_skills CLI
                                  |
                                  v
                        target/.agents/skills/

## Source of truth

The skills directory is the only committed distributable skill tree. Installed copies under .agents/skills are generated and ignored by Git. This prevents source/installed copies from drifting.

## Python package

The src/vibe_skills package contains lightweight local tooling:

- catalog.py parses portable scalar front matter and discovers skills;
- validation.py enforces repository structural rules and local references;
- installer.py performs guarded copy/update/remove operations and records managed state;
- cli.py exposes list/search/install/update/remove/validate/doctor and catalog commands.

The runtime uses only the Python standard library. Optional external engineering tools remain integrations, not hidden runtime dependencies.

## Update safety

At installation, the CLI records a SHA-256 digest of the installed skill tree. Update is refused when the installed copy has changed since installation. This makes update non-destructive by default and protects user-local edits.

## Helper scripts

Only checks with a deterministic, reviewable signal get scripts. Scripts:

- do not make source-code fixes by themselves;
- avoid network access unless the skill explicitly requires live data;
- emit structured results suitable for independent review;
- remain standalone inside the installed skill bundle.

## Research linkage

Each SKILL.md records the problem IDs that motivated it. The evidence table keeps sources separate from the instructions so a skill can stay concise while its rationale remains auditable.

