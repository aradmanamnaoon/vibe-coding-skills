# Skill opportunities and prioritization

Scores use the requested 100-point framework. Component scores are bounded by their weights and are engineering judgments informed by the evidence corpus; they are not prevalence percentages.

| Skill | Problems | Severity /20 | Recurrence /15 | Solvability /20 | Benefit /15 | Feasibility /10 | Uniqueness /10 | Testability /10 | Total | Selection rationale |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| completion-claims-auditor | P044, P039 | 20 | 15 | 20 | 15 | 10 | 10 | 10 | **100** | Directly addresses a defining vibe-coding failure with strong trust evidence and exceptionally clear testability. |
| dead-feature-detector | P039, P044 | 20 | 15 | 20 | 15 | 10 | 10 | 10 | **100** | Directly targets fake-completeness risk for vibe coders; highly distinctive, testable, and high benefit. |
| requirement-traceability-auditor | P045, P044 | 20 | 15 | 20 | 15 | 10 | 10 | 10 | **100** | Large-prompt omission is central to autonomous coding; deterministic matrices make it uniquely high-value and testable. |
| dependency-grounding-auditor | P002, P003, P052 | 19 | 15 | 20 | 15 | 10 | 9 | 10 | **98** | Survey hallucination rates and large dependency-grounding evidence make this highly supported and uniquely skill-suited. |
| existing-work-preservation | P048, P010 | 20 | 14 | 20 | 15 | 10 | 9 | 10 | **98** | Destructive rewrites are a core autonomous-agent risk; baseline evidence makes preservation enforceable. |
| loop-breaker | P007, P050 | 19 | 15 | 20 | 14 | 10 | 10 | 10 | **98** | Multiple concrete agent issues show infinite retries and false-positive loop detection; a progress-aware workflow is distinctive and directly testable. |
| regression-detector | P009, P048 | 20 | 15 | 20 | 15 | 10 | 8 | 10 | **98** | DORA stability evidence and common validation behavior make regression control high impact and strongly testable. |
| root-cause-debugger | P006, P008, P011 | 20 | 15 | 20 | 15 | 10 | 8 | 10 | **98** | Strong survey evidence for poor debugging paths; highly solvable and testable with seeded faults. |
| scope-drift-guard | P046, P010 | 18 | 14 | 20 | 15 | 10 | 10 | 10 | **97** | Scope drift is concrete, high-cost, and deterministic to audit from Git state. |
| secret-leakage-detector | P013 | 20 | 15 | 20 | 15 | 10 | 7 | 10 | **97** | Secret exposure is high severity and deterministic scanning is feasible; uniqueness is lower because scanners already exist. |
| agent-tool-trust-auditor | P020, P055 | 20 | 15 | 18 | 15 | 9 | 10 | 9 | **96** | Official prompt-injection guidance plus MCP failure evidence make this distinctive and high impact; full prevention needs platform support. |
| authorization-boundary-auditor | P015 | 20 | 14 | 19 | 15 | 9 | 9 | 10 | **96** | Authorization is critical, distinct from authentication, and supports strong multi-user fixtures. |
| input-validation-auditor | P017 | 19 | 14 | 20 | 15 | 10 | 8 | 10 | **96** | Strong security evidence and highly testable boundary-value workflow. |
| project-context-recovery | P047 | 18 | 14 | 20 | 15 | 10 | 10 | 9 | **96** | Session continuity failures are observed across agent products; repository-first recovery is portable and distinctive. |
| test-quality-auditor | P022, P023, P026 | 18 | 14 | 20 | 15 | 10 | 9 | 10 | **96** | Concrete skipped-test issue plus common test delegation; strong deterministic review opportunities. |
| api-contract-auditor | P025, P003 | 18 | 14 | 20 | 15 | 10 | 8 | 10 | **95** | Contract drift is common in AI changes and highly deterministic to test. |
| environment-config-auditor | P041 | 18 | 14 | 20 | 15 | 10 | 8 | 10 | **95** | Strong deployment relevance and deterministic static/runtime checks make this high value. |
| injection-risk-auditor | P016 | 20 | 14 | 19 | 15 | 9 | 8 | 10 | **95** | Common critical vulnerability class with clear deterministic and integration validation paths. |
| missing-test-detector | P021 | 18 | 15 | 20 | 15 | 10 | 7 | 10 | **95** | Testing is heavily delegated to AI and verification is common; existing tooling lowers uniqueness but the behavior map is valuable. |
| reproduction-builder | P012 | 18 | 14 | 20 | 14 | 10 | 9 | 10 | **95** | Verification behavior is common in survey data and reproduction is a prerequisite for high-quality debugging; easy to fixture-test. |
| authentication-security-auditor | P014 | 20 | 14 | 19 | 15 | 9 | 8 | 9 | **94** | Authentication failures are critical and testable, though provider-specific behavior limits full portability. |
| environment-parity-auditor | P040, P054 | 19 | 14 | 19 | 15 | 9 | 8 | 10 | **94** | Local-vs-production failure is high-impact and reproducibility controls are strongly skill-suited. |
| mcp-reliability-auditor | P055, P007 | 19 | 14 | 19 | 15 | 8 | 10 | 9 | **94** | Multiple 2026 coding-agent incidents show stalls and spawn/retry loops; a dedicated reliability workflow is distinctive. |
| dependency-vulnerability-auditor | P018, P052 | 20 | 14 | 18 | 15 | 9 | 8 | 9 | **93** | Security and supply-chain evidence is strong; external advisory freshness makes full offline validation impossible. |
| ci-failure-investigator | P042 | 18 | 14 | 19 | 14 | 9 | 8 | 10 | **92** | CI diagnosis is recurrent and operationally bounded; hosted runner limits reduce feasibility slightly. |
| security-misconfiguration-auditor | P019, P040 | 20 | 14 | 18 | 14 | 9 | 8 | 9 | **92** | Security misconfiguration is critical and recurring, with some platform-specific limitations. |
| ui-flow-verifier | P024, P039 | 19 | 14 | 18 | 15 | 8 | 8 | 10 | **92** | Product completeness evidence supports E2E verification; external browser availability lowers feasibility. |
| data-consistency-auditor | P034 | 20 | 12 | 18 | 15 | 8 | 9 | 9 | **91** | Concurrency failures are critical with a strong invariant-based workflow, though reproduction can be environment-sensitive. |
| documentation-accuracy-auditor | P051 | 16 | 14 | 20 | 14 | 10 | 7 | 10 | **91** | Documentation drift is common and highly testable, though many tools already solve basic link checking. |
| migration-safety-reviewer | P033 | 20 | 12 | 18 | 15 | 8 | 9 | 9 | **91** | High severity and clear workflow; real production scale remains an external factor. |
| production-readiness-auditor | P027, P043 | 20 | 13 | 18 | 15 | 8 | 8 | 9 | **91** | Deployment completion failures are severe; full production evidence may require unavailable platform access. |
| release-verification-agent | P053, P027 | 18 | 12 | 19 | 14 | 8 | 10 | 10 | **91** | Release verification is distinct from generic CI and highly evidence-oriented; platform constraints lower recurrence score. |
| cross-platform-readiness-auditor | P054 | 16 | 13 | 19 | 14 | 9 | 9 | 9 | **89** | Cross-platform incidents are concrete and deterministic in many areas, with true target-host validation sometimes external. |
| multi-agent-integration-reviewer | P049 | 17 | 11 | 19 | 14 | 9 | 10 | 9 | **89** | Parallel-agent use is growing and semantic merge review is under-served; recurrence evidence is less broad. |
| database-schema-reviewer | P031 | 19 | 12 | 18 | 14 | 8 | 8 | 9 | **88** | Schema mistakes can be severe; domain-specific invariants lower generic automation. |
| integration-reality-checker | P023, P027 | 18 | 13 | 18 | 14 | 8 | 8 | 9 | **88** | Mocks are a recurrent source of false confidence; feasibility varies with external services. |
| accessibility-auditor | P037 | 17 | 13 | 19 | 14 | 8 | 7 | 9 | **87** | Accessibility failures are common and important; established tools lower uniqueness but manual workflow adds value. |
| ux-state-completeness-auditor | P038 | 15 | 12 | 18 | 13 | 9 | 8 | 9 | **84** | Useful for nontechnical builders and highly testable, though product copy contains subjective decisions. |
| architecture-complexity-auditor | P028, P032 | 16 | 12 | 17 | 13 | 8 | 9 | 8 | **83** | Architecture risk is real but more judgment-dependent; skill enforces evidence and incremental scope. |
| dependency-cycle-auditor | P029 | 15 | 11 | 18 | 12 | 9 | 8 | 10 | **83** | Narrow deterministic problem with good testability; recurrence is lower than top-tier failures. |
| responsive-design-auditor | P036 | 15 | 12 | 18 | 13 | 8 | 7 | 9 | **82** | Common UI issue and testable with browser tooling; less severe than security/reliability failures. |
| token-efficient-workflow | P050 | 10 | 14 | 18 | 12 | 10 | 9 | 8 | **81** | Cost/limit survey evidence is strong, but optimization benefit is secondary to correctness and harder to benchmark portably. |

Selected: **42 original skills**. The count is inside the 30-50 target and reflects consolidation of overlapping candidates.

Selection rule: retain a candidate when it has a recognizable trigger, a bounded procedure, an observable result, a credible validation path, and adds more than generic advice. Lower-scoring ideas can remain in the roadmap rather than being split into superficial skills.
