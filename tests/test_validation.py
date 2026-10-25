from pathlib import Path
import tempfile
import unittest

from vibe_skills.validation import validate_repository


class ValidationTests(unittest.TestCase):
    def test_validation_reports_missing_operational_sections(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_dir = root / "testing" / "sample-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\n"
                "name: sample-skill\n"
                "description: Detect a representative issue with a reproducible workflow.\n"
                "---\n\n"
                "# Purpose\n"
                "Only purpose exists.\n",
                encoding="utf-8",
            )
            issues = validate_repository(root)
            self.assertTrue(any("When to activate" in issue.message for issue in issues))
            self.assertTrue(any("Safety restrictions" in issue.message for issue in issues))


if __name__ == "__main__":
    unittest.main()

