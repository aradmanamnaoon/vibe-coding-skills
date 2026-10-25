from __future__ import annotations

import argparse
import ast
from pathlib import Path


SKIP_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__"}
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".toml",
    ".yml",
    ".yaml",
    ".json",
    ".ps1",
    ".txt",
}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.casefold() in TEXT_SUFFIXES or path.name in {
            "LICENSE",
            ".gitignore",
            ".gitattributes",
        }:
            yield path


def lint(root: Path) -> list[str]:
    issues: list[str] = []
    for path in iter_text_files(root):
        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as exc:
            issues.append(f"{relative}: unreadable UTF-8 text: {exc}")
            continue

        if text and not text.endswith("\n"):
            issues.append(f"{relative}: missing final newline")

        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip(" \t") != line:
                issues.append(f"{relative}:{line_number}: trailing whitespace")

        if path.suffix.casefold() == ".py":
            try:
                ast.parse(text, filename=relative)
            except SyntaxError as exc:
                issues.append(
                    f"{relative}:{exc.lineno or 0}: Python syntax error: {exc.msg}"
                )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    issues = lint(root)
    for issue in issues:
        print(issue)
    if issues:
        print(f"Repository lint failed with {len(issues)} issue(s).")
        return 1
    print("Repository lint passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
