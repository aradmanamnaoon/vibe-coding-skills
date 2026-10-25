from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillHelperTests(unittest.TestCase):
    def test_secret_scanner_redacts_values(self) -> None:
        module = load_module(
            "scan_secrets",
            "skills/security/secret-leakage-detector/scripts/scan_secrets.py",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            secret = "sk-" + "A" * 30
            (root / "config.py").write_text(f'API_KEY = "{secret}"\n', encoding="utf-8")
            findings = module.scan(root)
            self.assertTrue(findings)
            serialized = repr(findings)
            self.assertNotIn(secret, serialized)
            self.assertEqual(findings[0]["path"], "config.py")

    def test_skipped_test_scanner_detects_multiple_frameworks(self) -> None:
        module = load_module(
            "find_skipped_tests",
            "skills/testing/test-quality-auditor/scripts/find_skipped_tests.py",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "test_sample.py").write_text(
                "@unittest.skip('later')\ndef test_x(): pass\n", encoding="utf-8"
            )
            (root / "sample.test.ts").write_text(
                "test.skip('later', () => {});\n", encoding="utf-8"
            )
            kinds = {finding["kind"] for finding in module.scan(root)}
            self.assertIn("unittest-skip", kinds)
            self.assertIn("jest-skip", kinds)

    def test_placeholder_scanner_finds_noop_and_not_implemented(self) -> None:
        module = load_module(
            "scan_placeholders",
            "skills/frontend/dead-feature-detector/scripts/scan_placeholders.py",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "App.tsx").write_text(
                "<button onClick={() => {}}>Run</button>\n// TODO implement\n",
                encoding="utf-8",
            )
            kinds = {finding["kind"] for finding in module.scan(root)}
            self.assertIn("empty-js-handler", kinds)
            self.assertIn("todo-fixme", kinds)

    def test_environment_key_discovery(self) -> None:
        module = load_module(
            "discover_env_keys",
            "skills/deployment/environment-config-auditor/scripts/discover_env_keys.py",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "settings.py").write_text(
                "import os\nURL = os.getenv('DATABASE_URL')\n", encoding="utf-8"
            )
            (root / "web.ts").write_text(
                "const key = process.env.PUBLIC_API_KEY;\n", encoding="utf-8"
            )
            discovered = module.discover(root)
            self.assertEqual(discovered["DATABASE_URL"], ["settings.py"])
            self.assertEqual(discovered["PUBLIC_API_KEY"], ["web.ts"])

    def test_python_cycle_scanner(self) -> None:
        module = load_module(
            "python_import_cycles",
            "skills/architecture/dependency-cycle-auditor/scripts/python_import_cycles.py",
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.py").write_text("import b\n", encoding="utf-8")
            (root / "b.py").write_text("import a\n", encoding="utf-8")
            found = module.cycles(module.graph(root))
            self.assertTrue(any(set(cycle) == {"a", "b"} for cycle in found))


if __name__ == "__main__":
    unittest.main()
