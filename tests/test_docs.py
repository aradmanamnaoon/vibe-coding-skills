from pathlib import Path
import importlib.util
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_checker():
    path = ROOT / "scripts" / "check_docs.py"
    spec = importlib.util.spec_from_file_location("check_docs", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DocumentationTests(unittest.TestCase):
    def test_reports_missing_local_link_but_ignores_web_link(self) -> None:
        module = load_checker()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[missing](docs/missing.md) [web](https://example.com)\\n",
                encoding="utf-8",
            )
            issues = module.check(root)
            self.assertEqual(len(issues), 1)
            self.assertIn("docs/missing.md", issues[0])


if __name__ == "__main__":
    unittest.main()

