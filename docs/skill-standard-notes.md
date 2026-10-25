# Agent Skills implementation notes

Sources checked on 2026-10-25:

- OpenAI Skills: https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI plugin skills: https://developers.openai.com/plugins/build/skills
- Claude Agent Skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude repository skill discovery: https://platform.claude.com/docs/en/managed-agents/skills
- Cursor skills: https://prod.cursor.com/docs/skills
- GitHub Copilot skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

## Portable core

The portable subset used by this repository is deliberately small:

1. one skill directory per skill;
2. exactly one SKILL.md;
3. YAML front matter with name and description;
4. a lowercase hyphenated name matching the skill folder;
5. a description that states both capability and trigger;
6. workflow instructions in the body;
7. optional scripts, references, assets, and examples.

The repository validator also enforces the widely documented 64-character maximum for skill names and 1024-character maximum for descriptions. The project intentionally uses the stricter lowercase-hyphen name subset so one source bundle remains portable across the documented environments above.

The description is a routing contract because supported agents see metadata before loading the full body. Descriptions therefore say when the skill should activate, not merely what topic it covers.

## Repository layout

The skills directory is the distributable source of truth. The CLI copies selected skill bundles into a target such as .agents/skills; generated copies are not committed. This prevents two manually edited trees from drifting.

Category folders are repository organization. Installation flattens the selected bundle so clients do not depend on category-recursion behavior.

## Quality contract

Every published skill defines:

- Purpose
- When to activate
- When not to activate
- Preconditions
- Required inputs
- Workflow
- Relevant tools
- Safety restrictions
- Validation
- Expected output
- Failure handling
- Completion criteria

The repository validator checks front matter, unique names, source directory/name agreement, required sections, and local resource links.

## Scripts

Scripts are preferred when a check is deterministic: parsing files, scanning for a known structural pattern, comparing manifests, or generating a report. A script result is evidence, not permission to make unrelated changes.
