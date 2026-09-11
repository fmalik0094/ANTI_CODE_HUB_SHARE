"""Read-only CLI loader probe; NOT proof of desktop startup or sandbox enforcement.

Reads the project's config, passes its values through temporary CLI overrides,
and verifies retirement of the old approval value. Never edits user config.
Project-file inclusion by the ordinary loader remains unproven by features list.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    tomllib = None

ROOT = Path(__file__).resolve().parent.parent


def overrides(config, prefix=""):
    for key, value in config.items():
        # Codex -c dotted paths are not TOML quoted-key syntax. Quoting a key
        # can create an ignored literal key and produce a false-positive probe.
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            raise ValueError(f"Unsupported CLI key {key!r}; review the seed contract")
        dotted = prefix + key
        if isinstance(value, dict):
            yield from overrides(value, dotted + ".")
        elif isinstance(value, (str, bool, int, float)):
            yield dotted + "=" + json.dumps(value)
        else:
            raise ValueError(f"Unsupported probe value at {dotted}; review the seed contract")


def run(executable, args):
    return subprocess.run(
        [executable] + args, cwd=ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=30, check=False,
    )


def report(label, result, expected=0, required_error=None):
    output = result.stdout + result.stderr
    ok = result.returncode == expected and (
        required_error is None or required_error in output
    )
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: exit {result.returncode}")
    if result.returncode or not ok:
        print(output.strip())
    return ok


def main():
    executable = shutil.which("codex")
    if executable is None or tomllib is None:
        print("[FAIL] Probe requires the installed codex executable and Python 3.11+.")
        return 1
    try:
        with (ROOT / ".codex/config.toml").open("rb") as source:
            config = tomllib.load(source)
        version = run(executable, ["--version"])
        print(f"Executable: {executable}")
        print(version.stdout.strip())
        print(f"Source: {ROOT / '.codex/config.toml'}")
        ok = report("runtime version", version)
        ordinary = run(executable, ["features", "list"])
        ok = report("ordinary CLI loader (project-file inclusion unproven)", ordinary) and ok
        args = []
        for value in overrides(config):
            args.extend(["-c", value])
        explicit = run(executable, args + ["features", "list"])
        ok = report("actual seed values through explicit CLI override layer", explicit) and ok
        # Prove the serialized seed key is consumed, rather than silently ignored.
        invalid_args = []
        for value in overrides({**config, "sandbox_mode": "anti-code-invalid-sandbox"}):
            invalid_args.extend(["-c", value])
        invalid = run(executable, invalid_args + ["features", "list"])
        ok = report(
            "serialized sandbox key negative control", invalid, expected=1,
            required_error="anti-code-invalid-sandbox",
        ) and ok
        invalid_network = {**config, "sandbox_workspace_write": {"network_access": "anti-code-invalid-network"}}
        invalid_args = []
        for value in overrides(invalid_network):
            invalid_args.extend(["-c", value])
        invalid = run(executable, invalid_args + ["features", "list"])
        ok = report(
            "serialized network key negative control", invalid, expected=1,
            required_error="anti-code-invalid-network",
        ) and ok
        retired = run(executable, args + ["-c", 'approval_policy="untrusted"', "features", "list"])
        ok = report(
            "retired-value negative control", retired, expected=1,
            required_error='approval_policy = "untrusted" is no longer supported',
        ) and ok
        print("Layers: ambient user/managed defaults plus temporary CLI overrides; no settings edited.")
        print("Not proved: project-layer inclusion, effective command approvals, sandbox enforcement, desktop startup.")
        return 0 if ok else 1
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"[FAIL] Runtime probe could not complete: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
