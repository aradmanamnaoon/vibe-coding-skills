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
        required_phrases = [
            "Purpose",
            "When to activate",
            "When not to activate",
            "Preconditions",
            "Required inputs",
            "Workflow",
            "Validation",
            "Expected output",
            "Failure handling",
            "Completion criteria",
        ]
        for phrase in required_phrases:
            if phrase.lower() not in text.lower():
                issues.append(ValidationIssue(manifest, f"missing required section: {phrase}"))

        for link in _LINK_RE.findall(text):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            local = (manifest.parent / link.split("#", 1)[0]).resolve()
            if not local.exists():
                issues.append(ValidationIssue(manifest, f"broken local link: {link}"))
    return issues

