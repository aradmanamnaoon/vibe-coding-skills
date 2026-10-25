from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .catalog import SkillFormatError, discover_skills
from .catalog_output import write_catalog
from .installer import InstallError, install_skill, remove_skill, update_skill
from .validation import validate_repository


def _repo_root() -> Path:
    return Path.cwd()


def _skills_root(args: argparse.Namespace) -> Path:
    return Path(args.source).resolve() if args.source else (_repo_root() / "skills").resolve()


def _records(args: argparse.Namespace):
    return discover_skills(_skills_root(args))


def _find(args: argparse.Namespace, name: str):
    for record in _records(args):
        if record.name == name:
            return record
    raise InstallError(f"unknown skill: {name}")


def cmd_list(args: argparse.Namespace) -> int:
    records = _records(args)
    if not records:
        print("No skills found.")
        return 0
    for record in records:
        print(f"{record.name}\t{record.category}\t{record.description}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    query = args.query.casefold()
    matches = [
        record
        for record in _records(args)
        if query in record.name.casefold()
        or query in record.description.casefold()
        or query in record.category.casefold()
    ]
    for record in matches:
        print(f"{record.name}\t{record.category}\t{record.description}")
    return 0 if matches else 1


def cmd_install(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    selected = _records(args)
    if args.name:
        selected = [_find(args, args.name)]
    elif args.category:
        selected = [record for record in selected if record.category == args.category]
    if not selected:
        raise InstallError("no skills matched the requested selection")
    for record in selected:
        target = install_skill(record, destination, dry_run=args.dry_run)
        prefix = "Would install" if args.dry_run else "Installed"
        print(f"{prefix} {record.name} -> {target}")
    return 0


def cmd_remove(args: argparse.Namespace) -> int:
    target = remove_skill(args.name, Path(args.destination), dry_run=args.dry_run)
    prefix = "Would remove" if args.dry_run else "Removed"
    print(f"{prefix} {args.name} from {target}")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    selected = _records(args)
    if args.name:
        selected = [_find(args, args.name)]
    elif args.category:
        selected = [record for record in selected if record.category == args.category]
    if not selected:
        raise InstallError("no skills matched the requested selection")
    for record in selected:
        target = update_skill(record, destination, dry_run=args.dry_run)
        prefix = "Would update" if args.dry_run else "Updated"
        print(f"{prefix} {record.name} -> {target}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    issues = validate_repository(_skills_root(args))
    if not issues:
        print("Skill validation passed.")
        return 0
    for issue in issues:
        print(f"{issue.path}: {issue.message}", file=sys.stderr)
    return 1


def cmd_doctor(args: argparse.Namespace) -> int:
    root = _skills_root(args)
    destination = Path(args.destination).resolve()
    print(f"Python: {sys.version.split()[0]}")
    print(f"Skill source: {root}")
    print(f"Skill source exists: {root.exists()}")
    print(f"Install destination: {destination}")
    print(f"Discovered skills: {len(discover_skills(root))}")
    issues = validate_repository(root)
    print(f"Validation issues: {len(issues)}")
    return 1 if issues else 0


def cmd_catalog(args: argparse.Namespace) -> int:
    write_catalog(
        _skills_root(args),
        Path(args.markdown).resolve(),
        Path(args.json).resolve(),
    )
    print(f"Wrote {Path(args.markdown).resolve()}")
    print(f"Wrote {Path(args.json).resolve()}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vibe-skills")
    parser.add_argument("--source", help="Skill source directory; defaults to ./skills")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List available skills").set_defaults(func=cmd_list)
    search = sub.add_parser("search", help="Search skills by name, category, or description")
    search.add_argument("query")
    search.set_defaults(func=cmd_search)

    install = sub.add_parser("install", help="Install one, a category, or all skills")
    selection = install.add_mutually_exclusive_group()
    selection.add_argument("name", nargs="?")
    selection.add_argument("--category")
    install.add_argument("--destination", default=".agents/skills")
    install.add_argument("--dry-run", action="store_true")
    install.set_defaults(func=cmd_install)

    remove = sub.add_parser("remove", help="Remove an installer-managed skill")
    remove.add_argument("name")
    remove.add_argument("--destination", default=".agents/skills")
    remove.add_argument("--dry-run", action="store_true")
    remove.set_defaults(func=cmd_remove)

    update = sub.add_parser("update", help="Update installer-managed skills without overwriting local edits")
    update_selection = update.add_mutually_exclusive_group()
    update_selection.add_argument("name", nargs="?")
    update_selection.add_argument("--category")
    update.add_argument("--destination", default=".agents/skills")
    update.add_argument("--dry-run", action="store_true")
    update.set_defaults(func=cmd_update)

    sub.add_parser("validate", help="Validate all source skills").set_defaults(func=cmd_validate)
    doctor = sub.add_parser("doctor", help="Check repository and install-path health")
    doctor.add_argument("--destination", default=".agents/skills")
    doctor.set_defaults(func=cmd_doctor)

    catalog = sub.add_parser("catalog", help="Generate Markdown and JSON skill catalogs")
    catalog.add_argument("--markdown", default="catalog/SKILLS.md")
    catalog.add_argument("--json", default="catalog/skills.json")
    catalog.set_defaults(func=cmd_catalog)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (SkillFormatError, InstallError, OSError) as exc:
        parser.error(str(exc))
        return 2

