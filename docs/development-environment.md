# Development environment

Verified on 2026-10-25 on the active Windows host.

| Tool | Observed state |
|---|---|
| Git | 2.54.0.windows.1 |
| GitHub CLI | 2.102.0 |
| GitHub authentication | Authenticated as aradmanamnaoon; token value is not recorded in this repository |
| Python | py resolves to Python 3.10.10; bare python is intercepted by the Microsoft Store alias |
| pip | 22.3.1 initially; project virtual environment upgraded pip to 26.2.2 |
| Node.js | 24.17.0 |
| npm / npx | 11.13.0 |
| pnpm | 12.15.0 via Corepack |
| Docker | 29.8.1 |
| Codex CLI | 0.164.0 from the official `@openai/codex` npm package; installed globally and callable |
| pytest | Not installed globally |
| Playwright MCP package | `npx -y @playwright/mcp@latest --help` executed successfully |
| MCP filesystem package | `@modelcontextprotocol/server-filesystem@2.0.1` resolved and launched far enough to validate its path argument; no client handshake is claimed |

## Project-local environment

The repository uses .venv for local Python tooling and keeps it out of Git. The runtime package is intentionally standard-library only.

An attempt to install the optional development bundle pytest, PyYAML, ruff, and bandit reached a DNS failure at files.pythonhosted.org while resolving ruff. This is recorded as an environment limitation, not as a successful installation.

The repository's core tests use the standard-library unittest runner, so they do not require PyPI access:

~~~powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
~~~

## Skills and MCP state

The managed /skills root exposed to this session currently contains one unrelated psylex directory. The host session provides the Chat On Steroids Core integration used for filesystem, terminal, plan, and worker operations.

Codex CLI 0.164.0 is installed and callable. `codex login status` reports `Not logged in`, and `codex doctor` reports that no Codex credentials were found. HTTPS endpoints were reachable during doctor checks, while the websocket probe returned HTTP 401 because bearer/basic authentication was absent. The configuration loaded and local state-database integrity checks passed.

`codex plugin list` and `codex mcp list` were inspected. Installed/enabled plugins included the OpenAI primary-runtime document/PDF/spreadsheet/presentation/template plugins and bundled browser/computer-use/code-review/visualization tooling. Codex MCP inventory showed `cua_repl` and `node_repl` enabled, with an optional warning that `node_repl` lacked `CODEX_WINDOWS_REGISTERED_CORE`. These are inventory/configuration observations only; model-driven behavior is not claimed while Codex is unauthenticated.

Three optional Codex plugins were reviewed but deliberately not installed: `codex-security` because of its broad credential surface and proprietary license; `openai-developers` because it is OpenAI-API-specific and unnecessary for this repository; and `superpowers` because it substantially overlaps this library. This follows the project's least-privilege and non-redundancy policy rather than maximizing plugin count.

The authenticated GitHub Search API was exercised during research. Bulk collection observed 537 unique issue records before rate limiting interrupted three configured searches. The current collector retains metadata only in an ignored local checkpoint.

