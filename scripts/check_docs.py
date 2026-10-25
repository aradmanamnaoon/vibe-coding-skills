from __future__ import annotations

import argparse
from pathlib import Path
import re


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def check(root: Path) -> list[str]:
    issues: list[str] = []
    for path in root.rglob("*.md"):
        if any(part in {".git", ".venv", "node_modules"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                issues.append(f"{path.relative_to(root)}: broken local link -> {target}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    issues = check(root)
    for issue in issues:
        print(issue)
    if issues:
        print(f"Documentation check failed with {len(issues)} broken local links.")
        return 1
    print("Documentation local-link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

