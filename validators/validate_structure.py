import os
import sys
from pathlib import Path

REQUIRED_PATHS = [
    ".geminiignore",
    ".vscode/settings.json",
    ".aiexclude",
    "AGENTS.md",
    ".agents/rules/global.md",
    ".agents/workflows/01_genesis_prompt.md",
    ".agents/workflows/02_entry_and_propose.md",
    ".agents/workflows/03_exit_and_sync.md",
    ".state/BASELINE.md",
    ".state/DECISIONS.md",
    ".state/DELTA_LOG.md",
    ".agents/states/_ACTIVE_INDEX.md"
]

def main():
    root = Path(__file__).resolve().parent.parent
    missing = []
    for path in REQUIRED_PATHS:
        if not (root / path).exists():
            missing.append(path)

    if missing:
        print(f"[FAIL] Missing required Anti-Code Hub paths in 'ANTI_CODE_HUB_SPEC_VAULT': {missing}")
        sys.exit(1)
    else:
        print(f"[SUCCESS] All required Anti-Code Hub topology paths are present in 'ANTI_CODE_HUB_SPEC_VAULT'.")
        sys.exit(0)

if __name__ == "__main__":
    main()
