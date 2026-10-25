from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


PATTERNS = [
    re.compile(r"""os\.environ\[\s*["']([A-Z][A-Z0-9_]*)["']\s*\]"""),
    re.compile(r"""os\.getenv\(\s*["']([A-Z][A-Z0-9_]*)["']"""),
    re.compile(r"""\bprocess\.env\.([A-Z][A-Z0-9_]*)\b"""),
    re.compile(r"""\bprocess\.env\[\s*["']([A-Z][A-Z0-9_]*)["']\s*\]"""),
    re.compile(r"""\bimport\.meta\.env\.([A-Z][A-Z0-9_]*)\b"""),
]

EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}


def discover(root: Path) -> dict[str, list[str]]:
    found: dict[str, set[str]] = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in {".git", ".venv", "node_modules", "dist", "build"} for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in PATTERNS:
            for match in pattern.finditer(text):
                found.setdefault(match.group(1), set()).add(path.relative_to(root).as_posix())
    return {key: sorted(paths) for key, paths in sorted(found.items())}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    print(json.dumps(discover(Path(args.root).resolve()), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

