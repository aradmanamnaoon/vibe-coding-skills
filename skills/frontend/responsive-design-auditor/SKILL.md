---
name: responsive-design-auditor
description: Verify changed UI across representative viewport widths for overflow, clipping, reflow, navigation, touch targets, and content priority. Use for frontend layout changes.
---

# Purpose

Catch desktop-only layouts and breakpoint regressions with observable viewport checks.

# When to activate

Layout/navigation/component changes can respond to viewport size.

# When not to activate

Backend-only change or a non-layout style token change is fully covered by existing visual tests.

# Preconditions

- Read applicable repository instructions before edits.
- Preserve unrelated working-tree changes and establish a baseline when the workflow can modify code.
- Identify which tools and environments are actually available; do not claim unavailable checks ran.

# Required inputs

- Runnable UI
- Critical routes/components
- Supported target widths/devices

# Workflow

1. Choose representative narrow, medium, and wide widths from product breakpoints or common constraints rather than testing dozens of devices.
2. At each width, inspect horizontal overflow, clipped content, overlapping controls, fixed/sticky elements, long text, tables/media, dialogs, and navigation.
3. Verify interactive targets remain reachable and appropriately sized without hover-only behavior.
4. Test text zoom/reflow where relevant to the changed component.
5. Prefer intrinsic/flexible layout fixes over adding one-off breakpoint patches.
6. Repeat the critical interaction at the narrowest supported width.
7. Record browser-specific checks separately from responsive checks.

# Relevant tools

Browser/Playwright or equivalent, devtools layout metrics, screenshots as supplemental evidence.

# Safety restrictions

Do not hide required content/actions at small widths merely to remove overflow.

# Validation

- No unintended horizontal scroll/clipping occurs in changed flows.
- Critical actions remain visible/reachable at representative widths.
- The narrowest flow completes successfully.

# Expected output

- Viewport matrix
- Layout/interactivity findings
- Fix rationale
- Browser evidence

# Failure handling

If browser automation is unavailable, inspect CSS/layout constraints and mark actual viewport execution pending.

# Completion criteria

The skill is complete only when every applicable validation item above has observed evidence or is explicitly marked not executed with the concrete blocker. Do not replace missing evidence with confidence language.

# Research mapping

This skill was selected from research problems: P036. See research/vibe-coding-problems.md and research/problem-evidence.csv in the Vibe Coding Skills repository.
