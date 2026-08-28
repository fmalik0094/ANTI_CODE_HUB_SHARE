import json
import re
import sys
from datetime import date
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
    ".agents/ORIENTATION.md",
    ".agents/resources/MODEL_REFERENCE.md",
    ".gitignore",
]

REQUIRED_REFERENCE_SOURCE_URLS = (
    "https://platform.claude.com/docs/en/about-claude/models/overview",
    "https://code.claude.com/docs/en/overview",
    "https://developers.openai.com/api/docs/models",
    "https://developers.openai.com/learn/codex",
    "https://learn.chatgpt.com/docs",
    "https://ai.google.dev/gemini-api/docs/models",
    "https://antigravity.google/docs/home",
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
    """The registry holds 3 permanent leads (bold IDs) plus 3 parametric slots
    (backticked IDs, specialization defined per project). main.md must agree on
    the permanent count and mention every ID."""
    errors = []
    registry_path = ROOT / ".agents" / "AGENT_REGISTRY.md"
    main_path = ROOT / "main.md"
    if not registry_path.exists() or not main_path.exists():
        return errors  # already reported by check_required_paths

    registry_text = registry_path.read_text(encoding="utf-8")
    permanent_ids = re.findall(r"\|\s*\*\*((?:GEM|CDX|CLD)-\d+)\*\*", registry_text)
    slot_ids = re.findall(r"\|\s*`((?:GEM|CDX|CLD)-\d+)`", registry_text)

    if len(permanent_ids) != 3:
        errors.append(
            f"AGENT_REGISTRY.md should list exactly 3 permanent leads (one per "
            f"engine, bold IDs); found {len(permanent_ids)}: "
            f"{', '.join(permanent_ids) or 'none'}"
        )

    if len(slot_ids) != 3:
        errors.append(
            f"AGENT_REGISTRY.md should list exactly 3 parametric slots (one per "
            f"engine, backticked IDs); found {len(slot_ids)}: "
            f"{', '.join(slot_ids) or 'none'}"
        )

    engines_seen = {pid.split("-")[0] for pid in permanent_ids}
    for engine in ("GEM", "CDX", "CLD"):
        if engine not in engines_seen:
            errors.append(
                f"AGENT_REGISTRY.md has no permanent lead for engine '{engine}'"
            )

    main_text = main_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+)\s+permanent agents\*\*", main_text)
    if not m:
        errors.append(
            "main.md does not state '**N permanent agents**' — cannot verify "
            "it agrees with .agents/AGENT_REGISTRY.md"
        )
        return errors

    stated_count = int(m.group(1))
    if stated_count != len(permanent_ids):
        errors.append(
            f"Agent count mismatch: AGENT_REGISTRY.md lists "
            f"{len(permanent_ids)} permanent leads "
            f"({', '.join(permanent_ids)}) but main.md states "
            f"'{stated_count} permanent agents'"
        )

    for agent_id in permanent_ids + slot_ids:
        if agent_id not in main_text:
            errors.append(f"main.md never mentions agent '{agent_id}'")
    return errors


BOOT_FILES = (
    "CLAUDE.md",
    "antigravity/.gemini/GEMINI.md",
    "vscode/.codex/instructions.md",
)


def check_boot_files_dont_pin_slots():
    """Slot 02 is parametric — each project defines its specialization. A boot
    file that names a slot must say so, not assign it a fixed role.

    This check exists because a migration to the 3+3 model updated the registry
    and main.md but left all three boot files still pinning CLD-02 as "QA
    Validator", GEM-02 as "multimodal ingestion", and CDX-02 as "file ops/git".
    The registry said parametric while every entry point said otherwise.
    """
    errors = []
    for rel_path in BOOT_FILES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Boot file missing: {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        mentions_slot = re.search(r"(?:GEM|CDX|CLD)-02", text)
        if mentions_slot and "parametric" not in text.lower():
            errors.append(
                f"{rel_path} names a parametric slot (GEM/CDX/CLD-02) without "
                f"describing it as parametric; it likely pins a fixed "
                f"specialization that the project registry is supposed to define"
            )
        if "ORIENTATION.md" not in text:
            errors.append(
                f"{rel_path} does not point at .agents/ORIENTATION.md; every "
                f"engine entry point must route to the single entry point"
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


def get_model_reference_staleness_warnings(content, today=None):
    """Report old vendor snapshots without blocking unrelated repository work."""
    today = today or date.today()
    warnings = []
    vendor_dates = re.findall(
        r"^## (Anthropic|OpenAI|Google)[^\n]*\n\n"
        r"Last verified:\s*(\d{4}-\d{2}-\d{2})",
        content,
        flags=re.MULTILINE,
    )
    for vendor, raw_date in vendor_dates:
        try:
            verified_on = date.fromisoformat(raw_date)
        except ValueError:
            continue
        age_days = (today - verified_on).days
        if age_days > 60:
            warnings.append(
                f"MODEL_REFERENCE.md {vendor} snapshot is {age_days} days "
                f"old (last verified {raw_date}); refresh before relying on "
                "exact values"
            )
    return warnings


def check_model_reference_contract():
    """Keep the compact local snapshot anchored to all three live catalogs."""
    errors = []
    reference_path = ROOT / ".agents" / "resources" / "MODEL_REFERENCE.md"
    if not reference_path.exists():
        return errors, []  # already reported by check_required_paths

    content = reference_path.read_text(encoding="utf-8")
    for source_url in REQUIRED_REFERENCE_SOURCE_URLS:
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
    return errors, get_model_reference_staleness_warnings(content)


def main():
    all_errors = []
    all_warnings = []
    all_errors += check_required_paths()

    settings_errors, settings_data = check_settings_json_valid()
    all_errors += settings_errors
    all_errors += check_permission_paths_real(settings_data)

    all_errors += check_agent_count_agreement()
    all_errors += check_boot_files_dont_pin_slots()
    all_errors += check_checkpoint_consistency()
    model_errors, model_warnings = check_model_reference_contract()
    all_errors += model_errors
    all_warnings += model_warnings

    for warning in all_warnings:
        print(f"[WARN] {warning}")

    if all_errors:
        print(f"[FAIL] {len(all_errors)} issue(s) found in ANTI_CODE_HUB_SPEC_VAULT:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("[SUCCESS] All structural and semantic checks passed for ANTI_CODE_HUB_SPEC_VAULT.")
    sys.exit(0)


if __name__ == "__main__":
    main()
