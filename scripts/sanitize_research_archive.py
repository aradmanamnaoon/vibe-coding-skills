from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


SECRET_ASSIGNMENT = re.compile(
    r"(?i)(\b(?:api[_-]?key|secret|token|password)\b\s*[:=]\s*['\"]?)"
    r"([^\\\s'\"<>]{12,})"
)


def sanitize_text(text: str) -> tuple[str, int]:
    return SECRET_ASSIGNMENT.subn(r"\1<REDACTED_BY_RESEARCH_ARCHIVE>", text)


def sanitize_payload(value):
    if isinstance(value, dict):
        return {
            key: sanitize_payload(item)
            for key, item in value.items()
            if key.casefold() != "body"
        }
    if isinstance(value, list):
        return [sanitize_payload(item) for item in value]
    if isinstance(value, str):
        return sanitize_text(value)[0]
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    original = path.read_text(encoding="utf-8-sig")
    payload = json.loads(original)
    sanitized = sanitize_payload(payload)
    path.write_text(
        json.dumps(sanitized, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Removed issue bodies and sanitized credential-shaped metadata in {path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
