from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class SkillFormatError(ValueError):
    """Raised when a SKILL.md manifest is structurally invalid."""


@dataclass(frozen=True, slots=True)
class SkillRecord:
    name: str
    description: str
    category: str
    path: Path


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_front_matter(text: str, source: Path | None = None) -> dict[str, str]:
    """Parse the small YAML subset used by this repository's skill manifests."""
    lines = text.splitlines()
    label = str(source) if source is not None else "SKILL.md"
    if not lines or lines[0].strip() != "---":
        raise SkillFormatError(f"{label}: missing opening YAML front matter")
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise SkillFormatError(f"{label}: missing closing YAML front matter") from exc

    metadata: dict[str, str] = {}
    for line_number, raw in enumerate(lines[1:end], 2):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            raise SkillFormatError(f"{label}:{line_number}: expected 'key: value'")
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = _unquote(value.strip())
        if not key or not value:
            raise SkillFormatError(f"{label}:{line_number}: empty metadata key/value")
        if key in metadata:
            raise SkillFormatError(f"{label}:{line_number}: duplicate metadata key '{key}'")
        metadata[key] = value
    return metadata


def load_skill(skill_file: Path, skills_root: Path) -> SkillRecord:
    text = skill_file.read_text(encoding="utf-8")
    metadata = parse_front_matter(text, skill_file)
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not _SLUG_RE.fullmatch(name):
        raise SkillFormatError(f"{skill_file}: invalid skill name '{name}'")
    if len(description) < 24:
        raise SkillFormatError(f"{skill_file}: description is too short to be actionable")
    if skill_file.parent.name != name:
        raise SkillFormatError(
            f"{skill_file}: directory '{skill_file.parent.name}' must match skill name '{name}'"
        )

    relative = skill_file.relative_to(skills_root)
    category = relative.parts[0] if len(relative.parts) > 2 else "uncategorized"
    return SkillRecord(name=name, description=description, category=category, path=skill_file.parent)


def discover_skills(skills_root: Path) -> list[SkillRecord]:
    if not skills_root.exists():
        return []
    records: list[SkillRecord] = []
    names: set[str] = set()
    for skill_file in sorted(skills_root.rglob("SKILL.md")):
        record = load_skill(skill_file, skills_root)
        if record.name in names:
            raise SkillFormatError(f"duplicate skill name: {record.name}")
        names.add(record.name)
        records.append(record)
    return records

