from __future__ import annotations

import argparse
from pathlib import Path
import re


SECRET_ASSIGNMENT = re.compile(
    r"(?i)(\b(?:api[_-]?key|secret|token|password)\b\s*[:=]\s*['\"]?)"
    r"([^\s'\"<>]{12,})"
)


def sanitize_text(text: str) -> tuple[str, int]:
    return SECRET_ASSIGNMENT.subn(r"\1<REDACTED_BY_RESEARCH_ARCHIVE>", text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    original = path.read_text(encoding="utf-8-sig")
    sanitized, count = sanitize_text(original)
    path.write_text(sanitized, encoding="utf-8")
    print(f"Redacted {count} credential-like assignments from {path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
