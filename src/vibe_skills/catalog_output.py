from __future__ import annotations

import json
from pathlib import Path

from .catalog import discover_skills
from .validation import validate_repository


def catalog_rows(skills_root: Path) -> list[dict[str, object]]:
    issues = validate_repository(skills_root)
    issue_paths = {issue.path.resolve() for issue in issues}
    rows: list[dict[str, object]] = []
    for record in discover_skills(skills_root):
        helper_dir = record.path / "scripts"
        rows.append(
            {
                "name": record.name,
                "category": record.category,
                "description": record.description,
                "source": record.path.relative_to(skills_root.parent).as_posix(),
                "has_scripts": helper_dir.is_dir() and any(helper_dir.iterdir()),
                "structurally_valid": (record.path / "SKILL.md").resolve() not in issue_paths,
                "install": f"python -m vibe_skills install {record.name}",
            }
        )
    return rows


def render_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Skill catalog",
        "",
        f"Generated from the validated source tree. **{len(rows)} skills** are listed.",
        "",
        "| Skill | Category | Trigger / purpose | Helper | Structural status | Install |",
        "|---|---|---|:---:|:---:|---|",
    ]
    for row in rows:
        name = str(row["name"])
        category = str(row["category"])
        description = str(row["description"]).replace("|", "/")
        helper = "yes" if row["has_scripts"] else "-"
        status = "valid" if row["structurally_valid"] else "invalid"
        install = str(row["install"])
        source = str(row["source"])
        lines.append(
            f"| [{name}](../{source}/SKILL.md) | {category} | {description} | {helper} | {status} | {install} |"
        )
    lines.extend(
        [
            "",
            "Behavioral and agent-execution status is intentionally separate from structural status. See docs/validation-report.md.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_catalog(skills_root: Path, markdown_path: Path, json_path: Path) -> None:
    rows = catalog_rows(skills_root)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_markdown(rows), encoding="utf-8")
    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")

