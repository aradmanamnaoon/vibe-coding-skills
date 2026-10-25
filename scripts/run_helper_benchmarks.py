from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def load_module(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(name: str, callback) -> dict[str, object]:
    start = time.perf_counter()
    try:
        detail = callback()
    except Exception as exc:
        return {
            "name": name,
            "passed": False,
            "detail": f"{type(exc).__name__}: {exc}",
            "elapsed_ms": round((time.perf_counter() - start) * 1000, 3),
        }
    return {
        "name": name,
        "passed": True,
        "detail": detail,
        "elapsed_ms": round((time.perf_counter() - start) * 1000, 3),
    }


def secret_case() -> str:
    module = load_module(
        "benchmark_scan_secrets",
        "skills/security/secret-leakage-detector/scripts/scan_secrets.py",
    )
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        secret = "sk-" + "A" * 30
        (root / "config.py").write_text(f'API_KEY = "{secret}"\n', encoding="utf-8")
        findings = module.scan(root)
        if not findings:
            raise AssertionError("credential-shaped fixture was not detected")
        if secret in repr(findings):
            raise AssertionError("finding exposed the secret value")
        return f"detected {len(findings)} redacted finding(s)"


def skipped_test_case() -> str:
    module = load_module(
        "benchmark_find_skipped_tests",
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
        expected = {"unittest-skip", "jest-skip"}
        if not expected.issubset(kinds):
            raise AssertionError(f"missing expected kinds: {expected - kinds}")
        return "detected Python and JavaScript skipped-test signals"


def placeholder_case() -> str:
    module = load_module(
        "benchmark_scan_placeholders",
        "skills/frontend/dead-feature-detector/scripts/scan_placeholders.py",
    )
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "App.tsx").write_text(
            "<button onClick={() => {}}>Run</button>\n// TODO implement\n",
            encoding="utf-8",
        )
        kinds = {finding["kind"] for finding in module.scan(root)}
        expected = {"empty-js-handler", "todo-fixme"}
        if not expected.issubset(kinds):
            raise AssertionError(f"missing expected kinds: {expected - kinds}")
        return "detected empty handler and implementation-marker signals"


def env_case() -> str:
    module = load_module(
        "benchmark_discover_env_keys",
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
        if discovered.get("DATABASE_URL") != ["settings.py"]:
            raise AssertionError("Python environment key mapping was incorrect")
        if discovered.get("PUBLIC_API_KEY") != ["web.ts"]:
            raise AssertionError("JavaScript environment key mapping was incorrect")
        return "mapped two environment keys to their source files"


def cycle_case() -> str:
    module = load_module(
        "benchmark_python_import_cycles",
        "skills/architecture/dependency-cycle-auditor/scripts/python_import_cycles.py",
    )
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "a.py").write_text("import b\n", encoding="utf-8")
        (root / "b.py").write_text("import a\n", encoding="utf-8")
        found = module.cycles(module.graph(root))
        if not any(set(cycle) == {"a", "b"} for cycle in found):
            raise AssertionError("two-module cycle was not detected")
        return "detected the seeded two-module import cycle"


def write_report(results: list[dict[str, object]]) -> None:
    passed = sum(bool(result["passed"]) for result in results)
    lines = [
        "# Benchmark results",
        "",
        "Observed locally on 2026-10-25 using Python 3.10.10 on the active Windows host.",
        "",
        f"Deterministic helper fixtures passed: **{passed}/{len(results)}**.",
        "",
        "| Fixture | Result | Evidence | Local elapsed time |",
        "|---|:---:|---|---:|",
    ]
    for result in results:
        status = "pass" if result["passed"] else "fail"
        lines.append(
            f"| {result['name']} | {status} | {result['detail']} | {result['elapsed_ms']} ms |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "These measurements establish that the bundled deterministic helpers recognize their seeded fixture conditions and that the secret scanner does not echo its seeded credential value. The elapsed times are informational local observations, not cross-machine performance claims.",
            "",
            "No agent-versus-agent or agent-with-skill versus agent-without-skill success-rate claim is reported. Agent-level benchmark status is **not executed** for this release.",
        ]
    )
    (DOCS / "benchmark-results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    cases = [
        ("secret leakage helper", secret_case),
        ("skipped-test helper", skipped_test_case),
        ("dead-feature helper", placeholder_case),
        ("environment-config helper", env_case),
        ("dependency-cycle helper", cycle_case),
    ]
    results = [run_case(name, callback) for name, callback in cases]
    write_report(results)
    failures = [result for result in results if not result["passed"]]
    for result in results:
        print(
            f"{'PASS' if result['passed'] else 'FAIL'} {result['name']}: "
            f"{result['detail']} ({result['elapsed_ms']} ms)"
        )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
