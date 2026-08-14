# UAWC 1.0 Dynamic Flow Orchestration User Manual

================================================================================
          UNIFIED AGENT WORKSPACE CONTRACT (UAWC 1.0) - REPOSITORY SPEC
                      DYNAMIC PATH & MULTI-AGENT ORCHESTRATION
================================================================================

#### SECTION 1: MASTER DIRECTORY TOPOLOGY (THE REPOSITORY SCAFFOLDING)

The absolute file-system framework for the hybrid workspace is deployed at root directory `C:\01_LOCAL_CODING_F.M\00-TEST-ONLY\ANTI_CODE-HUB\`. It isolates planning, building, templates, and documentation into distinct directory panels.

```text
ANTI_CODE-HUB/
├── FM-NOTES/                         # Consolidated Documentation & Field Manuals
│   ├── 00-antigravity-state_manager_field_manual.md
│   ├── 00-vscode-execution_core_field_manual.md
│   ├── 00-anticode-dual_ide_co_processing_manual.md
│   ├── 00.00-LEXICON.md              # Symmetrical Lexicon & Definitions
│   ├── 01_sidebyside comparaision_anti-vs.md
│   └── base_workspace_template.md    # [NEW] CWI/CNC Compliant Base Workspace Template
├── antigravity/                      # Stateless Planning Workspace Panel
│   ├── .agents/                      # Shared System Lifecycles & Rules
│   │   ├── rules/
│   │   │   ├── global.md             # Baseline Precedence (DENY > ASK > ALLOW)
│   │   │   └── base_workspace_template.md # [NEW] Symmetrical Base Template
│   │   ├── workflows/                # Genesis, Entry, and Exit checklists
│   │   └── states/                   # Snapshot Vault & Active Domain Ledger
│   ├── .gemini/GEMINI.md             # Non-Conversational Meta-Rules
│   ├── .geminiignore                 # Context Buffer Ingestion Exclude list
│   ├── AGENTS.md                     # Antigravity Squad Definition Matrix
│   └── hub_manager.py                # [NEW] Local python CLI utility for pruning/merging
├── vscode/                           # Stateful Execution Workspace Panel
│   ├── .vscode/                      # IDE launch profiles, settings & tasks
│   ├── .codex/                       # Session limit & command blocklist configurations
│   ├── .state/                       # Split Delta Ledger tracks (BASELINE, DELTA_LOG, etc.)
│   ├── validators/                   # Python validation checkers
│   └── src/                          # Production Codebase targets (/vba, /python, etc.)
├── anti-code hub/                    # Integrated Dual-IDE Co-Processing Template
│   ├── .agents/                      # Symmetrical copy of planning controls
│   │   ├── rules/
│   │   │   ├── global.md             # Baseline Precedence
│   │   │   └── base_workspace_template.md # [NEW] Symmetrical Base Template
│   │   ├── workflows/
│   │   └── states/
│   ├── .codex/                       # Symmetrical copy of execution controls
│   ├── .state/                       # Symmetrical copy of delta ledger tracks
│   ├── .vscode/                      # Shared editor options
│   ├── validators/                   # Unified validator execution files
│   ├── src/                          # Production codebase files
│   ├── AGENTS.md                     # Integrated agent definitions
│   └── hub_manager.py                # [NEW] Local python CLI utility for pruning/merging
├── main.md                           # Master Co-Processing Entrypoint Manual
├── .geminiignore                     # Root Ingestion Filter
├── .aiexclude                        # MCP Hard File System Blocklist
└── .gitignore                        # Git Source Control Exclusion Ledger
```

---

#### SECTION 2: DUAL-IDE FILTRATION MATRIX (LOOP REVERSAL PREVENTION)

To block background indexing loops from locking files on disk or causing file-watcher racing, directory boundary paths must be excluded symmetrically in settings.

##### 1. VS Code Settings Blueprint (`vscode/.vscode/settings.json`)

```json
{
  "search.exclude": {
    "**/logs": true,
    "**/temp": true,
    "**/*.csv": true,
    "**/*.xlsm": true,
    "**/*.pdf": true,
    "**/.state": true,
    "**/.agents/states": true
  },
  "files.watcherExclude": {
    "**/logs/**": true,
    "**/temp/**": true,
    "**/.state/**": true,
    "**/.agents/states/**": true
  },
  "editor.formatOnSave": true
}
```

##### 2. Antigravity Ingestion Exclusion Blueprint (`antigravity/.geminiignore`)

```text
# EXCLUSION MATRIX: ANTIGRAVITY CONTEXT WINDOW PROTECTION
logs/
temp/
output/
artifacts/
*.csv
*.xlsm
*.xlsx
*.pptx
*.pdf
.state/
.agents/states/
.vscode/
.codex/
```

##### 3. Security Boundary Blueprint (`.aiexclude`)

```text
# CRYPTOGRAPHIC & PRIVACY HARD BLOCKLIST - INTERCEPTED AT FS LAYER
**/*.secret
**/*.key
**/*.pem
credentials/
config/private/
```

---

#### SECTION 3: MULTI-AGENT INTERACTION MATRIX & DYNAMIC PATH BOUNDARIES

The architecture orchestrates **8 specialized agents** across distinct runtime sessions. Each agent is strictly confined to specific workspace directory nodes.

```text
===================================================================================================
ROLE                 IDE           PRIMARY OBJECTIVE             PATH ACCESS     PRIVILEGE LEVEL
===================================================================================================
1. Architect Core    Antigravity   Session Task Planner          .agents/        Read-Only
2. Harvester         Antigravity   MCP Data Ingest               External / API  Network Read-Only
3. Auditor           Antigravity   Cross-Session Token Validator .state/         Read-Only
4. Reporter          Antigravity   Log & Document Serializer     temp/           Write-Only
5. Orchestrator      VS Code       Specialist Task Allocator     AGENTS.md       Read-Only
6. VBA Specialist    VS Code       Single-Module Script Compiler src/vba/        Read/Write
7. Python Validator  VS Code       AST Analysis Automation Engine src/python/     Read/Write
8. Shell Specialist  VS Code       PowerShell Task Builder       src/powershell/ Read/Write
===================================================================================================
```

##### 1. Antigravity Agent Squad (Sensory Ingest Layer - Monitor 1)

* **Architect Core:**
  * *Task:* Ingests high-level customer blueprints and outputs modular system change vectors.
  * *Path Interaction:* Scans `antigravity/.agents/rules/` and `antigravity/.agents/skills/` to prioritize execution rules before planning code shifts.
  * *Dynamic Flow Rule:* Prohibited from touching `/src/` directories directly. It writes the planned schema change vector exclusively to the `.state/` staging vault.

* **Harvester:**
  * *Task:* Queries authorized Model Context Protocol (MCP) data streams (e.g., live stock tables, network paths).
  * *Path Interaction:* Sandboxed outside the physical workspace directory structure. Reads remote inputs or server endpoints.
  * *Dynamic Flow Rule:* Zero local directory write privileges. It streams collected payloads straight to the `temp/raw_payloads/` directory.

* **Auditor:**
  * *Task:* Performs cross-session verification passes to guard against logic drift and token degradation.
  * *Path Interaction:* Targets `.state/BASELINE_HASH.md` and `.state/DECISIONS.md`.
  * *Dynamic Flow Rule:* Monitors historical project boundaries, stopping the active execution pipeline if an unauthorized framework rewrite is detected.

* **Reporter:**
  * *Task:* Flushes active conversation history and serializes context changes down to plain text.
  * *Path Interaction:* Appends and overwrites files inside `.state/DELTA_LOG.md` and `antigravity/.agents/states/_ACTIVE_INDEX.md`.
  * *Dynamic Flow Rule:* Operates at the end of each turn, turning temporary workspace memory into disk persistence blocks.

##### 2. VS Code Codex Agent Squad (Stateful Construction Layer - Monitor 2)

* **Orchestrator:**
  * *Task:* Parses local editor commands triggered via `.vscode/tasks.json` or inline shortcuts.
  * *Path Interaction:* Evaluates `AGENTS.md` and `.codex/config.toml`.
  * *Dynamic Flow Rule:* Coordinates multi-file refactoring runs by delegating explicit, localized strings to language specialists.

* **VBA Specialist:**
  * *Task:* Builds production macros, applying late-binding compile-first architecture constraints.
  * *Path Interaction:* Confined to directory path `src/vba/`.
  * *Dynamic Flow Rule:* Prohibited from accessing system-level PowerShell scripts or external network modules.

* **Python Validator:**
  * *Task:* Compiles internal analysis tools and maintains script file typings.
  * *Path Interaction:* Confined to directory path `src/python/` and `validators/`.
  * *Dynamic Flow Rule:* Automatically executes `validators/validate_structure.py` on-save to protect against code-breaking modifications.

* **Shell Specialist:**
  * *Task:* Builds path-hardened local file manipulation scripts and handles local drive configurations.
  * *Path Interaction:* Confined to directory path `src/powershell/`.
  * *Dynamic Flow Rule:* Command primitives are filtered against a hardcoded blocklist (`rm`, `sudo`, `wget`, `curl`) managed inside `.codex/config.toml`.

---

#### SECTION 4: THE INTEGRATED TRIPLE-STAGE LIFECYCLE (THE RUNTIME HANDSHAKE)

To operate both environments concurrently without creating version forks or folder-locking issues, execute this systematic runtime lifecycle:

```text
[STAGE 1: PLAN (Antigravity)]           [STAGE 2: BUILD (VS Code)]          [STAGE 3: REAP (Dual-IDE Sync)]
1. Run Genesis Prompt Compiler.  ───>   1. Open Local Workspace.     ───>   1. Trigger Exit Prompt Node.
2. Formulate Modular Blueprint.         2. Execute Specialist Run.          2. Run Python Schema Checks.
3. Lock Core Decision Variables.        3. Mutate Code inside /src/.        3. Flush Active Chat Cache.
4. Export Target State Binary.          4. Execute Local Validators.        4. Append Ledger Record Row.
```

##### Step 1: High-Level Planning & Genesis Inception

* **Action:** Open your clean Google Antigravity/Gemini environment window on Monitor 1. Paste the `antigravity/.agents/workflows/01_genesis_prompt.md` block into the terminal, wrapping your raw project idea underneath.
* **Data Flow:** The **Antigravity Architect Agent** processes the parameters, bypasses conversational text summaries, and generates a standalone `[DOMAIN]_V1.0.md` State Binary block.
* **Path Storage:** Save this file block physically to your drive path under `antigravity/.agents/states/[DOMAIN]_V1.0.md`.

##### Step 2: The Dual-IDE Execution & Validation Cycle

* **Action:** Launch standard VS Code on Monitor 2, targeted at the exact same workspace root directory.
* **Data Flow:** The **VS Code Orchestrator Agent** ingests `vscode/.codex/config.toml` and reads the target goals from your saved State Binary.
* **Workspace Protection:** While you use Antigravity on Monitor 1 to brainstorm structural expansions, you can run terminal scripts, automate data processing loops, and review system metrics in VS Code on Monitor 2.
* **Collision Override:** Both engines access the filesystem in parallel without locking errors. The symmetrical parameters defined in `.geminiignore` and `.vscode/settings.json` prevent background scanners from thrashing the same target storage spaces.
* **Deterministic Assertion:** Code generation cannot be injected into production tracks based on semantic reasoning alone. The VS Code task manager (`tasks.json`) runs local scripts (`validators/validate_formula.py`) to mathematically confirm logic outputs before authorization gates unlock.

##### Step 3: Complete Turn Serialization & State Sync

* **Action:** When pausing or halting development, paste the contents of `antigravity/.agents/workflows/03_exit_and_sync.md` into your active communication channels.
* **Data Flow:** The **Antigravity Reporter Agent** stops active trajectories and generates exactly two distinct output text arrays:
  1. *Block 1 (The Incremental State Binary):* Carries the updated cumulative decision ledger and session deltas. Overwrite your local `antigravity/.agents/states/[DOMAIN]_V*.md` file with this target block.
  2. *Block 2 (The Registry Tracking Row):* A single tabular string documenting your active progress metrics.
* **Path Storage:** Open `antigravity/.agents/states/_ACTIVE_INDEX.md` in your local editor and append the Block 2 row to the bottom of the ledger file. Close your active conversations safely; your entire technical timeline is stored in plain text on your local disk, ready for immediate ingestion during the next session turn.

---

#### SECTION 5: SYSTEMIC FAILURE MODES & OPERATIONAL SAFEGUARDS

##### 1. Watcher State Racing (Infinite Disk-Write Loops)

* *Cause:* Mismatched workspace ignore files. If Antigravity generates a state binary and VS Code's indexing daemon tracks it as a change event, it triggers an automated build runner, creating an infinite background loop that thrashes disk I/O.
* *Safe Solution:* The workspace synchronization settings are locked. Never remove `.state/` or `antigravity/.agents/states/` from either `.geminiignore` or `.vscode/settings.json`.

##### 2. Semantic Data Inflation (Context Blending)

* *Cause:* Passing raw database arrays or massive manufacturing CSV assets straight into general reasoning windows, causing immediate context window degradation.
* *Safe Solution:* The platform enforces a **Strict Ingestion Guardrail**. Broad LLM layers read configuration maps, JSON typing schemas, and short decision blocks. Heavy processing data files are handled locally within isolated execution sandboxes (`validators/`).

##### 3. Local Handle Deadlocks (`explorer.exe` Folder Lockout)

* *Cause:* Windows MUP handles refuse to drop file locks over network mappings (`\\swfs01-mtl\COMPANY\`) when automated sub-agents fire high-frequency update loops.
* *Safe Solution:* Do not execute open command arrays directly on raw strings. Always pass fully qualified network directories wrapped in deep string parameters (`cd "UNC_PATH"`). If a process deadlock occurs, run the native automation terminal script:
  `Stop-Process -Name explorer -Force; Start-Process explorer`

---

#### SECTION 6: RETROSPECTIVE & ARCHITECTURAL LESSONS (TOPIC HUB INTEGRATION)

Based on the development lifecycle of the CNC and CWI production environments, we have codified several critical principles for multi-agent hybrid work:

##### 1. Save-State Architecture & State Pruning
*   **The Principle:** Treating the workspace state as a serialized versioned snapshot (`_ACTIVE_INDEX.md` and domain binaries) prevents the LLM from losing its structural constraints over long chats.
*   **Active Pruning:** The introduction of the `hub_manager.py` command line utility automates the archival of older, obsolete state iterations to a dedicated `/archive/` directory. This keeps the primary `.agents/states/` scope clean and context-tight.

##### 2. Localized Multi-Agent Governance
*   **The Principle:** Agents must be constrained by local workspace configurations rather than general system-wide profiles.
*   **Systemic Guardrails:**
    *   **Config Isolation:** Confining VS Code / Codex behavior inside `.codex/config.toml` ensures that rules (e.g. allowed write roots, max line edits) are tailored to the codebase scope.
    *   **Watcher Boundaries:** IDE watcher exclusions must completely block the monitoring of `.state/` and `/logs/` directories to prevent infinite loops.
    *   **Zero-Trust Command Gates:** Primitives matching system mutations (e.g., `rm`, `sudo`, `wget`, `curl`) must go through explicit, manual operator approval loops.

##### 3. Path Resilience & Relative Anchors
*   **The Principle:** Governance configs and active instructions must use relative paths (e.g. `./validators/`) rather than absolute path strings. This ensures configuration robustness across different staging environments, absolute project mounts, and team-member systems.

##### 4. Quality Gates & Validator Loops
*   **The Principle:** Logic verification should not be deferred. Automated validators (such as syntax linters and structural integrity scripts) running on-save mathematically ensure that no regressions are committed to `src/` prior to the generation of exit state binaries.

