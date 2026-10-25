from __future__ import annotations

import json
import hashlib
from pathlib import Path
import shutil

from .catalog import SkillRecord


STATE_FILE = ".vibe-skills-state.json"


class InstallError(RuntimeError):
    """Raised for unsafe or conflicting installation operations."""


def _safe_child(root: Path, child_name: str) -> Path:
    root = root.resolve()
    candidate = (root / child_name).resolve()
    if candidate.parent != root:
        raise InstallError(f"unsafe skill destination: {candidate}")
    return candidate


def _state_path(destination: Path) -> Path:
    return destination.resolve().parent / STATE_FILE


def _read_state(destination: Path) -> dict[str, dict[str, str]]:
    state_path = _state_path(destination)
    if not state_path.exists():
        return {}
    try:
        payload = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallError(f"cannot read installer state: {state_path}") from exc
    if not isinstance(payload, dict):
        raise InstallError(f"invalid installer state: {state_path}")
    return payload


def _write_state(destination: Path, state: dict[str, dict[str, str]]) -> None:
    state_path = _state_path(destination)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    temp = state_path.with_suffix(state_path.suffix + ".tmp")
    temp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp.replace(state_path)


def _tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        data = path.read_bytes()
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def install_skill(
    record: SkillRecord,
    destination: Path,
    *,
    dry_run: bool = False,
) -> Path:
    destination = destination.resolve()
    target = _safe_child(destination, record.name)
    if target.exists():
        raise InstallError(
            f"skill '{record.name}' already exists at {target}; remove it explicitly before reinstalling"
        )
    if dry_run:
        return target

    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(record.path, target)
    installed_digest = _tree_digest(target)
    state = _read_state(destination)
    state[record.name] = {
        "source": str(record.path.resolve()),
        "target": str(target),
        "installed_digest": installed_digest,
    }
    _write_state(destination, state)
    return target


def update_skill(
    record: SkillRecord,
    destination: Path,
    *,
    dry_run: bool = False,
) -> Path:
    destination = destination.resolve()
    target = _safe_child(destination, record.name)
    state = _read_state(destination)
    entry = state.get(record.name)
    if entry is None or Path(entry.get("target", "")).resolve() != target:
        raise InstallError(
            f"refusing to update unmanaged skill '{record.name}'; install it with vibe-skills first"
        )
    if not target.exists():
        raise InstallError(f"managed skill '{record.name}' is missing from {target}")

    installed_digest = entry.get("installed_digest")
    current_digest = _tree_digest(target)
    if not installed_digest or current_digest != installed_digest:
        raise InstallError(
            f"refusing to overwrite locally modified skill '{record.name}' at {target}"
        )
    if dry_run:
        return target

    staging = _safe_child(destination, f".{record.name}.update")
    if staging.exists():
        raise InstallError(f"stale update staging path exists: {staging}")
    shutil.copytree(record.path, staging)
    new_digest = _tree_digest(staging)
    backup = _safe_child(destination, f".{record.name}.backup")
    if backup.exists():
        raise InstallError(f"stale update backup path exists: {backup}")
    try:
        target.replace(backup)
        staging.replace(target)
        shutil.rmtree(backup)
    except Exception:
        if not target.exists() and backup.exists():
            backup.replace(target)
        if staging.exists():
            shutil.rmtree(staging)
        raise

    state[record.name] = {
        "source": str(record.path.resolve()),
        "target": str(target),
        "installed_digest": new_digest,
    }
    _write_state(destination, state)
    return target


def remove_skill(name: str, destination: Path, *, dry_run: bool = False) -> Path:
    destination = destination.resolve()
    target = _safe_child(destination, name)
    state = _read_state(destination)
    entry = state.get(name)
    if entry is None or Path(entry.get("target", "")).resolve() != target:
        raise InstallError(
            f"refusing to remove unmanaged skill '{name}'; only installer-managed skills can be removed"
        )
    if not target.exists():
        raise InstallError(f"managed skill '{name}' is missing from {target}")
    if dry_run:
        return target

    shutil.rmtree(target)
    del state[name]
    _write_state(destination, state)
    return target

