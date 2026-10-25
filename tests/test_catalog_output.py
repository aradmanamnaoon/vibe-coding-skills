from pathlib import Path
import tempfile
import unittest

from vibe_skills.catalog_output import catalog_rows, render_markdown


class CatalogOutputTests(unittest.TestCase):
    def test_catalog_reports_helpers_and_install_command(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "skills"
            skill = root / "testing" / "sample-skill"
            scripts = skill / "scripts"
            scripts.mkdir(parents=True)
            (scripts / "check.py").write_text("print('ok')\n", encoding="utf-8")
            (skill / "SKILL.md").write_text(
                "---\n"
                "name: sample-skill\n"
                "description: Check a sample condition with repeatable validation steps.\n"
                "---\n\n"
                "# Purpose\nx\n"
                "# When to activate\nx\n"
                "# When not to activate\nx\n"
                "# Preconditions\nx\n"
                "# Required inputs\nx\n"
                "# Workflow\nx\n"
                "# Relevant tools\nx\n"
                "# Safety restrictions\nx\n"
                "# Validation\nx\n"
                "# Expected output\nx\n"
                "# Failure handling\nx\n"
                "# Completion criteria\nx\n",
                encoding="utf-8",
            )
            rows = catalog_rows(root)
            self.assertEqual(len(rows), 1)
            self.assertTrue(rows[0]["has_scripts"])
            self.assertTrue(rows[0]["structurally_valid"])
            rendered = render_markdown(rows)
            self.assertIn("python -m vibe_skills install sample-skill", rendered)


if __name__ == "__main__":
    unittest.main()
