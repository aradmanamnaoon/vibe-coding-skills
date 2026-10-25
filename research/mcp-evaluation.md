# MCP evaluation

Reviewed on 2026-10-25. MCP servers are selected only when they add live state or controlled actions that a local script or CLI cannot provide efficiently.

| Server / integration | Official source | Purpose | Maintenance / license | Auth / cost | Security considerations | Decision and observed status |
|---|---|---|---|---|---|---|
| Chat On Steroids Core | connected host integration | filesystem, terminal, plans, worker orchestration | host-provided | current ChatGPT connection | powerful local mutation/command access; use explicit project roots | Used and functioning in this build |
| OpenAI developer docs MCP | https://developers.openai.com/mcp | current OpenAI docs retrieval | OpenAI-hosted | public remote endpoint documented by OpenAI | remote content remains untrusted data | Recommended optional; Codex CLI absent so no Codex config was modified |
| Official MCP filesystem server | https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem | bounded filesystem tools | active; MIT; npm package | local/free | restrict allowed roots; 2.0.1 includes important path fixes and Windows caveats | Package resolved through npx and argument validation executed; excluded because Core already supplies scoped filesystem access |
| Microsoft Playwright MCP | https://github.com/microsoft/playwright-mcp | browser automation and persistent browser state | active Microsoft OSS | local/free; browser runtime required | browser session may contain credentials; not a security boundary | npx package successfully executed --help; optional for browser flows |
| GitHub access | https://github.com/github/github-mcp-server | repos, issues, PRs, Actions | official GitHub project | GitHub auth; API rate limits | use least-privilege repository permissions | Host GitHub/gh access functioning; repo creation/push worked; Search API rate limit was observed |
| Official MCP Registry | https://registry.modelcontextprotocol.io/ | server discovery and metadata | official community registry | public discovery | a registry listing is provenance data, not a trust decision | Used for discovery only |

## Excluded from automatic installation

The project does not install a large MCP bundle as a side effect of skill installation.

1. The active host already exposes filesystem, terminal, and GitHub capabilities.
2. Duplicate servers expand startup cost and permission surface.
3. The research corpus includes real MCP startup/retry/process-proliferation failures.
4. Credential-bearing servers require user-specific least-privilege configuration.
5. Codex CLI is absent from PATH, so Codex MCP configuration could not be validated end-to-end.

The example configuration therefore documents a small optional profile rather than claiming every integration was installed and connected.

