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
| Codex CLI | Not found on PATH |
| pytest | Not installed globally |

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

Codex CLI is unavailable on PATH, so its official skill-installer cannot be invoked from this host as currently configured. Any third-party skill or MCP installation will be documented separately with provenance and an observed connectivity status; unavailable credential-dependent integrations will remain optional.

