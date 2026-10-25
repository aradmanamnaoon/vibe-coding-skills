from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_linter():
    path = ROOT / "scripts" / "lint_repository.py"
    spec = importlib.util.spec_from_file_location("lint_repository", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositoryLintTests(unittest.TestCase):
    def test_reports_trailing_whitespace_and_python_syntax(self) -> None:
        module = load_linter()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "bad.md").write_text("bad  \n", encoding="utf-8")
            (root / "bad.py").write_text("def broken(:\n", encoding="utf-8")
            issues = module.lint(root)
            self.assertTrue(any("trailing whitespace" in issue for issue in issues))
            self.assertTrue(any("Python syntax error" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
