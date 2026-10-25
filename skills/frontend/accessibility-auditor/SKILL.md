---
name: accessibility-auditor
description: Audit interactive UI for semantic structure, keyboard/focus behavior, accessible names, contrast, motion, and touch targets. Use for UI changes or accessibility review.
---

# Purpose

Combine automated accessibility checks with manual interaction checks that automation misses.

# When to activate

A user-facing interface or component is added/changed.

# When not to activate

Non-visual backend-only work has no rendered UI impact.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Runnable UI or component preview
- Target flows/components
- Supported browser/a11y tools

# Workflow

1. Use semantic elements and the accessibility tree to inspect roles, names, relationships, headings, landmarks, labels, and live/error messaging.
2. Run an automated accessibility scanner when available and retain exact rule findings.
3. Keyboard-test the critical flow: logical order, visible focus, no traps, operable controls, dialogs/menus focus management, skip/navigation behavior where relevant.
4. Check contrast, non-color cues, motion/reduced-motion, zoom/reflow, and target sizing for changed UI.
5. Test form validation and errors for programmatic association and focus/announcement behavior.
6. Fix root semantics before adding ARIA workarounds.
7. Re-run automated and manual checks and record what automation cannot establish.

# Relevant tools

Browser accessibility tree, axe or equivalent, keyboard, responsive browser tools.

# Safety restrictions

Do not claim full WCAG conformance from automated scans alone.

# Validation

- No known critical automated violation remains in the changed scope.
- Critical flow is keyboard-operable with visible/manageable focus.
- Manual checks are reported separately from automated scanner results.

# Expected output

- Automated findings
- Keyboard/focus results
- Manual visual checks
- Residual WCAG review items

# Failure handling

If no browser/scanner is available, perform source-level semantic checks and explicitly mark interactive/contrast verification not executed.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P037. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
