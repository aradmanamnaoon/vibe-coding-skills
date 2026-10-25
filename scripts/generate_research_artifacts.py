from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"


SOURCES = {
    "SO-DISRUPTION": {
        "title": "Stack Overflow Developer Survey 2026 — AI-caused business disruptions",
        "url": "https://survey.stackoverflow.co/2026/technology/data/disruption",
        "date": "2026",
        "kind": "survey",
        "notes": "n=13,648. Reports categories of AI mistakes that cost respondents or teams the most time.",
    },
    "SO-AI-DATA": {
        "title": "Stack Overflow Developer Survey 2026 — AI data",
        "url": "https://survey.stackoverflow.co/2026/ai/data",
        "date": "2026",
        "kind": "survey",
        "notes": "Workflow adoption, usefulness, satisfaction, switching, memory control, and organizational AI practices.",
    },
    "SO-TRUST": {
        "title": "Stack Overflow Developer Survey 2026 — Trust in AI tools",
        "url": "https://survey.stackoverflow.co/2026/ai/data/ai-trust",
        "date": "2026",
        "kind": "survey",
        "notes": "n=14,304. Trust is strongly conditional on easy verification.",
    },
    "SO-COMPLEX": {
        "title": "Stack Overflow Developer Survey 2026 — Complex task performance",
        "url": "https://survey.stackoverflow.co/2026/ai/data/ai-complex",
        "date": "2026",
        "kind": "survey",
        "notes": "n=14,341. Only a minority rate AI as very good at complex tasks.",
    },
    "SO-NEXT": {
        "title": "Stack Overflow Developer Survey 2026 — Validation after AI answers",
        "url": "https://survey.stackoverflow.co/2026/ai/data/ai-work-next",
        "date": "2026",
        "kind": "survey",
        "notes": "n=13,162. Running locally, codebase comparison, and test/security inspection are common verification steps.",
    },
    "SO-KNOWLEDGE": {
        "title": "Stack Overflow Developer Survey 2026 — Knowledge data",
        "url": "https://survey.stackoverflow.co/2026/knowledge/data",
        "date": "2026",
        "kind": "survey",
        "notes": "Agent task delegation plus cost and usage-limit behavior.",
    },
    "VERACODE-2026": {
        "title": "Veracode 2026 GenAI Code Security Report",
        "url": "https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/",
        "date": "2026",
        "kind": "security study",
        "notes": "Reports security-pass rates across models and languages; best observed model still fails a material share of security tasks.",
    },
    "VERACODE-2025": {
        "title": "Veracode 2025 GenAI Code Security Report",
        "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/",
        "date": "2025",
        "kind": "security study",
        "notes": "Reports 45% of tested generated-code cases introducing a detectable OWASP Top 10 vulnerability.",
    },
    "ARXIV-GH-SEC": {
        "title": "Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories",
        "url": "https://arxiv.org/abs/2510.26103",
        "date": "2025-10-30",
        "kind": "research paper",
        "notes": "Analyzes 7,703 AI-attributed files and 4,241 CWE instances using CodeQL.",
    },
    "ARXIV-SECURE-CODING": {
        "title": "Secure Coding with AI, From Creation to Inspection",
        "url": "https://arxiv.org/abs/2504.20814",
        "date": "2025-04-29",
        "kind": "research paper",
        "notes": "Manual analysis found model-introduced vulnerabilities and incomplete detection/fixing performance.",
    },
    "DORA-2025": {
        "title": "2025 DORA Report announcement",
        "url": "https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report",
        "date": "2025",
        "kind": "industry research",
        "notes": "AI adoption correlated positively with throughput/product performance but negatively with delivery stability; testing and feedback loops matter.",
    },
    "METR-2025": {
        "title": "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity",
        "url": "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/",
        "date": "2025-07-10",
        "kind": "randomized field study",
        "notes": "In this specific sample, AI use increased task completion time by 19%; authors warn against overgeneralization.",
    },
    "METR-2026": {
        "title": "METR update on developer productivity experiment design",
        "url": "https://metr.org/blog/2026-02-24-uplift-update/",
        "date": "2026-02-24",
        "kind": "research update",
        "notes": "Reports selection effects and weak evidence of improved speedup, underscoring measurement difficulty.",
    },
    "SONATYPE-2026": {
        "title": "2026 Sonatype Software Supply Chain Report — Grounded AI Agents",
        "url": "https://www.sonatype.com/state-of-the-software-supply-chain/2026/ai-agents",
        "date": "2026",
        "kind": "supply-chain study",
        "notes": "Across 36,870 upgrade recommendations, 27.76% referenced nonexistent versions before registry grounding.",
    },
    "GH-COPILOT-LIMITS": {
        "title": "GitHub Copilot Agents — responsible use and limitations",
        "url": "https://docs.github.com/en/copilot/responsible-use/agents",
        "date": "2026",
        "kind": "official documentation",
        "notes": "Documents missed quality problems and hallucinated false positives; recommends human review.",
    },
    "OPENAI-PROMPT-INJECTION": {
        "title": "OpenAI — Understanding prompt injections",
        "url": "https://openai.com/safety/prompt-injections/",
        "date": "2026",
        "kind": "official security guidance",
        "notes": "Describes third-party content misleading tool-using agents as an evolving security challenge.",
    },
    "OPENAI-SKILLS": {
        "title": "OpenAI Developers — Build skills",
        "url": "https://developers.openai.com/plugins/build/skills",
        "date": "2026",
        "kind": "official documentation",
        "notes": "Defines focused skill structure, trigger descriptions, workflow boundaries, supporting scripts, testing, and MCP dependencies.",
    },
    "OPENAI-PLUGINS": {
        "title": "OpenAI Developers — Package plugins",
        "url": "https://developers.openai.com/plugins/build/plugins",
        "date": "2026",
        "kind": "official documentation",
        "notes": "Documents portable plugin layout, skills directory, MCP configuration, path rules, and Codex compatibility layout.",
    },
    "GH-COPILOT-CUSTOM": {
        "title": "GitHub Docs — Comparing Copilot customization features",
        "url": "https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations",
        "date": "2026",
        "kind": "official documentation",
        "notes": "Distinguishes agent skills, instructions, MCP tools, hooks, subagents, custom agents, and plugins.",
    },
    "ISSUE-CODEX-LOOP": {
        "title": "Codex Desktop enters an infinite loop of repeated tool calls",
        "url": "https://github.com/openai/codex/issues/42444",
        "date": "2026-09-03",
        "kind": "public bug report",
        "notes": "Reports repeated tool calls and failure to progress.",
    },
    "ISSUE-CODEX-MCP-STALL": {
        "title": "Codex Desktop app-server stalls with MCP startup load",
        "url": "https://github.com/openai/codex/issues/56379",
        "date": "2026-10-23",
        "kind": "public bug report",
        "notes": "Reports queue saturation, many descendant processes, and slow/failing MCP startup interactions.",
    },
    "ISSUE-CODEX-SPAWN": {
        "title": "Codex Windows bundled plugin causes cmd/node spawn loop",
        "url": "https://github.com/openai/codex/issues/32690",
        "date": "2026-07-13",
        "kind": "public bug report",
        "notes": "Reports plugin/MCP startup retry behavior causing process proliferation.",
    },
    "ISSUE-CODEX-STALL": {
        "title": "Codex Windows tool calls can stall for hours",
        "url": "https://github.com/openai/codex/issues/47910",
        "date": "2026-09-24",
        "kind": "public bug report",
        "notes": "Reports root turns waiting on tool results without progress and recovery problems.",
    },
    "ISSUE-ROO-LOOP": {
        "title": "Roo Code loop detection false positives on MCP tools",
        "url": "https://github.com/RooCodeInc/Roo-Code/issues/9502",
        "date": "2025-11-22",
        "kind": "public bug report",
        "notes": "Reports legitimate repeated MCP calls incorrectly flagged as a stuck loop.",
    },
    "ISSUE-AIDER-TESTS": {
        "title": "Aider polyglot benchmark leaves tests skipped",
        "url": "https://github.com/Aider-AI/aider/issues/5898",
        "date": "2026-10-23",
        "kind": "public bug report",
        "notes": "Reports test fixtures remaining disabled/skipped, relevant to benchmark and test-integrity auditing.",
    },
    "ISSUE-CLINE-CONTEXT": {
        "title": "Cline session not found issue",
        "url": "https://github.com/cline/cline/issues/12240",
        "date": "2026-07-12",
        "kind": "public bug report",
        "notes": "Reports session continuity failure.",
    },
    "ISSUE-ROO-RETRY": {
        "title": "Roo Code structural API error retries forever",
        "url": "https://github.com/RooCodeInc/Roo-Code/issues/11762",
        "date": "2026-02-26",
        "kind": "public bug report",
        "notes": "Reports missing circuit breaker and repeated retries with corrupted history.",
    },
}


PROBLEMS = [
    ("P001", "Plausible but wrong code", "code-quality", "all AI-assisted developers", "critical", "strong", "language-model plausibility without executable verification", "tests, static analysis, code review", "feature-verification-agent", "turn completion claims into executable checks", "cannot prove behavior not represented by available tests or observability", "seed fixtures with correct and subtly incorrect implementations; measure detection precision/recall", ["SO-DISRUPTION", "GH-COPILOT-LIMITS"]),
    ("P002", "Hallucinated packages, versions, and configuration", "dependencies", "all AI-assisted developers", "high", "strong", "stale model knowledge and ungrounded package guesses", "package registries, lockfiles, dependency resolvers", "dependency-grounding-auditor", "verify names and versions against real project/registry state", "offline environments can limit registry verification", "fixtures with nonexistent and valid dependencies; assert false-positive rate", ["SO-DISRUPTION", "SONATYPE-2026"]),
    ("P003", "Outdated or nonexistent APIs", "code-quality", "all AI-assisted developers", "high", "strong", "training-data staleness and incomplete library context", "official docs, type checkers, compilation", "api-contract-grounder", "force documentation and executable API verification", "documentation may lag prerelease APIs", "compile/type-check fixtures across pinned dependency versions", ["SO-DISRUPTION", "GH-COPILOT-LIMITS"]),
    ("P004", "Missing codebase context", "agent-reliability", "all AI-assisted developers", "high", "strong", "context-window limits, indexing gaps, ignored files", "repository search, targeted context, architecture docs", "context-coverage-auditor", "identify unseen callers, configs, tests, and contracts before edits", "cannot inspect inaccessible or ignored content", "fixtures with hidden cross-file dependencies and ignored files", ["SO-DISRUPTION", "ISSUE-CLINE-CONTEXT"]),
    ("P005", "Generated changes are hard to review", "maintainability", "teams using AI-generated patches", "high", "strong", "oversized diffs, mixed concerns, unnecessary rewrites", "small commits, code review, diff tooling", "reviewability-guard", "reduce patch size and isolate concerns", "some large migrations are inherently broad", "compare diff size/cohesion before and after skill guidance", ["SO-DISRUPTION", "GH-COPILOT-LIMITS"]),
    ("P006", "Poor debugging paths", "debugging", "developers debugging with agents", "high", "strong", "guessing fixes before reproduction or evidence collection", "logs, debuggers, tests, bisecting", "root-cause-debugger", "prioritize reproducible evidence and root cause", "intermittent failures can remain hard to reproduce", "fault-injected fixtures with misleading symptoms", ["SO-DISRUPTION", "SO-AI-DATA"]),
    ("P007", "Infinite or circular agent loops", "agent-reliability", "agent users", "high", "strong", "missing progress criteria and retry circuit breakers", "iteration limits, checkpoints, manual cancellation", "loop-breaker", "detect no-progress repetition and change strategy or stop", "repeated calls can be legitimate when measurable progress exists", "simulate repeated identical and progress-making tool calls", ["ISSUE-CODEX-LOOP", "ISSUE-ROO-RETRY", "ISSUE-ROO-LOOP"]),
    ("P008", "Symptom patching instead of root-cause fixes", "debugging", "developers debugging with agents", "high", "moderate", "local patch bias and insufficient causal tracing", "root-cause analysis, regression tests", "root-cause-debugger", "tie fixes to a falsifiable failure mechanism", "root causes may span external services", "multi-layer fixture where superficial patch leaves failing invariant", ["SO-DISRUPTION", "DORA-2025"]),
    ("P009", "Regressions introduced by fixes", "testing", "all AI-assisted developers", "critical", "strong", "narrow validation and broad edits", "regression suites, CI, canary testing", "regression-detector", "compare pre/post behavior and guard untouched flows", "legacy tests may be incomplete", "known regression fixtures plus baseline test comparison", ["DORA-2025", "SO-NEXT"]),
    ("P010", "Unnecessary full-project rewrites", "agent-reliability", "developers using autonomous agents", "high", "moderate", "scope loss and preference for internally consistent regeneration", "git diffs, change plans, file ownership", "existing-work-preservation", "minimize edit surface and preserve working code", "some migrations legitimately require wide changes", "fixtures with protected unrelated modules and required narrow fix", ["SO-COMPLEX", "GH-COPILOT-LIMITS"]),
    ("P011", "Logs and stack traces are ignored", "debugging", "developers debugging with agents", "high", "moderate", "premature hypothesis generation", "logging, tracing, debuggers", "evidence-first-debugger", "extract failing frame and evidence before edits", "logs can be incomplete or misleading", "fixtures where error message uniquely identifies root cause", ["SO-AI-DATA", "SO-NEXT"]),
    ("P012", "Failure is not reproduced before editing", "debugging", "developers debugging with agents", "high", "strong", "pressure to act immediately and missing test harness", "minimal reproduction, failing tests", "reproduction-builder", "establish a stable red test before a fix", "environment-only failures may resist local reproduction", "fixtures requiring minimal reproducer creation", ["SO-NEXT", "METR-2025"]),
    ("P013", "Secrets are exposed in code or commits", "security", "all software builders", "critical", "strong", "hardcoded credentials and unsafe debugging output", "secret scanners, env files, key rotation", "secret-leakage-detector", "detect likely secrets before commit/push", "entropy heuristics can create false positives", "fixtures with synthetic secrets and safe lookalikes", ["VERACODE-2026", "OPENAI-PROMPT-INJECTION"]),
    ("P014", "Authentication is incomplete or bypassable", "security", "web/backend developers", "critical", "strong", "client-side-only checks and missing server verification", "auth middleware, integration tests, threat modeling", "authentication-security-auditor", "trace authentication on every protected entry point", "provider-specific auth semantics vary", "fixtures with missing middleware and forged identity paths", ["VERACODE-2025", "ARXIV-GH-SEC"]),
    ("P015", "Authorization boundaries are incorrect", "security", "web/backend developers", "critical", "strong", "confusing identity with permission and missing object-level checks", "RBAC/ABAC tests, policy engines", "authorization-boundary-auditor", "verify per-resource and per-action authorization", "business rules require domain context", "multi-user fixtures with horizontal/vertical privilege escalation", ["VERACODE-2026", "ARXIV-SECURE-CODING"]),
    ("P016", "Unsafe database and command queries", "security", "backend developers", "critical", "strong", "string interpolation and missing parameterization", "ORM parameterization, SAST, prepared statements", "injection-risk-auditor", "find controllable input reaching interpreters", "dynamic query builders can be hard to reason about statically", "SQL/command injection fixtures with tainted input", ["VERACODE-2025", "ARXIV-GH-SEC"]),
    ("P017", "Missing server-side input validation", "security", "backend/API developers", "high", "strong", "trust in client validation and schema drift", "schema validators, contract tests", "input-validation-auditor", "ensure every trust boundary validates shape and constraints", "semantic validation may need domain-specific rules", "malformed/boundary-value request fixtures", ["VERACODE-2026", "ARXIV-SECURE-CODING"]),
    ("P018", "Vulnerable or malicious dependencies", "security", "all dependency-using projects", "critical", "strong", "unreviewed additions and stale vulnerability knowledge", "lockfiles, vulnerability scanners, registries", "dependency-vulnerability-auditor", "ground dependency changes in live metadata and project need", "offline scans can miss new advisories", "fixtures with known-vulnerable test dependencies and typo packages", ["SONATYPE-2026", "SO-DISRUPTION"]),
    ("P019", "Security misconfiguration and insecure defaults", "security", "deployers and backend developers", "critical", "strong", "development defaults leaking into production", "CIS/OWASP guidance, config validation", "security-misconfiguration-auditor", "check exposed services, debug modes, CORS, cookies, TLS and headers", "environment-specific policy varies", "container/config fixtures with known insecure settings", ["VERACODE-2026", "DORA-2025"]),
    ("P020", "Prompt injection changes tool-using agent behavior", "security", "agent users with web/MCP/tools", "critical", "strong", "untrusted content shares instruction channel with agent context", "least privilege, approvals, content isolation", "agent-tool-trust-auditor", "separate data from authority and constrain high-impact actions", "prompt injection cannot be fully eliminated by instructions alone", "fixtures containing malicious third-party instructions plus protected action policy", ["OPENAI-PROMPT-INJECTION", "ISSUE-CODEX-MCP-STALL"]),
    ("P021", "Important behavior has no automated tests", "testing", "all software teams", "high", "strong", "prototype-first development and unverified agent completion", "unit/integration/E2E testing", "missing-test-detector", "map changed behavior to absent test coverage", "coverage metrics do not imply assertion quality", "fixtures with changed untested branch and known existing tests", ["SO-AI-DATA", "DORA-2025"]),
    ("P022", "Tests are superficial or assertion-poor", "testing", "all software teams", "high", "strong", "tests mirror implementation or only assert success status", "mutation testing, review, property tests", "test-quality-auditor", "detect vacuous assertions and missing negative cases", "semantic quality cannot be fully inferred statically", "mutation fixtures and intentionally weak tests", ["SO-NEXT", "ISSUE-AIDER-TESTS"]),
    ("P023", "Mocks create false confidence about integrations", "testing", "API/integration developers", "high", "moderate", "all external behavior replaced by mocks", "contract tests, sandbox services, testcontainers", "integration-reality-checker", "identify critical boundaries never exercised against realistic dependencies", "real integrations may be expensive or credential-bound", "fixtures with passing mocked test and failing local fake server", ["SO-COMPLEX", "DORA-2025"]),
    ("P024", "UI flows are broken despite component success", "frontend", "frontend/full-stack developers", "high", "moderate", "component-local testing and missing browser-level verification", "browser E2E tests, accessibility trees", "ui-flow-verifier", "exercise real navigation/forms/loading/errors", "browser automation can be flaky", "broken route/form fixture tested through browser harness when available", ["SO-NEXT", "SO-AI-DATA"]),
    ("P025", "API contracts drift across client/server boundaries", "backend", "full-stack/API teams", "high", "moderate", "independent edits to schema, types, docs, and consumers", "OpenAPI, generated clients, contract tests", "api-contract-auditor", "compare producer/consumer schemas and error semantics", "dynamic APIs may lack formal schema", "fixtures with mismatched field/type/status codes", ["SO-DISRUPTION", "DORA-2025"]),
    ("P026", "Tests leak state or contaminate each other", "testing", "test-suite maintainers", "medium", "moderate", "shared global state, reused databases, order dependence", "isolated fixtures, randomized order", "test-isolation-auditor", "find shared mutable fixtures and order-sensitive behavior", "intermittent races can be hard to reproduce", "order-randomized fixture suite with intentional leakage", ["ISSUE-AIDER-TESTS", "DORA-2025"]),
    ("P027", "Deployment is declared successful without runtime verification", "deployment", "deployers and product builders", "critical", "strong", "build success treated as product success", "smoke tests, health checks, synthetic monitoring", "deployment-smoke-verifier", "verify critical user/API flows after deploy", "production credentials and external access may be unavailable", "local container deployment fixture plus smoke probes", ["DORA-2025", "SO-AI-DATA"]),
    ("P028", "Generated architecture accumulates oversized modules", "architecture", "growing AI-built codebases", "high", "moderate", "incremental additions without boundary review", "modularity metrics, code review", "architecture-complexity-auditor", "surface high-coupling modules and coherent split points", "metrics can reward fragmentation", "fixtures with god modules vs cohesive modules", ["SO-COMPLEX", "METR-2025"]),
    ("P029", "Circular dependencies and import tangles", "architecture", "medium/large codebases", "high", "moderate", "cross-layer shortcuts and generated convenience imports", "dependency graph tools, layering rules", "dependency-cycle-auditor", "detect cycles and propose minimal boundary changes", "runtime/dynamic imports can hide edges", "graph fixtures with direct and indirect cycles", ["SO-COMPLEX", "DORA-2025"]),
    ("P030", "State management becomes fragile and duplicated", "frontend", "frontend/full-stack developers", "high", "moderate", "multiple sources of truth and ad hoc async state", "state machines, query caches, architecture review", "state-management-auditor", "trace ownership, lifecycle, and duplicate state", "framework patterns differ", "fixture with stale derived state and duplicate stores", ["SO-COMPLEX", "SO-AI-DATA"]),
    ("P031", "Database schema relationships are incorrect", "backend", "backend/data developers", "critical", "moderate", "model generation without real access patterns or constraints", "schema review, constraints, migration tests", "database-schema-reviewer", "check keys, uniqueness, nullability and query patterns", "cannot infer all business invariants", "fixture with missing FK/unique/index plus representative queries", ["SO-COMPLEX", "DORA-2025"]),
    ("P032", "Tight coupling makes AI changes cascade", "architecture", "maintainers", "high", "moderate", "cross-layer knowledge and direct dependencies", "ports/adapters, interfaces, module boundaries", "coupling-refactor-planner", "identify smallest seam that reduces change fan-out", "abstraction can be overused", "change-impact fixture measuring touched modules", ["DORA-2025", "METR-2025"]),
    ("P033", "Database migrations risk data loss or lockups", "backend", "backend/data developers", "critical", "moderate", "destructive schema changes without staged rollout", "expand-contract migrations, backups, dry runs", "migration-safety-reviewer", "classify destructive operations and require rollback evidence", "database engines differ in locking/DDL semantics", "temporary database fixtures for forward/rollback migrations", ["DORA-2025", "SO-AI-DATA"]),
    ("P034", "Transactions and concurrency invariants are missing", "backend", "backend developers", "critical", "moderate", "happy-path generation without interleaving analysis", "transactions, idempotency, locking tests", "data-consistency-auditor", "identify write sequences requiring atomicity/idempotency", "race reproduction may be nondeterministic", "concurrent fixture with double-submit/lost-update scenarios", ["SO-COMPLEX", "VERACODE-2026"]),
    ("P035", "AI-generated UI is visually inconsistent", "frontend", "frontend/product builders", "medium", "moderate", "local component generation without design tokens or system context", "design systems, visual regression tests", "ui-consistency-auditor", "enforce token/component reuse and layout consistency", "visual taste is partly subjective", "DOM/style fixture plus token-usage checks", ["SO-AI-DATA"]),
    ("P036", "Responsive behavior breaks across viewports", "frontend", "frontend developers", "high", "moderate", "desktop-first generation and untested breakpoints", "responsive testing, browser matrices", "responsive-design-auditor", "exercise representative widths and overflow/touch targets", "device-specific browser bugs may remain", "viewport fixture with intentional overflow and clipped controls", ["SO-AI-DATA"]),
    ("P037", "Accessibility requirements are missed", "frontend", "frontend/product builders", "high", "strong", "visual-only validation and missing semantic checks", "axe, WCAG review, keyboard/screen-reader testing", "accessibility-auditor", "systematically test semantics, keyboard, focus, contrast and labels", "automated checks catch only part of WCAG", "fixture with known automated and manual accessibility defects", ["SO-AI-DATA", "GH-COPILOT-LIMITS"]),
    ("P038", "Loading, empty, and error states are incomplete", "frontend", "product builders", "high", "moderate", "happy-path bias in generated UI", "UX state matrices, integration tests", "ux-state-completeness-auditor", "enumerate asynchronous and zero/error states per flow", "product-specific messaging still needs judgment", "fixture with unhandled loading/empty/error branches", ["SO-COMPLEX", "SO-AI-DATA"]),
    ("P039", "Buttons, routes, or integrations are placeholders", "product-completeness", "nontechnical and technical builders", "critical", "strong", "UI scaffolding mistaken for implemented behavior", "E2E tests, dead-code/static route checks", "dead-feature-detector", "trace visible actions to real handlers and effects", "some placeholders are intentional and must be declared", "fixture with fake buttons, TODO handlers, hardcoded demo data", ["SO-DISRUPTION", "GH-COPILOT-LIMITS"]),
    ("P040", "Local environment differs from production", "deployment", "all deployers", "critical", "strong", "implicit machine state and unpinned dependencies", "containers, lockfiles, reproducible builds", "environment-parity-auditor", "compare runtime versions, services, files and configuration assumptions", "managed platforms can hide details", "fixture passing locally but failing in containerized clean environment", ["DORA-2025", "SO-AI-DATA"]),
    ("P041", "Environment variables are missing, stale, or undocumented", "deployment", "deployers", "high", "strong", "configuration scattered across code and dashboards", "schema validation, example env files", "environment-config-auditor", "derive required variables from code and deployment manifests", "secret values cannot be validated offline", "fixtures with missing/unused/misspelled environment variables", ["SO-DISRUPTION", "DORA-2025"]),
    ("P042", "CI failures are patched without understanding the failing stage", "deployment", "teams using CI", "high", "moderate", "large logs and guess-driven config edits", "CI logs, local reproduction, workflow validation", "ci-failure-investigator", "map failing job/step to reproducible local or isolated cause", "hosted-runner-only failures may remain", "fixture workflows with dependency, permission and test failures", ["SO-DISRUPTION", "SO-NEXT"]),
    ("P043", "Production has no meaningful health or smoke checks", "deployment", "deployers", "critical", "moderate", "build/deploy status used as health proxy", "health endpoints, synthetic checks, monitoring", "production-readiness-auditor", "require liveness/readiness plus critical workflow probes", "full observability is platform-specific", "container fixture with process alive but dependency unavailable", ["DORA-2025", "SO-AI-DATA"]),
    ("P044", "Agent claims completion without evidence", "agent-reliability", "users delegating multi-step work", "critical", "strong", "language completion bias and missing acceptance criteria", "tests, screenshots, command evidence, checklists", "completion-claims-auditor", "tie each completion claim to observed verification", "some requirements are subjective", "fixtures with passing prose but failing feature behavior", ["SO-TRUST", "SO-NEXT", "GH-COPILOT-LIMITS"]),
    ("P045", "Agent silently ignores requirements", "agent-reliability", "users giving large prompts/specs", "critical", "strong", "long-context omission and no requirement ledger", "acceptance checklists, traceability matrices", "requirement-traceability-auditor", "map every requirement to implementation and evidence", "ambiguous requirements still need user interpretation", "fixture spec with seeded omitted requirement", ["SO-COMPLEX", "SO-DISRUPTION"]),
    ("P046", "Agent modifies unrelated files", "agent-reliability", "developers using autonomous agents", "high", "moderate", "scope drift and broad formatting/refactors", "git diff review, ownership rules", "scope-drift-guard", "flag edits without a requirement or dependency rationale", "generated files can create legitimate broad diffs", "fixture repo with explicit allowed/forbidden edit set", ["SO-TRUST", "GH-COPILOT-LIMITS"]),
    ("P047", "Project context is lost across sessions", "agent-reliability", "long-running agent projects", "high", "strong", "ephemeral conversation state and incomplete handoffs", "repo docs, task ledgers, persisted plans", "project-context-recovery", "reconstruct state from repository evidence before acting", "uncommitted external decisions may be unrecoverable", "fixture with interrupted task and partial commits/notes", ["ISSUE-CLINE-CONTEXT", "SO-AI-DATA"]),
    ("P048", "Working code is destroyed while fixing another area", "agent-reliability", "developers using agents on existing projects", "critical", "moderate", "overwrite/regeneration instead of minimal patching", "version control, tests, protected files", "existing-work-preservation", "baseline known-good behavior and restrict edit surface", "baseline may already contain defects", "fixture with protected working flow and unrelated requested fix", ["SO-TRUST", "DORA-2025"]),
    ("P049", "Parallel agents create conflicting or duplicate work", "agent-reliability", "multi-agent users", "high", "moderate", "shared files, overlapping objectives, missing integration owner", "worktrees, file ownership, integration review", "multi-agent-integration-reviewer", "detect overlap, inconsistent assumptions, and merge hazards", "semantic conflicts can survive clean merges", "parallel fixture branches with syntactic and semantic conflicts", ["METR-2026", "ISSUE-CODEX-MCP-STALL"]),
    ("P050", "AI workflows waste tokens and repeat research", "efficiency", "frequent AI coding users", "medium", "strong", "weak task decomposition, repeated context, no cached evidence", "plans, repo docs, search result caching", "token-efficient-workflow", "reuse verified context and stop redundant exploration", "token savings can trade off with missing context", "compare tool calls/context size on fixed tasks", ["SO-KNOWLEDGE", "METR-2025"]),
    ("P051", "Documentation is missing or inaccurate", "documentation", "maintainers and new contributors", "high", "strong", "code changes without docs synchronization", "docs tests, examples, generated reference docs", "documentation-accuracy-auditor", "verify commands, paths, APIs, screenshots and claims against repo state", "external service behavior can change after validation", "fixtures with stale command/path/API docs", ["SO-AI-DATA", "SO-NEXT"]),
    ("P052", "Dead or redundant dependencies accumulate", "dependencies", "maintainers", "medium", "moderate", "AI adds libraries for narrow tasks then leaves them", "dependency analyzers, lockfile review", "dependency-cleanup-auditor", "find unused, duplicate, replaceable or stale packages", "dynamic imports/plugins can look unused", "fixtures with direct, transitive, optional and dynamically loaded dependencies", ["SONATYPE-2026", "SO-DISRUPTION"]),
    ("P053", "Release artifacts and version metadata are inconsistent", "release", "maintainers", "high", "moderate", "manual release steps and unverified generated artifacts", "release checklists, provenance, CI packaging", "release-verification-agent", "cross-check version, changelog, tags, artifacts and install smoke tests", "platform-specific signing may be inaccessible", "fixture release with mismatched version/tag/artifact metadata", ["DORA-2025", "SO-NEXT"]),
    ("P054", "Cross-platform assumptions break builds or runtime", "deployment", "cross-platform projects", "high", "strong", "path/shell/case/newline assumptions from one host", "CI matrices, platform abstractions", "cross-platform-readiness-auditor", "find OS-specific commands, paths, permissions and encoding assumptions", "cannot fully emulate every target OS locally", "Windows/Linux path and shell fixtures plus CI matrix", ["ISSUE-CODEX-MCP-STALL", "SO-DISRUPTION"]),
    ("P055", "MCP/plugin integration overload or failure blocks the agent", "agent-reliability", "users with multiple MCP servers/plugins", "high", "strong", "eager startup, slow handshakes, retry storms, broad tool sets", "timeouts, lazy startup, health checks, least-privilege tool sets", "mcp-reliability-auditor", "inventory servers, startup cost, timeouts, failure isolation and permissions", "host implementations differ and some telemetry is inaccessible", "fake MCP servers with slow/failing handshakes plus resource/process assertions", ["ISSUE-CODEX-MCP-STALL", "ISSUE-CODEX-SPAWN", "ISSUE-CODEX-STALL"]),
]


def evidence_row(
    evidence_id: str,
    problem_id: str,
    source_id: str,
    claim: str,
    affected: str,
    severity: str,
    strength: str,
    root_cause: str,
    existing_solution: str,
    proposed_skill: str,
    benefit: str,
    limitation: str,
    validation: str,
) -> dict[str, str]:
    source = SOURCES[source_id]
    return {
        "evidence_id": evidence_id,
        "problem_id": problem_id,
        "description": claim,
        "evidence_links": source["url"],
        "source_date": source["date"],
        "affected_developers": affected,
        "severity": severity,
        "estimated_frequency_or_evidence_strength": strength,
        "root_causes": root_cause,
        "existing_solutions": existing_solution,
        "proposed_skill_based_solution": proposed_skill,
        "expected_benefits": benefit,
        "limitations": limitation,
        "validation_strategy": validation,
        "source_kind": source["kind"],
        "source_title": source["title"],
    }


def build_evidence() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    counter = 1

    def add(problem_id: str, source_id: str, claim: str, affected: str, severity: str, strength: str, root: str, existing: str, skill: str, benefit: str, limitation: str, validation: str) -> None:
        nonlocal counter
        rows.append(
            evidence_row(
                f"E{counter:03d}",
                problem_id,
                source_id,
                claim,
                affected,
                severity,
                strength,
                root,
                existing,
                skill,
                benefit,
                limitation,
                validation,
            )
        )
        counter += 1

    disruption = [
        ("P001", "Plausible but wrong code", "69.3%"),
        ("P005", "Hard-to-review generated code", "54.2%"),
        ("P004", "Missing context", "49.3%"),
        ("P002", "Hallucinated package/config", "45.1%"),
        ("P003", "Incorrect or stale internal knowledge", "38.7%"),
        ("P003", "Outdated APIs", "33.9%"),
        ("P006", "Poor debugging path", "24.7%"),
        ("P013", "Security/privacy issue", "23.5%"),
        ("P051", "Licensing/source uncertainty", "11.4%"),
    ]
    for problem_id, label, pct in disruption:
        add(problem_id, "SO-DISRUPTION", f"{pct} of respondents selected {label} as an AI mistake that cost them or their team the most time.", "professional developers using AI", "high", "strong survey evidence", "AI output is accepted before sufficient grounding or verification", "local execution, code review, official docs, tests/security checks", "verification and grounding workflow", "focus agent effort on observed failure modes", "self-reported multi-select survey does not prove causality", "track detection of seeded instances in fixed repository fixtures")

    workflow = [
        ("P050", "Analyzing data, logs, metrics, or query results", "41.9%"),
        ("P045", "Answering complex or ambiguous technical questions", "50.0%"),
        ("P003", "Answering straightforward technical questions", "59.4%"),
        ("P028", "Architecture or technical design exploration", "47.4%"),
        ("P040", "Creating or configuring development/test environments", "28.1%"),
        ("P006", "Debugging, troubleshooting, or refactoring code", "63.8%"),
        ("P027", "Deploying, operating, or troubleshooting production systems", "19.9%"),
        ("P019", "Finding or fixing security issues", "34.6%"),
        ("P001", "Generating code in a familiar area", "69.3%"),
        ("P004", "Generating code in an unfamiliar area", "56.0%"),
        ("P035", "Generating visual, audio, or multimedia elements", "17.5%"),
        ("P035", "Product, UX, or visual design", "30.3%"),
        ("P005", "Reviewing code, pull requests, or design decisions", "40.5%"),
        ("P047", "Searching, summarizing, or interpreting internal knowledge", "49.7%"),
        ("P047", "Understanding or onboarding to a new codebase", "49.7%"),
        ("P051", "Writing documentation, comments, or knowledge base content", "51.1%"),
        ("P050", "Writing emails, messages, summaries, or other communication", "23.5%"),
        ("P021", "Writing or improving tests", "58.1%"),
        ("P045", "Writing tickets, requirements, plans, or project updates", "27.8%"),
    ]
    for problem_id, label, pct in workflow:
        add(problem_id, "SO-AI-DATA", f"{pct} currently use AI for {label}.", "professional developers using AI", "context", "strong adoption evidence", "high usage increases exposure to quality and verification failures in this workflow", "human review and domain-specific tools", "workflow-specific skill", "target safeguards where AI is already used", "usage rate is not a defect rate", "measure task-specific failure detection on representative fixtures")

    validation_steps = [
        ("P012", "Run AI output locally", "76.5%"),
        ("P004", "Compare AI output against codebase context", "63.9%"),
        ("P021", "Inspect tests/security implications", "53.0%"),
        ("P003", "Read official docs", "38.0%"),
        ("P006", "Search Stack Overflow", "12.2%"),
        ("P044", "Use AI output as-is", "9.6%"),
        ("P005", "Ask a coworker", "6.9%"),
        ("P044", "Do not use AI tools", "1.7%"),
    ]
    for problem_id, label, pct in validation_steps:
        add(problem_id, "SO-NEXT", f"{pct} reported the validation behavior: {label}.", "professional developers using AI", "context", "strong survey evidence", "developers compensate for uncertain AI output with independent checks", "local execution, codebase comparison, docs, peer review", "completion and verification workflow", "encode high-value validation steps into repeatable agent behavior", "behavior frequency does not establish which step is most effective", "compare defect escape rates with and without prescribed checks")

    trust = [
        ("P044", "Trust when output is easy to verify", "48.0%"),
        ("P044", "Trust for many tasks but not important decisions", "16.3%"),
        ("P044", "Trust for low-risk tasks only", "16.3%"),
        ("P044", "Do not trust for most work tasks", "12.3%"),
        ("P044", "Trust including important decisions", "6.6%"),
        ("P044", "Not sure or do not use AI", "0.5%"),
    ]
    for problem_id, label, pct in trust:
        add(problem_id, "SO-TRUST", f"{pct} selected: {label}.", "professional developers using AI", "high", "strong survey evidence", "trust depends heavily on verifiability and risk", "human review and executable verification", "completion-claims-auditor", "make verification evidence explicit before claiming success", "trust is subjective and task-dependent", "measure whether every claim links to observed test/tool evidence")

    complex_rows = [
        ("Very well", "16.0%"),
        ("Good, but not great", "38.8%"),
        ("Neither good nor bad", "14.4%"),
        ("Bad", "16.0%"),
        ("Very poor", "8.0%"),
        ("Do not use AI for complex tasks / do not know", "6.9%"),
    ]
    for label, pct in complex_rows:
        add("P045", "SO-COMPLEX", f"{pct} rated AI handling of complex tasks as: {label}.", "developers using AI for complex tasks", "high", "strong survey evidence", "complex multi-step tasks amplify context, planning and verification limits", "task decomposition, plans, tests, human review", "requirement-traceability-auditor", "reduce omission and premature-completion failures", "subjective rating; tools/models vary", "fixed complex-task benchmark with requirement-level scoring")

    delegated = [
        ("P001", "Writing/editing/generating code", "72.9%"),
        ("P006", "Debugging/troubleshooting", "62.2%"),
        ("P021", "Writing/maintaining tests", "50.6%"),
        ("P051", "Writing/updating documentation", "48.3%"),
        ("P005", "Reviewing code/PRs/technical changes", "44.9%"),
        ("P028", "Technical design/architecture decisions", "26.4%"),
        ("P043", "Investigating incidents/outages/production issues", "25.9%"),
        ("P045", "Planning/scoping/estimating work", "25.2%"),
        ("P050", "Answering teammate/customer/stakeholder questions", "21.4%"),
        ("P050", "Analyzing data/reports/business metrics", "20.2%"),
        ("P047", "Onboarding to new project/tool/system/codebase", "19.7%"),
        ("P019", "Finding/fixing security, privacy, compliance issues", "19.5%"),
        ("P027", "Changing production code/systems/infrastructure", "18.9%"),
        ("P052", "Maintaining dependencies/packages/environments", "18.5%"),
        ("P043", "Monitoring systems/logs/metrics/alerts", "13.6%"),
        ("P053", "Deploying/releasing software", "9.8%"),
    ]
    for problem_id, label, pct in delegated:
        add(problem_id, "SO-KNOWLEDGE", f"{pct} delegated {label} to an AI tool or agent in the last 30 days.", "professional AI-agent users", "context", "strong adoption evidence", "delegation makes repeatable verification and boundaries valuable", "existing engineering controls plus human approval", "domain-specific guard skill", "put checks next to workflows already delegated", "delegation rate is not a failure rate", "benchmark skill on representative delegated-task fixtures")

    cost = [
        ("P050", "Personally monitor own AI use", "32.6%"),
        ("P050", "Choose cheaper models when possible", "25.3%"),
        ("P050", "Usage is metered to manage costs", "23.8%"),
        ("P050", "Cost/limits have not affected usage", "22.4%"),
        ("P050", "Have not encountered cost/limits", "20.6%"),
        ("P050", "More selective about tasks", "16.6%"),
        ("P050", "Company/team increased AI budget", "12.8%"),
        ("P050", "Not sure", "11.3%"),
        ("P050", "Company/team switched to more affordable models/vendors", "6.9%"),
        ("P050", "Choose faster models even when they cost more", "4.9%"),
    ]
    for problem_id, label, pct in cost:
        add(problem_id, "SO-KNOWLEDGE", f"{pct} reported cost/usage-limit behavior: {label}.", "AI tool users facing cost or limits", "medium", "strong survey evidence", "model/tool use has real budget and quota constraints", "task selection, model routing, caching, concise context", "token-efficient-workflow", "reduce unnecessary calls without weakening verification", "cost-sensitive subset is smaller than full survey", "measure tool calls/context bytes/task success on fixed tasks")

    switching = [
        ("No switch", "33.7%"),
        ("Better output quality", "25.1%"),
        ("Organization required/recommended different tool", "10.6%"),
        ("Better workflow/development-environment integration", "7.4%"),
        ("Lower cost", "6.4%"),
        ("Better agents/automation/coding workflows", "3.7%"),
        ("Another reason", "3.6%"),
        ("Previous tool too expensive/limited/unavailable", "3.3%"),
        ("Better security/privacy/compliance", "2.2%"),
        ("Preferred model/provider access", "2.1%"),
        ("Specific feature", "1.4%"),
    ]
    for label, pct in switching:
        add("P054", "SO-AI-DATA", f"{pct} reported AI tool switching outcome/reason: {label}.", "professional AI users", "context", "strong survey evidence", "tool ecosystems differ and users switch for quality, integration, cost and security", "portable skills and adapters", "cross-agent compatibility layer", "avoid lock-in to one agent surface", "switching reason does not imply standards compatibility", "run structural/behavioral compatibility checks on supported agents")

    memory = [
        ("Just me", "53.6%"),
        ("Organization centrally", "14.7%"),
        ("Do not want retained memory", "14.2%"),
        ("My team", "11.1%"),
        ("Not sure", "6.4%"),
    ]
    for label, pct in memory:
        add("P047", "SO-AI-DATA", f"{pct} prefer AI work-memory control by: {label}.", "AI users", "medium", "strong survey evidence", "project continuity competes with privacy and control requirements", "repo-local handoffs and explicit persisted context", "project-context-recovery", "recover context from user-controlled repository evidence", "survey preference does not specify implementation architecture", "verify skill works with memory disabled and only repo-local artifacts")

    org = [
        ("AI optional and individual-led", "29.7%"),
        ("Approved tools and guidance", "24.0%"),
        ("Teams encourage AI but practices vary", "15.9%"),
        ("Some employees expected to use AI", "11.5%"),
        ("AI use measured/evaluated", "10.2%"),
        ("Organization does not use AI for work", "6.1%"),
        ("Not sure", "2.6%"),
    ]
    for label, pct in org:
        add("P045", "SO-AI-DATA", f"{pct} reported organizational AI practice: {label}.", "professional developers", "context", "strong survey evidence", "governance and repeatable workflows are uneven across organizations", "team guidance, approved tools, policies", "portable skill library", "codify repeatable quality gates independent of one vendor", "organization policy varies and may override library defaults", "validate skills under least-privilege local and CI workflows")

    external = [
        ("P013", "VERACODE-2026", "The report states the best model in its Summer 2026 dataset had a 68% security pass rate; several models clustered near 50%.", "developers relying on generated code", "critical", "strong benchmark evidence", "functional code generation does not imply secure generation", "SAST/DAST, review, threat modeling", "security audit skills", "make security checks explicit", "benchmark task distribution may differ from real projects", "security fixture suite with known CWEs"),
        ("P013", "VERACODE-2025", "The 2025 report found detectable OWASP Top 10 vulnerabilities in 45% of tested generated-code cases.", "developers relying on generated code", "critical", "strong benchmark evidence", "security is not guaranteed by syntactic correctness", "security scanners and manual review", "security audit skills", "prevent shipping syntactically valid but unsafe code", "vendor-authored benchmark; reproduce with open fixtures where possible", "known-vulnerability fixture suite"),
        ("P019", "ARXIV-GH-SEC", "A public-GitHub analysis reported 4,241 CWE instances across 7,703 AI-attributed files.", "open-source AI-assisted developers", "critical", "research evidence", "generated code can carry real-world vulnerability patterns", "CodeQL and language-specific secure coding", "security-misconfiguration-auditor", "prioritize real CWE classes", "AI attribution and repository selection can be noisy", "replicate selected checks on public fixtures"),
        ("P015", "ARXIV-SECURE-CODING", "In a manually reviewed subset, ChatGPT detected 18 of 32 confirmed vulnerabilities and fixed 17; 22 vulnerabilities were introduced by ChatGPT rather than prompts.", "developers using LLMs for security-sensitive code", "critical", "research evidence", "same model that generates defects may incompletely review them", "independent scanners and manual review", "security review separation", "avoid self-certification by the generator alone", "small manually reviewed subset", "independent static-analysis verification"),
        ("P009", "DORA-2025", "DORA reported AI adoption positively related to throughput/product performance but negatively related to delivery stability.", "software teams adopting AI", "high", "strong industry research", "higher change volume exposes weak testing and feedback systems", "automated testing, version control, fast feedback", "regression-detector", "make AI speed conditional on stability controls", "correlation does not prove causation", "compare defect escape/stability on fixed CI fixtures"),
        ("P050", "METR-2025", "A randomized study of experienced open-source developers found tasks took 19% longer with early-2025 AI tools in that setting.", "experienced developers on mature familiar repos", "medium", "RCT in narrow setting", "review/interaction overhead can outweigh generation speed", "selective AI use and measurable workflows", "token-efficient-workflow", "optimize for task success and time, not amount of AI use", "authors explicitly warn against generalizing to all developers/tasks", "benchmark end-to-end elapsed work on controlled tasks"),
        ("P049", "METR-2026", "METR later reported selection effects and weak evidence of improved speedup, especially with more concurrent agent use.", "developers using newer agents", "context", "research update", "concurrency changes measurement and workflow coordination", "task ownership and integration review", "multi-agent-integration-reviewer", "make parallelism auditable", "selection bias prevents strong causal estimate", "measure overlap/conflicts in parallel fixture tasks"),
        ("P002", "SONATYPE-2026", "Across 36,870 upgrade recommendations, 27.76% referenced nonexistent versions before live repository grounding.", "developers using AI for dependency upgrades", "high", "large vendor dataset", "package ecosystems change faster than model knowledge", "live registries and lockfile-aware tools", "dependency-grounding-auditor", "eliminate invented versions through grounding", "dataset comes from vendor methodology", "compare recommendations to live/local package metadata"),
        ("P001", "GH-COPILOT-LIMITS", "GitHub documents that Copilot may miss code-quality problems and may hallucinate false-positive review comments.", "Copilot users", "high", "official limitation", "LLM review is fallible in both directions", "human review and independent checks", "completion-claims-auditor", "require evidence before accepting review findings", "applies to GitHub Copilot and may not transfer exactly", "seed true/false defects and measure precision/recall"),
        ("P020", "OPENAI-PROMPT-INJECTION", "OpenAI describes prompt injection as third-party content misleading an agent into actions the user did not request.", "tool-using agents reading untrusted content", "critical", "official security guidance", "untrusted data can be interpreted as instructions", "least privilege, approvals, isolation", "agent-tool-trust-auditor", "reduce authority confusion", "instruction-only defenses are incomplete", "malicious-content fixtures with protected actions"),
        ("P007", "ISSUE-CODEX-LOOP", "A 2026 Codex Desktop issue reports repeated tool calls continuing without task progress.", "Codex Desktop users", "high", "concrete issue evidence", "missing no-progress stop condition", "manual cancellation and restart", "loop-breaker", "detect repeated identical actions before waste escalates", "single issue report; cause may be product-specific", "synthetic repeated-tool-call transcript"),
        ("P055", "ISSUE-CODEX-MCP-STALL", "A 2026 Codex issue reports slow/failing MCP startup, queue saturation, and hundreds of descendant processes under many loaded threads.", "Codex users with many MCP servers/threads", "high", "detailed issue evidence", "eager startup and retry behavior can couple unrelated workflows", "timeouts, lazy loading, health checks", "mcp-reliability-auditor", "surface startup cost and failure isolation", "complex environment and no minimal reproduction", "local fake MCP servers with controlled delays/failures"),
        ("P055", "ISSUE-CODEX-SPAWN", "A 2026 Codex issue reports an infinite cmd/node process spawn loop associated with a bundled plugin MCP startup path.", "Windows Codex plugin users", "high", "concrete issue evidence", "handshake retry loops can multiply processes", "disable failing plugin, add startup circuit breaker", "mcp-reliability-auditor", "detect runaway child-process growth", "product-specific implementation", "fake failing MCP with process-count guard"),
        ("P055", "ISSUE-CODEX-STALL", "A 2026 Codex issue reports tool calls stalling for hours while turns wait for tool results.", "Codex Desktop users", "high", "concrete issue evidence", "tool dispatch/completion signaling can deadlock or fail silently", "timeouts, cancellation, health probes", "mcp-reliability-auditor", "require bounded waits and observable failure", "single environment; root cause not fully isolated", "fake tool that never returns plus timeout/cancel assertion"),
        ("P007", "ISSUE-ROO-LOOP", "A Roo Code issue reports false-positive loop detection when repeated MCP calls are making measurable progress.", "Roo Code MCP users", "medium", "concrete issue evidence", "naive repetition heuristics ignore state progress", "progress-aware loop detection", "loop-breaker", "avoid both infinite loops and premature aborts", "issue is specific to one loop detector", "paired fixtures: identical-no-progress vs repeated-progress"),
        ("P022", "ISSUE-AIDER-TESTS", "An Aider issue reports benchmark tests left disabled or skipped, undermining execution coverage.", "agent benchmark maintainers", "high", "concrete issue evidence", "test presence can be mistaken for test execution", "fail on skipped critical tests; inspect runner output", "test-quality-auditor", "separate test files from tests actually run", "open issue may reflect a transient benchmark bug", "fixture with skipped tests and expected executed-test count"),
        ("P047", "ISSUE-CLINE-CONTEXT", "A Cline issue reports session-not-found behavior, illustrating continuity failures across coding sessions.", "Cline users", "medium", "concrete issue evidence", "session state can disappear or become inaccessible", "repo-local handoff state", "project-context-recovery", "make progress recoverable from repository evidence", "product-specific bug and sparse public detail", "interrupt/resume fixture using only repository artifacts"),
        ("P007", "ISSUE-ROO-RETRY", "A Roo Code issue reports structural API errors retried indefinitely without a circuit breaker.", "Roo Code users", "high", "concrete issue evidence", "retries occur without classifying permanent vs transient failures", "retry budgets and error classification", "loop-breaker", "bound repeated failures and protect conversation history", "single issue report", "permanent-error fixture asserting bounded attempts"),
    ]
    for entry in external:
        add(*entry)

    return rows


def write_sources() -> None:
    lines = [
        "# Sources",
        "",
        "Sources were selected for recency, direct relevance, methodological clarity, and traceability. Survey rows are evidence about developer experience and behavior; issue reports are concrete failure examples rather than prevalence estimates.",
        "",
        "| ID | Source | Date | Type | Why it is used |",
        "|---|---|---|---|---|",
    ]
    for source_id, source in SOURCES.items():
        lines.append(
            f"| {source_id} | [{source['title']}]({source['url']}) | {source['date']} | {source['kind']} | {source['notes']} |"
        )
    (RESEARCH / "sources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_methodology(evidence: list[dict[str, str]]) -> None:
    source_kinds = sorted({row["source_kind"] for row in evidence})
    text = f"""# Research methodology

## Question

Which recurring problems in AI-assisted software development can be reduced by reusable Agent Skills, deterministic repository tooling, or carefully scoped MCP integrations?

## Evidence strategy

The corpus combines:

- current 2026 developer survey data,
- security and software-delivery research,
- official product limitations and security guidance,
- public issue reports from coding-agent projects,
- current Agent Skills and plugin documentation.

The generated evidence table contains {len(evidence)} traceable evidence items across {len(SOURCES)} named sources. Evidence types include {", ".join(source_kinds)}.

Survey percentages are copied as reported and are never converted into defect rates. A high usage percentage means a workflow is common, not that the workflow fails at that rate. Public issue reports demonstrate concrete failure modes but do not establish prevalence.

## Inclusion criteria

1. Directly relevant to AI-assisted coding, software quality, security, testing, agent reliability, deployment, maintainability, or developer workflow.
2. Prefer evidence published in the last 12 months relative to 2026-10-25.
3. Older evidence is retained when it provides a foundational controlled study or a still-relevant security result.
4. Every quantitative claim must link to a source that reports the value.
5. Product issue reports are labeled as issue evidence and are not generalized into population-level frequency estimates.

## Deduplication

Reports are grouped by underlying failure pattern. For example, repeated-tool-call bugs from different agents support one broader no-progress-loop pattern rather than becoming separate candidate problems.

## Corroboration

A problem is treated as independently corroborated when it has support from at least two materially different evidence sources or evidence types, such as a developer survey plus a security study, or an official limitation plus public issue evidence.

## Mapping to skills

Candidate skills are favored when the workflow can define:

- a recognizable trigger,
- required evidence or inputs,
- a bounded procedure,
- deterministic checks where available,
- an observable output,
- explicit failure handling,
- testable completion criteria.

Problems that require privileged infrastructure, proprietary telemetry, organizational policy decisions, or guaranteed prevention of model-level failures are documented as partially solvable rather than presented as fully solved by instructions.
"""
    (RESEARCH / "research-methodology.md").write_text(text, encoding="utf-8")


def write_evidence_csv(evidence: list[dict[str, str]]) -> None:
    fieldnames = list(evidence[0].keys())
    with (RESEARCH / "problem-evidence.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(evidence)


def write_problems() -> None:
    lines = [
        "# Vibe-coding problem inventory",
        "",
        f"This inventory contains {len(PROBLEMS)} candidate problems. Severity is an engineering-risk judgment; evidence strength describes the support in the current corpus and is not a prevalence estimate.",
        "",
        "| ID | Problem | Category | Affected | Severity | Evidence | Root causes | Existing solutions | Proposed skill | Expected benefit | Limitations | Validation | Supporting sources |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in PROBLEMS:
        (
            problem_id,
            title,
            category,
            affected,
            severity,
            strength,
            causes,
            existing,
            skill,
            benefit,
            limitation,
            validation,
            refs,
        ) = row
        links = "; ".join(f"[{ref}]({SOURCES[ref]['url']})" for ref in refs)
        cells = [problem_id, title, category, affected, severity, strength, causes, existing, skill, benefit, limitation, validation, links]
        cells = [cell.replace("|", "/") for cell in cells]
        lines.append("| " + " | ".join(cells) + " |")
    (RESEARCH / "vibe-coding-problems.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_taxonomy() -> None:
    categories: dict[str, list[tuple[str, str]]] = {}
    for row in PROBLEMS:
        categories.setdefault(row[2], []).append((row[0], row[1]))
    lines = [
        "# Problem taxonomy",
        "",
        "The taxonomy separates the underlying engineering failure from the product or agent where it was observed. One skill may address several related failures when they share the same trigger and verification workflow.",
        "",
    ]
    for category in sorted(categories):
        lines.append(f"## {category.replace('-', ' ').title()}")
        lines.append("")
        for problem_id, title in categories[category]:
            lines.append(f"- **{problem_id} — {title}**")
        lines.append("")
    lines.extend(
        [
            "## Cross-cutting distinctions",
            "",
            "- **AI-specific failures:** hallucinated dependencies, false completion claims, prompt injection against tool-using agents, context loss, runaway tool loops, and MCP/plugin failure coupling.",
            "- **General engineering failures amplified by AI:** weak tests, insecure configuration, schema mistakes, oversized modules, deployment drift, stale documentation, and release inconsistency.",
            "- **Nontechnical-user risks:** fake completeness, placeholder UI, weak authentication, missing deployment verification, and inability to distinguish plausible output from working software.",
            "- **Experienced-developer risks:** review overhead, change-volume instability, multi-agent conflicts, context-selection errors, and excessive tool/cost usage.",
            "- **Not fully solvable by skills alone:** model hallucination elimination, guaranteed prompt-injection prevention, platform runtime bugs, hosted CI outages, and privileged production observability.",
        ]
    )
    (RESEARCH / "problem-taxonomy.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_limitations(evidence: list[dict[str, str]]) -> None:
    text = f"""# Research limitations

The current corpus contains {len(evidence)} evidence items and {len(PROBLEMS)} candidate problems. It is intentionally broad, but it is not a prevalence meta-analysis.

## Main limitations

- The Stack Overflow 2026 survey is large and current, but it is self-reported and its percentages should not be interpreted as causal defect rates.
- Public GitHub issues demonstrate real failure modes but are subject to reporting bias, duplicate reports, incomplete root-cause analysis, and product-specific behavior.
- Security reports differ in task selection, languages, models, scanners, and definitions of a failure. Their absolute percentages are not directly comparable.
- AI coding tools change quickly. Findings from 2025 are retained only when the study design or failure pattern remains informative.
- METR's early-2025 randomized study was deliberately narrow. The authors explicitly caution against generalizing its 19% slowdown result, and their 2026 update reports selection effects in newer measurements.
- The automated GitHub issue collector hit the authenticated Search API rate limit on 2026-10-25 before completing all configured queries. Public issue pages already retrieved remain cited, and the repository records the collector so the corpus can be refreshed later without hiding this blocker.
- Codex CLI is not installed on the active Windows PATH, so official Codex skill-installer behavior could not be tested locally in this session.
- PyPI DNS resolution failed while fetching optional development tools. The project therefore keeps core validation dependency-free and does not claim those optional tools were installed.

## Interpretation rule

The repository uses three evidence labels:

- **strong:** large current survey, repeated independent findings, official limitation plus independent evidence, or strong benchmark evidence.
- **moderate:** credible but narrower study, indirect evidence, or multiple concrete issue reports.
- **issue evidence / context:** useful concrete example or adoption context without a prevalence inference.

The prioritization phase uses evidence strength as one input rather than turning every reported issue into a separate skill.
"""
    (RESEARCH / "research-limitations.md").write_text(text, encoding="utf-8")


def main() -> int:
    RESEARCH.mkdir(parents=True, exist_ok=True)
    evidence = build_evidence()
    write_sources()
    write_methodology(evidence)
    write_evidence_csv(evidence)
    write_problems()
    write_taxonomy()
    write_limitations(evidence)
    print(f"Generated {len(evidence)} evidence items and {len(PROBLEMS)} candidate problems.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
