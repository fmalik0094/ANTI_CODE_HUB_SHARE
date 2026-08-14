# ANTI-CODE HUB DUAL-IDE CO-PROCESSING OPERATIONAL MANUAL (UAWC 1.0)

================================================================================
         DUAL-IDE HYBRID SYNC & COORDINATED HANDOVER PIPELINE
================================================================================

#### SECTION 1: MASTER TOPOLOGY INTEGRATION (THE SHARED WORKSPACE)

The hybrid co-processing model operates concurrently inside the same repository workspace, segregating the planning layer (Antigravity) and the stateful building layer (VS Code).

```text
ANTI_CODE-HUB/
├── .agent/                           # Shared AI Brain & Workflows (Antigravity)
│   ├── rules/                        # Global Permissions Rules (DENY > ASK > ALLOW)
│   ├── workflows/                    # Genesis, Entry, and Exit prompt checklists
│   └── states/                       # Active registry index and snapshot vaults
├── .codex/                           # Orchestrator limits & command blocklist (VS Code)
├── .vscode/                          # Watch exclusions & task commands (VS Code)
├── .state/                           # Persistent delta change trackers (VS Code)
├── validators/                       # Programmatic verification checkers (VS Code)
├── src/                              # Unified production directories (/vba, /python, /powershell)
└── temp/                             # Ephemeral payload staging directories
```

---

#### SECTION 2: CATEGORY CO-PROCESSING ROLES & CONFIGURATION SEPARATIONS

##### 1. Google Antigravity (Stateless Planning Core)
Responsible for structural planning, parsing requirements, and managing state serialization snapshot binaries.
*   **`main.md` (Master Plan):** Stores global variables (`[TECH_STACK]`, `[GLOBAL_OBJECTIVE]`, `[ACTIVE_CONSTRAINTS]`) to prime the planning engine without session token overhead.
*   **`AGENTS.md` (Squad Hierarchy):** Isolates sub-agent scopes (e.g., Harvester, Auditor, Reporter) to block unauthorized path access or tool execution.
*   **`states/[DOMAIN_NAME]_V*.md` (State Snapshot):** Compiles cumulative decisions, delta logs, and the "next execution node," allowing instantaneous environment context restoration in clean chats.

##### 2. VS Code (Stateful Execution Core)
Responsible for system-level tool operations, script runs, local code modifications, and running deterministic validators.
*   **`.vscode/settings.json` (Exclusion Anchors):** Masks dynamic areas (e.g., `/logs`, `/temp`, `*.csv`) to prevent infinite indexing watch racing.
*   **`.vscode/tasks.json` (Command Wrappers):** Standardizes validation script command lines into editor task runners.
*   **`.state/DELTA_LOG.md` (Change Log Ledger):** Documents a granular, chronological ledger of all project modifications to prevent configuration drift.

---

#### SECTION 3: MULTI-IDE DUAL FILTRATION AND IGNORE BLUEPRINTS

Symmetrical exclusion rules block background watch racing, drive deadlocks, and context window saturation.

##### 1. Watcher Ignorers (`.vscode/settings.json` vs `.geminiignore`)
Both systems mask identical folders to ensure filesystem safety:
*   *VS Code Watcher Exclude:* `**/logs/**`, `**/temp/**`, `**/.state/**`, `**/.agent/states/**`.
*   *Antigravity Ingest Exclude:* `logs/`, `temp/`, `output/`, `artifacts/`, `.state/`, `.agent/states/`, `.vscode/`, `.codex/`.

##### 2. Security Boundaries (`.aiexclude`)
Standardizes a hard blocks manifest, preventing credentials or keys from leaking into reasoning context paths:
*   *Blocked Coordinates:* `**/*.secret`, `**/*.key`, `**/*.pem`, `credentials/`, `config/private/`.

---

#### SECTION 4: CO-PROCESSING LIFECYCLE (WALKTHROUGH SIMULATION)

```text
 [STAGE 1: PLAN (Antigravity)]           [STAGE 2: BUILD (VS Code)]          [STAGE 3: REAP (Dual-IDE Sync)]
 1. Paste Genesis workflow script. ───>  1. Open shared workspace paths. ───>  1. Trigger Exit workflow check.
 2. Generate Domain_V1.0.md state.       2. Read configuration rules.          2. Overwrite Domain_V1.1.md.
 3. Paste Entry resumption rules.        3. Edit src/ folders.                 3. Append Registry ledger row.
 4. Pause at Authorization Hold.         4. Run tasks.json validators.         4. Close chat to flush memory.
```

##### Co-Processing Run: KRAS Mutation Tracker
To query mutation consequences from the Ensembl API and structural models from the Protein Data Bank (PDB):

1.  **Stage 1: Genesis Planning (Antigravity)**
    *   Developer inputs the unstructured genomics workflow idea below the `01_genesis_prompt.md` header in a stateless Antigravity session.
    *   The model compiles the objectives, constraints, and failures into `.agent/states/GENOMICS_V1.0.md`.

2.  **Stage 2: Entry Resumption Hold (Antigravity)**
    *   Developer pastes `02_entry_prompt.md` and the contents of `GENOMICS_V1.0.md` into the active chat.
    *   The planning engine outputs the Action Plan and halts execution at `[PENDING OPERATOR APPROVAL]`. The operator reviews the proposed coordinates and types `APPROVED` to release the console lock.

3.  **Stage 3: Execution and Build (VS Code)**
    *   The developer opens the workspace in VS Code.
    *   The developer modifies source code under `src/` to fetch gene data, outputting sequence coordinates to `temp/kras.pdb`. Symmetrical watch exclusions mask these files, keeping disk access stable.
    *   Developer runs the automated tasks inside `.vscode/tasks.json` to execute `validators/validate_structure.py` on the workspace.

4.  **Stage 4: Exit and Synchronization (Antigravity)**
    *   At the end of the turn, the developer inputs `03_exit_prompt.md` into the Antigravity session.
    *   Block 1 generates `GENOMICS_V1.1.md`, which is saved as an overwrite to the local state file.
    *   Block 2 outputs the registry row, which is appended to `.agent/states/_ACTIVE_INDEX.md`.
    *   The chat context is closed, flushing memory caches safely.

---

#### SECTION 5: FAILURE MODES & OPERATIONAL SAFEGUARDS

##### 1. Watcher Feedback Racing
*   *Risk:* Mismatched workspace search ignore configurations, causing write-loop cascades that lock up drive I/O.
*   *Resolution:* Symmetrical exclusions are locked in `.vscode/settings.json` and `.geminiignore`.

##### 2. Semantic Context Saturation
*   *Risk:* Passing heavy data files directly into the reasoning window.
*   *Resolution:* Exclude all raw datasets from LLM sweeps and process them locally using sandbox Python verification files in `validators/`.

##### 3. Explorer Handle Deadlocks
*   *Risk:* Unvetted network loop scans on UNC shares causing MUP handle deadlocks.
*   *Resolution:* Execute commands targeting absolute local folders, copy outputs recursively, and reset filesystem handles using:
    `Stop-Process -Name explorer -Force; Start-Process explorer`
