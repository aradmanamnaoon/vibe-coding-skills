from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


PATTERNS = {
    "todo-fixme": re.compile(r"\b(?:TODO|FIXME)\b", re.IGNORECASE),
    "not-implemented": re.compile(r"\b(?:NotImplementedError|not implemented|coming soon)\b", re.IGNORECASE),
    "empty-js-handler": re.compile(r"(?:onClick|onSubmit|onChange)\s*=\s*\{\s*\(\s*\)\s*=>\s*\{\s*\}\s*\}"),
    "dummy-link": re.compile(r"""href\s*=\s*["']#["']"""),
    "placeholder-alert": re.compile(r"\balert\s*\(\s*['\"][^'\"]*(?:todo|coming soon|not implemented)", re.IGNORECASE),
}

EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html"}


def scan(root: Path) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in {".git", ".venv", "node_modules", "dist", "build"} for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(lines, 1):
            for kind, pattern in PATTERNS.items():
                if pattern.search(line):
                    results.append(
                        {"path": path.relative_to(root).as_posix(), "line": number, "kind": kind}
                    )
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    findings = scan(Path(args.root).resolve())
    print(json.dumps(findings, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

