from pathlib import Path
import tempfile
import unittest

from vibe_skills.catalog import SkillFormatError, discover_skills, parse_front_matter


def _write_skill(root: Path, category: str, name: str, description: str) -> Path:
    skill_dir = root / category / name
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n\n# Purpose\n",
        encoding="utf-8",
    )
    return skill_file


class CatalogTests(unittest.TestCase):
    def test_discover_skills_reads_category_and_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _write_skill(
                root,
                "debugging",
                "root-cause-debugger",
                "Diagnose recurring failures using reproducible evidence and focused verification.",
            )
            records = discover_skills(root)
            self.assertEqual(
                [(record.name, record.category) for record in records],
                [("root-cause-debugger", "debugging")],
            )

    def test_invalid_name_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _write_skill(
                root,
                "debugging",
                "Bad_Name",
                "A sufficiently long skill description for validation.",
            )
            with self.assertRaisesRegex(SkillFormatError, "invalid skill name"):
                discover_skills(root)

    def test_front_matter_requires_closing_delimiter(self) -> None:
        with self.assertRaisesRegex(SkillFormatError, "closing"):
            parse_front_matter("---\nname: test\n")


if __name__ == "__main__":
    unittest.main()

