from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


PATTERNS = {
    "pytest-skip": re.compile(r"\bpytest\.(?:skip|mark\.skip|mark\.skipif)\b"),
    "unittest-skip": re.compile(r"@unittest\.(?:skip|skipIf|skipUnless)\b"),
    "jest-skip": re.compile(r"\b(?:it|test|describe)\.skip\s*\("),
    "vitest-xit": re.compile(r"\b(?:xit|xdescribe)\s*\("),
    "junit-disabled": re.compile(r"@Disabled\b"),
}

EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".kt"}


def scan(root: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in {".git", ".venv", "node_modules", "dist", "build"} for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(lines, 1):
            for kind, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(
                        {"path": path.relative_to(root).as_posix(), "line": line_number, "kind": kind}
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    results = scan(Path(args.root).resolve())
    print(json.dumps(results, indent=2))
    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())

