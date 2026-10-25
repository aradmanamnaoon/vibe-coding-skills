from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def _load():
    path = ROOT / "scripts" / "sanitize_research_archive.py"
    spec = importlib.util.spec_from_file_location("sanitize_research_archive", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ResearchSanitizerTests(unittest.TestCase):
    def test_redacts_assignment_value_without_echoing_it(self) -> None:
        module = _load()
        key_name = "api" + "Key"
        fixture_value = "abcdefghijklmnopqrstuvwxyz" + "123456"
        original = f'{key_name} = "{fixture_value}"\n'
        sanitized, count = module.sanitize_text(original)
        self.assertEqual(count, 1)
        self.assertNotIn(fixture_value, sanitized)
        self.assertIn("<REDACTED_BY_RESEARCH_ARCHIVE>", sanitized)


if __name__ == "__main__":
    unittest.main()
