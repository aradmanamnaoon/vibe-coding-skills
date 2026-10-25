# Existing skill ecosystems

Reviewed on 2026-10-25. The goal is to avoid publishing thin copies of workflows that an established ecosystem already provides well.

| Source | What exists | Strengths | Limits here | Redistribution decision | Source |
|---|---|---|---|---|---|
| OpenAI Agent Skills | Portable SKILL.md bundles with optional scripts, references, and assets | Current open-standard alignment; progressive disclosure | Official examples are focused rather than a broad SDLC audit library | Link and integrate; do not copy examples | https://developers.openai.com/api/docs/guides/tools-skills |
| OpenAI plugin skills | Workflow layer around MCP tools | Clear separation between live tools and procedural knowledge | Plugin packaging is broader than this standalone skill repository | Follow design guidance; do not require MCP when local tooling is enough | https://developers.openai.com/plugins/build/skills |
| Cursor built-in skills | Automation, review, security review, shell, split-to-PRs, hooks, skill creation, and more | Mature product integration and manual/automatic discovery | Product-specific built-ins are not portable repository content | Complement rather than duplicate | https://prod.cursor.com/docs/skills |
| GitHub Copilot Agent Skills | Repository/user-level skills with SKILL.md plus scripts/resources | Supports cloud agent, code review, CLI, app, and VS Code agent mode | Tool availability differs by Copilot surface | Build portable content; document unverified behavior | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills |
| Microsoft Playwright MCP / CLI skills | Browser automation over MCP plus a CLI-and-skills path | Real browser verification; maintainers document MCP versus CLI tradeoffs | Browser runtime is external and MCP can add context overhead | Integrate optionally | https://github.com/microsoft/playwright-mcp |
| Local managed skills on this host | The managed /skills root exposed an unrelated psylex directory | Confirms a managed skill root exists | No relevant general-purpose vibe-coding collection was available there | Do not copy unrelated content | local observation |

## Duplication decisions

Generic actions such as "review code", "run a shell command", or "create a skill" are already normal agent/product capabilities. This repository instead focuses on evidence-backed failure patterns with explicit completion evidence, for example:

- distinguish a completion claim from a verified feature;
- detect a no-progress debugging or tool loop while allowing repeated actions that still make measurable progress;
- check whether visible UI controls have real handlers and side effects;
- ground package/version changes against actual project or registry state;
- preserve unrelated working behavior while an agent edits an established project;
- reconcile multi-agent branches for semantic conflict, not only clean Git merges;
- check MCP startup cost, retry behavior, failure isolation, and permission scope.

## Reuse policy

Third-party skills are referenced rather than vendored unless a later contribution includes a license review and required attribution. Original skills in this repository use the MIT license. External executable helpers are never downloaded or run as a hidden side effect of installing a skill.
