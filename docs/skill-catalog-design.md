# Skill catalog design

The catalog is generated from validated skill metadata instead of maintained as a second hand-edited inventory.

## Fields

Each catalog entry exposes:

- name;
- category;
- description and activation cue;
- source path;
- installation command;
- deterministic helper presence;
- structural validation status;
- compatibility status from the repository-level matrix.

Behavioral or agent-tested status lives in the validation report and is never inferred from the existence of SKILL.md.

## Discovery paths

Users can:

1. browse catalog/SKILLS.md;
2. search from the CLI by name/category/description;
3. list all skills;
4. install one named skill;
5. install a category;
6. install the complete library;
7. update managed skills safely;
8. remove only installer-managed skills;
9. run doctor/validate.

## Naming

Names are lowercase hyphenated stable identifiers. Renaming a skill is treated as a remove/install migration because external prompts and installed paths can reference the name.

