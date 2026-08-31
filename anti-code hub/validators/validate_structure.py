"""Structural and semantic validation for a project seeded from ANTI_CODE-HUB.

Project-neutral by design: it validates the governance contract every seeded
project inherits, not any one project's content. Add project-specific checks
below the marked section rather than editing the inherited ones.
"""

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    ".agents/ORIENTATION.md",
    ".agents/AGENT_REGISTRY.md",
    ".agents/rules/global.md",
    ".agents/workflows/01_genesis_prompt.md",
    ".agents/workflows/02_entry_and_propose.md",
    ".agents/workflows/03_exit_and_sync.md",
    ".state/BASELINE.md",
    ".state/DECISIONS.md",
    ".state/DELTA_LOG.md",
    ".state/EXECUTION_LOG.md",
    ".claude/settings.json",
    ".codex/config.toml",
    ".codex/instructions.md",
    ".gemini/GEMINI.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".aiexclude",
    ".geminiignore",
    ".gitignore",
]

BOOT_FILES = ("CLAUDE.md", ".gemini/GEMINI.md", ".codex/instructions.md")

# Denials that are defensive by intent — they must hold whether or not the file
# exists yet, so their paths are never checked for existence.
PERMISSION_PATH_EXEMPTIONS = ("C:/", "../", "config/private", "credentials")

# Verified against https://developers.openai.com/codex/config-reference on
# 2026-08-31. Keep this deliberately narrow: the seed config needs only these
# documented keys, so an unfamiliar key fails instead of becoming decorative
# policy that Codex silently ignores.
CODEX_CONFIG_TOP_LEVEL_KEYS = {
    "approval_policy",
    "sandbox_mode",
    "sandbox_workspace_write",
}
CODEX_WORKSPACE_WRITE_KEYS = {"network_access"}


def check_required_paths():
    return [
        f"Missing required path: {p}"
        for p in REQUIRED_PATHS
        if not (ROOT / p).exists()
    ]


def load_claude_settings():
    path = ROOT / ".claude" / "settings.json"
    try:
        return [], json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [f".claude/settings.json is not valid JSON: {e}"], None


def load_codex_config():
    path = ROOT / ".codex" / "config.toml"
    try:
        with path.open("rb") as config_file:
            return [], tomllib.load(config_file)
    except (OSError, tomllib.TOMLDecodeError) as e:
        return [f".codex/config.toml is not valid TOML: {e}"], None


def check_codex_config(config):
    """Accept only the documented keys and the seed's review-first posture."""
    errors = []
    if config is None:
        return errors

    unknown_top_level = sorted(set(config) - CODEX_CONFIG_TOP_LEVEL_KEYS)
    if unknown_top_level:
        errors.append(
            ".codex/config.toml contains unsupported top-level key(s): "
            + ", ".join(unknown_top_level)
        )

    if config.get("approval_policy") != "untrusted":
        errors.append(
            ".codex/config.toml must set approval_policy = 'untrusted' so "
            "untrusted commands require operator review"
        )

    if config.get("sandbox_mode") != "workspace-write":
        errors.append(
            ".codex/config.toml must set sandbox_mode = 'workspace-write'"
        )

    workspace_write = config.get("sandbox_workspace_write")
    if not isinstance(workspace_write, dict):
        errors.append(
            ".codex/config.toml must define [sandbox_workspace_write]"
        )
        return errors

    unknown_workspace_write = sorted(
        set(workspace_write) - CODEX_WORKSPACE_WRITE_KEYS
    )
    if unknown_workspace_write:
        errors.append(
            ".codex/config.toml contains unsupported "
            "sandbox_workspace_write key(s): "
            + ", ".join(unknown_workspace_write)
        )

    if workspace_write.get("network_access") is not False:
        errors.append(
            ".codex/config.toml must set "
            "sandbox_workspace_write.network_access = false"
        )

    return errors


def check_permission_paths_real(settings):
    """An 'allow' grant for a path that doesn't exist is dead weight at best and
    a copy-paste artifact at worst. 'deny' is exempt — see the note above."""
    errors = []
    if not settings:
        return errors
    pattern = re.compile(r"^(?:Read|Write)\((.+)\)$")
    for entry in settings.get("permissions", {}).get("allow", []):
        m = pattern.match(entry)
        if not m:
            continue
        raw = m.group(1)
        if raw.startswith("**") or any(x in raw for x in PERMISSION_PATH_EXEMPTIONS):
            continue
        base = raw.split("*")[0].rstrip("/")
        if base and not (ROOT / base).exists():
            errors.append(
                f".claude/settings.json grants a path that doesn't exist: "
                f"'{entry}' (base '{base}' not found)"
            )
    return errors


def check_destructive_commands_gated(settings):
    """git commit/push and rm must require approval — validation passing is not
    authorization to commit, and committing is not authorization to push."""
    errors = []
    if not settings:
        return errors
    ask = " ".join(settings.get("permissions", {}).get("ask", []))
    for required in ("git commit", "git push", "rm"):
        if required not in ask:
            errors.append(
                f".claude/settings.json does not gate '{required}' behind ask; "
                f"approval gates in ORIENTATION.md assume it does"
            )
    return errors


def check_agent_registry():
    """3 permanent leads (bold IDs), 3 parametric slots (backticked IDs), one
    permanent lead per engine."""
    errors = []
    path = ROOT / ".agents" / "AGENT_REGISTRY.md"
    if not path.exists():
        return errors
    text = path.read_text(encoding="utf-8")
    permanent = re.findall(r"\|\s*\*\*((?:GEM|CDX|CLD)-\d+)\*\*", text)
    slots = re.findall(r"\|\s*`((?:GEM|CDX|CLD)-\d+)`", text)

    if len(permanent) != 3:
        errors.append(
            f"AGENT_REGISTRY.md should list 3 permanent leads (bold IDs); "
            f"found {len(permanent)}: {', '.join(permanent) or 'none'}"
        )
    if len(slots) != 3:
        errors.append(
            f"AGENT_REGISTRY.md should list 3 parametric slots (backticked "
            f"IDs); found {len(slots)}: {', '.join(slots) or 'none'}"
        )
    seen = {p.split("-")[0] for p in permanent}
    for engine in ("GEM", "CDX", "CLD"):
        if engine not in seen:
            errors.append(f"No permanent lead registered for engine '{engine}'")
    return errors


def check_boot_files():
    """Every engine entry point must route to ORIENTATION.md, and none may pin a
    parametric slot's specialization — that belongs to this project's registry."""
    errors = []
    for rel in BOOT_FILES:
        path = ROOT / rel
        if not path.exists():
            continue  # already reported by check_required_paths
        text = path.read_text(encoding="utf-8")
        if "ORIENTATION.md" not in text:
            errors.append(
                f"{rel} does not point at .agents/ORIENTATION.md; every engine "
                f"entry point must route to the single entry point"
            )
        if re.search(r"(?:GEM|CDX|CLD)-02", text) and "parametric" not in text.lower():
            errors.append(
                f"{rel} names a parametric slot without describing it as "
                f"parametric; it likely pins a specialization the project "
                f"registry is supposed to define"
            )
    return errors


def check_placeholders_replaced():
    """Warn (not fail) while genesis placeholders are still present."""
    warnings = []
    for rel in ("CLAUDE.md", ".agents/ORIENTATION.md", ".state/BASELINE.md"):
        path = ROOT / rel
        if path.exists() and "[PROJECT" in path.read_text(encoding="utf-8"):
            warnings.append(
                f"{rel} still contains a [PROJECT...] placeholder; run "
                f".agents/workflows/01_genesis_prompt.md"
            )
    return warnings


# --- Add project-specific checks below this line ---------------------------


def main():
    errors = []
    errors += check_required_paths()

    config_errors, codex_config = load_codex_config()
    errors += config_errors
    errors += check_codex_config(codex_config)

    settings_errors, settings = load_claude_settings()
    errors += settings_errors
    errors += check_permission_paths_real(settings)
    errors += check_destructive_commands_gated(settings)

    errors += check_agent_registry()
    errors += check_boot_files()

    for warning in check_placeholders_replaced():
        print(f"[WARN] {warning}")

    if errors:
        print(f"[FAIL] {len(errors)} issue(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("[SUCCESS] All structural and semantic checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
