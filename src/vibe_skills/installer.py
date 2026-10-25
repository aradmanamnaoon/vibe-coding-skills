from __future__ import annotations

import json
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
    state = _read_state(destination)
    state[record.name] = {
        "source": str(record.path.resolve()),
        "target": str(target),
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

