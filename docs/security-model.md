# Security model

## Trust boundaries

The repository contains instructions and local deterministic scripts. Installing a skill copies files; it does not automatically:

- install an MCP server;
- download or execute remote code;
- request credentials;
- broaden filesystem/network permissions;
- modify an agent's global configuration.

## Installer protections

- destination skill names are resolved as direct children of the explicit destination;
- traversal outside the destination is rejected;
- existing destinations are never overwritten by install;
- remove operates only on skills recorded as installer-managed;
- update requires the installed tree digest to match its recorded installation digest;
- update stages a new copy and keeps a recoverable backup during replacement.

## Helper-script policy

Bundled helpers are standard-library Python and operate on explicit local paths. Security scanners redact secret values from structured findings. Helpers report signals and return nonzero status when appropriate; they do not make hidden source changes.

## Supply chain

Core runtime has no third-party Python dependency. Optional MCP/browser/security tools are documented separately with provenance and are not fetched as an installation side effect.

## Prompt injection

Research content, issue text, web pages, source comments, and MCP-returned text are data rather than authority. Skills that use external content preserve the user's task and platform policies and must not accept embedded instructions to expose credentials or expand permissions.

## Reporting vulnerabilities

See SECURITY.md for coordinated reporting. Do not open public proof-of-concept issues containing real secrets or exploitable private-system details.

