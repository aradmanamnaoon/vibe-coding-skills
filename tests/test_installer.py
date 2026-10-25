from pathlib import Path
import tempfile
import unittest

from vibe_skills.catalog import SkillRecord
from vibe_skills.installer import InstallError, install_skill, remove_skill


def _record(tmp_path: Path) -> SkillRecord:
    source = tmp_path / "source" / "safe-skill"
    source.mkdir(parents=True)
    (source / "SKILL.md").write_text("content", encoding="utf-8")
    return SkillRecord(
        name="safe-skill",
        description="A long enough description for this installation fixture.",
        category="testing",
        path=source,
    )


class InstallerTests(unittest.TestCase):
    def test_dry_run_does_not_create_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            target = install_skill(_record(root), destination, dry_run=True)
            self.assertEqual(target, destination.resolve() / "safe-skill")
            self.assertFalse(destination.exists())

    def test_install_refuses_existing_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            record = _record(root)
            install_skill(record, destination)
            with self.assertRaisesRegex(InstallError, "already exists"):
                install_skill(record, destination)

    def test_remove_refuses_unmanaged_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            target = destination / "safe-skill"
            target.mkdir(parents=True)
            with self.assertRaisesRegex(InstallError, "unmanaged"):
                remove_skill("safe-skill", destination)

    def test_managed_install_and_remove_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            record = _record(root)
            target = install_skill(record, destination)
            self.assertTrue((target / "SKILL.md").exists())
            removed = remove_skill(record.name, destination)
            self.assertEqual(removed, target)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()

