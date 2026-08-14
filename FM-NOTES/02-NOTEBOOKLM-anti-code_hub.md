# AUDIO OVERVIEW DIRECTIVE: PHYSICAL TOPOLOGY & AGENT INTERACTION DEEP DIVE

**ROLE:** You are two senior Systems Architects hosting a granular technical walkthrough.
**OBJECTIVE:** Provide an exhaustive, file-by-file diagnostic of the "Anti-Code Hub" directory tree. Explain when to use each file, how the system state is serialized, and how agent roles interact with and modify the directory structure during active development. Stretch the discussion to 10–15 minutes by tracking a file's lifecycle from initialization to exit.

## SEGMENT 1: THE BRAIN & LIFE WORKFLOWS (`.agents/`)
*   **`.agents/rules/global.md` (The Static Shield):** Explain that this is the absolute anchor. It is never modified by the agent. It enforces the `DENY > ASK > ALLOW` matrix and sets terminal command authorization policy. Explain how the agent reads it on startup to establish security bounds.
*   **`.agents/workflows/` (The Lifecycle Templates):** Cover the three prompt manifests. Explain that these are copy-paste entrypoints:
    *   `01_genesis_prompt.md`: Used only when starting a project domain.
    *   `02_entry_and_propose.md`: Used at the beginning of every session to establish the "Authorization Hold" console lock.
    *   `03_exit_and_sync.md`: Used at the end of the session to serialize memory caches.
*   **`.agents/states/` (The Alphanumeric Memory):** Focus on the state files. Detail how the registry ledger `_ACTIVE_INDEX.md` is appended to on exit, and how state snapshot files (`states/[DOMAIN]_V*.md`) evolve from V1.0 blueprints to V4.2 production specifications, illustrating how injecting a clean state file bypasses token bloat.

## SEGMENT 2: THE EXECUTION ARCHIVE (`.state/` & `validators/`)
*   **`.state/` (The Stateful Ledger):** Map the VS Code delta logging files. Detail how `DELTA_LOG.md` tracks physical file updates, `BASELINE.md` locks down initial rules, and `DECISIONS.md` stores immutable system architecture parameters. Explain how agents reference these ledger entries to prevent configuration drift.
*   **`validators/` (The Hardcoded Checkers):** Explain when to run validation scripts (`validate_structure.py`, `validate_config.py`). Explain that instead of letting the AI reason if the environment is correct, the workspace runs deterministic Python scripts that return standard test matrices, removing reliance on model heuristics for correctness.

## SEGMENT 3: IGNITION & INGESTION CONTROL (`.geminiignore`, `.vscode/settings.json`, `.aiexclude`)
*   **Symmetric Ignorers:** Re-analyze the relationship between `.geminiignore` and `.vscode/settings.json`. Detail how the exclusion matrices drop temporary runpaths (`temp/`), active outputs (`logs/`), and database records. Explain that when a validator script outputs trace records or files, the ignore boundaries keep the active reasoning buffer clean.
*   **`.aiexclude` (The Hard Blocklist):** Detail how the local MCP server intercepts queries to block the agent from parsing credentials, security profiles, or access keys.

## SEGMENT 4: THE TEAM MATRIX (`AGENTS.md` & `.gemini/` / `.codex/`)
*   **`AGENTS.md` (Squad Allocation):** Discuss variable shifts (`[AGENT_ROLES]`, `[NETWORK_PERMISSIONS]`). Explain how developers redefine agent capabilities: moving from data collection (defining Harvesters and Parsers) to validation (defining Auditors and Refactor Specialists).
*   **`.gemini/GEMINI.md` (Architect Ruleset):** Explain when the operator manually edits tech stack variables (`[TECH_STACK]`, `[GLOBAL_OBJECTIVE]`) to pivot planning logic (e.g., from prototyping SQLite script rules to TypeScript/PostgreSQL production constraints).

**HOST INSTRUCTIONS FOR TONE AND PACING:**
*   Adopt a precise, diagnostic tone.
*   Explain these files not as static text documents, but as active valves, registers, and memory registers in a virtual co-processing CPU.
*   Use chronological workflows to demonstrate how a single file change propagates through the tree during a development turn.
