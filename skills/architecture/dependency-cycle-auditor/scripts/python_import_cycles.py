from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


def module_name(root: Path, path: Path) -> str:
    relative = path.relative_to(root).with_suffix("")
    parts = list(relative.parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def graph(root: Path) -> dict[str, set[str]]:
    modules: dict[str, Path] = {}
    for path in root.rglob("*.py"):
        if any(part in {".git", ".venv", "__pycache__", "build", "dist"} for part in path.parts):
            continue
        name = module_name(root, path)
        if name:
            modules[name] = path

    edges = {name: set() for name in modules}
    for name, path in modules.items():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, UnicodeDecodeError, SyntaxError):
            continue
        package = name.split(".")[:-1]
        for node in ast.walk(tree):
            candidates: list[str] = []
            if isinstance(node, ast.Import):
                candidates.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    base = package[: max(0, len(package) - node.level + 1)]
                    if node.module:
                        base += node.module.split(".")
                    candidates.append(".".join(base))
                elif node.module:
                    candidates.append(node.module)
            for imported in candidates:
                for target in modules:
                    if imported == target or imported.startswith(target + "."):
                        edges[name].add(target)
    return edges


def cycles(edges: dict[str, set[str]]) -> list[list[str]]:
    result: set[tuple[str, ...]] = set()

    def visit(start: str, node: str, path: list[str]) -> None:
        for nxt in edges.get(node, set()):
            if nxt == start:
                cycle = path + [start]
                body = cycle[:-1]
                rotations = [tuple(body[i:] + body[:i]) for i in range(len(body))]
                result.add(min(rotations))
            elif nxt not in path and len(path) <= len(edges):
                visit(start, nxt, path + [nxt])

    for start in edges:
        visit(start, start, [start])
    return [list(item) for item in sorted(result)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    found = cycles(graph(Path(args.root).resolve()))
    print(json.dumps(found, indent=2))
    return 1 if found else 0


if __name__ == "__main__":
    raise SystemExit(main())
