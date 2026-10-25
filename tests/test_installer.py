from pathlib import Path
import tempfile
import unittest

from vibe_skills.catalog import SkillRecord
from vibe_skills.installer import InstallError, install_skill, remove_skill, update_skill


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

    def test_update_refuses_locally_modified_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            record = _record(root)
            target = install_skill(record, destination)
            (target / "SKILL.md").write_text("local edit", encoding="utf-8")
            with self.assertRaisesRegex(InstallError, "locally modified"):
                update_skill(record, destination)
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "local edit")

    def test_update_replaces_unchanged_managed_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            record = _record(root)
            target = install_skill(record, destination)
            (record.path / "SKILL.md").write_text("new source content", encoding="utf-8")
            update_skill(record, destination)
            self.assertEqual(
                (target / "SKILL.md").read_text(encoding="utf-8"),
                "new source content",
            )

    def test_path_traversal_name_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root / "installed"
            source = root / "source" / "unsafe"
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text("content", encoding="utf-8")
            record = SkillRecord(
                name="../escape",
                description="A long enough description for traversal testing.",
                category="testing",
                path=source,
            )
            with self.assertRaisesRegex(InstallError, "unsafe skill destination"):
                install_skill(record, destination, dry_run=True)


if __name__ == "__main__":
    unittest.main()

