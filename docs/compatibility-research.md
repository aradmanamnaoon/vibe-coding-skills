# Compatibility research

Checked on 2026-10-25. Supported means the vendor documents Agent Skills support; it does not mean every skill in this repository has been behaviorally tested on that product.

| Environment | Documented skill support | Discovery path relevant here | Scripts/resources | Behavioral status for this repository |
|---|---|---|---|---|
| OpenAI agents / APIs | Yes; compatible with the open Agent Skills standard | skill bundles and configured capability directories | Yes | Structural format aligned; Codex CLI behavioral test not executed because codex is not on PATH |
| Claude Code | Yes | .claude/skills for project skills and ~/.claude/skills for personal skills | Yes | Portable SKILL.md format aligned; repository-specific discovery path requires an install adapter; runtime behavioral test not executed |
| Cursor | Yes | .agents/skills and .cursor/skills; also reads Claude/Codex skill directories | Yes | Structural format aligned; runtime behavioral test not executed |
| GitHub Copilot | Yes across cloud agent, code review, CLI, app, and VS Code agent mode | .agents/skills, .github/skills, and .claude/skills depending on surface | Yes | Structural format aligned; runtime behavioral test not executed |
| Other Agent Skills implementations | Potentially | implementation-specific | standard permits resources | Unverified until tested |

## Design implications

- Avoid product-only commands in the core workflow.
- Describe capabilities such as running the repository test command rather than assuming a particular tool name.
- Put product-specific adapters in references only when required.
- Treat MCP as optional unless the workflow genuinely requires live external state.
- Never claim a browser, package registry, CI platform, or production service was checked unless a compatible tool actually returned evidence.

## Official references

- OpenAI Skills: https://developers.openai.com/api/docs/guides/tools-skills
- Claude Agent Skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude repository skill discovery: https://platform.claude.com/docs/en/managed-agents/skills
- Cursor Agent Skills: https://cursor.com/docs/skills
- GitHub Copilot agent skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

## Browser automation

Microsoft's current Playwright MCP documentation says coding agents may benefit from Playwright CLI exposed through skills because it can be more token-efficient than loading MCP tool schemas and accessibility trees. MCP remains useful for persistent browser state and exploratory loops. UI skills in this repository therefore define the required evidence and accept either a supported CLI/browser harness or MCP-backed browser, while recording not-executed status when neither is available.
