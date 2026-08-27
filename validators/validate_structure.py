import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    ".geminiignore",
    ".vscode/settings.json",
    ".claude/settings.json",
    "CLAUDE.md",
    ".aiexclude",
    "AGENTS.md",
    ".agents/rules/global.md",
    ".agents/workflows/01_genesis_prompt.md",
    ".agents/workflows/02_entry_and_propose.md",
    ".agents/workflows/03_exit_and_sync.md",
    ".state/BASELINE.md",
    ".state/DECISIONS.md",
    ".state/DELTA_LOG.md",
    ".state/EXECUTION_LOG.md",
    ".agents/states/_ACTIVE_INDEX.md",
    ".agents/AGENT_REGISTRY.md",
    ".agents/resources/MODEL_REFERENCE.md",
    ".gitignore",
]

REQUIRED_MODEL_SOURCE_URLS = (
    "https://platform.claude.com/docs/en/about-claude/models/overview",
    "https://developers.openai.com/api/docs/models",
    "https://ai.google.dev/gemini-api/docs/models",
)

# Path fragments that are expected to be absent locally or outside this repo's
# tree — real by convention/intent, not a structural gap.
PERMISSION_PATH_EXEMPTIONS = ("C:/", "../", "config/private", "credentials")


def check_required_paths():
    errors = []
    for path in REQUIRED_PATHS:
        if not (ROOT / path).exists():
            errors.append(f"Missing required path: {path}")
    return errors


def check_settings_json_valid():
    errors = []
    settings_path = ROOT / ".claude" / "settings.json"
    try:
        with open(settings_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f".claude/settings.json is not valid JSON: {e}")
        return errors, None
    return errors, data


def check_permission_paths_real(settings_data):
    """Every 'allow' glob should resolve to something that actually exists —
    a grant for a path that isn't real is dead weight at best and a copy-paste
    artifact at worst. 'deny' is exempt: secret-pattern denials (.env, *.key)
    are intentionally defensive and should hold even before such a file ever
    gets created."""
    errors = []
    if not settings_data:
        return errors
    perms = settings_data.get("permissions", {})
    pattern = re.compile(r"^(?:Read|Write)\((.+)\)$")
    for bucket in ("allow",):
        for entry in perms.get(bucket, []):
            m = pattern.match(entry)
            if not m:
                continue
            raw_path = m.group(1)
            if any(ex in raw_path for ex in PERMISSION_PATH_EXEMPTIONS):
                continue
            if raw_path.startswith("**"):
                # global glob like **/*.key — nothing specific to check
                continue
            base = raw_path.split("*")[0].rstrip("/")
            if not base:
                continue
            if not (ROOT / base).exists():
                errors.append(
                    f".claude/settings.json [{bucket}] grants a path that "
                    f"doesn't exist: '{entry}' (base '{base}' not found)"
                )
    return errors


def check_agent_count_agreement():
    errors = []
    registry_path = ROOT / ".agents" / "AGENT_REGISTRY.md"
    main_path = ROOT / "main.md"
    if not registry_path.exists() or not main_path.exists():
        return errors  # already reported by check_required_paths

    registry_text = registry_path.read_text(encoding="utf-8")
    row_ids = re.findall(r"\|\s*\*\*((?:GEM|CDX|CLD)-\d+)\*\*", registry_text)
    registry_count = len(row_ids)

    main_text = main_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+)\s+registered agents\*\*", main_text)
    if not m:
        errors.append(
            "main.md does not state '**N registered agents**' — cannot "
            "verify it agrees with .agents/AGENT_REGISTRY.md"
        )
        return errors

    stated_count = int(m.group(1))
    if stated_count != registry_count:
        errors.append(
            f"Agent count mismatch: AGENT_REGISTRY.md has {registry_count} "
            f"rows ({', '.join(row_ids)}) but main.md states "
            f"'{stated_count} registered agents'"
        )

    for engine_id in row_ids:
        if engine_id not in main_text:
            errors.append(
                f"main.md never mentions registered agent '{engine_id}'"
            )
    return errors


def check_checkpoint_consistency():
    """The version _ACTIVE_INDEX.md claims for a domain should match the
    version the domain's own state file declares."""
    errors = []
    index_path = ROOT / ".agents" / "states" / "_ACTIVE_INDEX.md"
    if not index_path.exists():
        return errors
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|") or "DOMAIN" in line or ":---" in line:
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        domain, version, statefile = cols[0], cols[1], cols[2]
        state_path = ROOT / ".agents" / "states" / statefile
        if not state_path.exists():
            errors.append(
                f"_ACTIVE_INDEX.md references '{statefile}' for {domain}, "
                f"which doesn't exist"
            )
            continue
        content = state_path.read_text(encoding="utf-8")
        if version and version not in content:
            errors.append(
                f"_ACTIVE_INDEX.md says {domain} is at {version}, but "
                f"{statefile} doesn't declare that version anywhere in its text"
            )
    return errors


def check_model_reference_contract():
    """Keep the compact local snapshot anchored to all three live catalogs."""
    errors = []
    reference_path = ROOT / ".agents" / "resources" / "MODEL_REFERENCE.md"
    if not reference_path.exists():
        return errors  # already reported by check_required_paths

    content = reference_path.read_text(encoding="utf-8")
    for source_url in REQUIRED_MODEL_SOURCE_URLS:
        if source_url not in content:
            errors.append(
                "MODEL_REFERENCE.md is missing authoritative source URL: "
                f"{source_url}"
            )

    verification_dates = re.findall(
        r"Last verified:\s*\d{4}-\d{2}-\d{2}", content
    )
    if len(verification_dates) != 3:
        errors.append(
            "MODEL_REFERENCE.md must contain exactly three vendor-section "
            "'Last verified: YYYY-MM-DD' markers"
        )
    return errors


def main():
    all_errors = []
    all_errors += check_required_paths()

    settings_errors, settings_data = check_settings_json_valid()
    all_errors += settings_errors
    all_errors += check_permission_paths_real(settings_data)

    all_errors += check_agent_count_agreement()
    all_errors += check_checkpoint_consistency()
    all_errors += check_model_reference_contract()

    if all_errors:
        print(f"[FAIL] {len(all_errors)} issue(s) found in ANTI_CODE_HUB_SPEC_VAULT:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("[SUCCESS] All structural and semantic checks passed for ANTI_CODE_HUB_SPEC_VAULT.")
    sys.exit(0)


if __name__ == "__main__":
    main()
