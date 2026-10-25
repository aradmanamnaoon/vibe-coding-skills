---
name: authentication-security-auditor
description: Audit authentication flows for server-side identity verification, session/token handling, and bypass paths. Use when login, session, OAuth, API-key, or protected-route code changes.
---

# Purpose

Verify that protected operations establish trustworthy identity on the server side.

# When to activate

Authentication code, protected routes, session middleware, tokens, or identity providers are added or changed.

# When not to activate

A static/public endpoint has no identity requirement and authentication is outside the change surface.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Auth architecture and provider
- Protected entry points
- Session/token configuration
- Relevant tests

# Workflow

1. Map every protected entry point to the component that establishes authenticated identity.
2. Trace credentials/tokens from receipt through validation: signature or session lookup, issuer/audience/expiry, revocation/session state where applicable.
3. Verify client-side state is never the sole gate for a protected server action.
4. Check session fixation, logout/invalidation, cookie flags, CSRF where relevant, and safe failure defaults.
5. Test unauthenticated, malformed/expired credential, valid credential, and provider-failure cases.
6. Confirm sensitive error responses do not disclose credential/token internals.
7. Record provider-specific assumptions and links to configuration evidence.

# Relevant tools

Route search, auth middleware, integration tests, provider docs/config when accessible.

# Safety restrictions

Use synthetic credentials in tests; never paste or replay production sessions/tokens.

# Validation

- Unauthenticated and invalid identities cannot reach protected effects.
- Valid identities still work through the intended flow.
- Failure paths deny access by default.

# Expected output

- Authentication boundary map
- Bypass findings
- Test evidence
- Provider/config assumptions

# Failure handling

If provider configuration is inaccessible, validate code-level enforcement and mark provider-side controls unverified.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P014. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
