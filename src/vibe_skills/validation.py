from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .catalog import SkillFormatError, discover_skills


_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    path: Path
    message: str


def validate_repository(skills_root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    try:
        records = discover_skills(skills_root)
    except SkillFormatError as exc:
        return [ValidationIssue(skills_root, str(exc))]

    for record in records:
        manifest = record.path / "SKILL.md"
        text = manifest.read_text(encoding="utf-8")
        headings = {
            line.strip().casefold()
            for line in text.splitlines()
            if line.strip().startswith("#")
        }
        required_headings = {
            "# purpose": "Purpose",
            "# when to activate": "When to activate",
            "# when not to activate": "When not to activate",
            "# preconditions": "Preconditions",
            "# required inputs": "Required inputs",
            "# workflow": "Workflow",
            "# relevant tools": "Relevant tools",
            "# safety restrictions": "Safety restrictions",
            "# validation": "Validation",
            "# expected output": "Expected output",
            "# failure handling": "Failure handling",
            "# completion criteria": "Completion criteria",
        }
        for heading, label in required_headings.items():
            if heading not in headings:
                issues.append(
                    ValidationIssue(
                        manifest,
                        f"missing required section: {label}",
                    )
                )

        for link in _LINK_RE.findall(text):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            local = (manifest.parent / link.split("#", 1)[0]).resolve()
            if not local.exists():
                issues.append(ValidationIssue(manifest, f"broken local link: {link}"))
    return issues

