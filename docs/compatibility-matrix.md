# Compatibility matrix

Checked against vendor documentation on 2026-10-25. Documented format support is distinct from repository-specific runtime testing.

| Environment | Documented support | Recommended project destination | Supporting files | Runtime test in this project | Notes |
|---|---|---|---|---|---|
| OpenAI Skills / agent surfaces | yes | environment-specific skill bundle or configured skill directory | yes | structural only; Codex CLI installed but unauthenticated | Core format follows the open Agent Skills model documented by OpenAI. |
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
