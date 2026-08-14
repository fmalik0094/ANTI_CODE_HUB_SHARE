# ANTI-CODE HUB: DUAL-IDE CO-PROCESSING OPERATIONAL MANUAL

This manual serves as the active reference guide for running the `ORCHESTRATION_V1.0` Dual-IDE workspace configuration under the `anti-code hub/` subdirectory. It covers configuration shifts, variable controls, and execution routines used to manage co-processing workflows between Google Antigravity and VS Code.

---

## CATEGORY 1: GOOGLE ANTIGRAVITY (Stateless Planning Core)

Google Antigravity operates as the stateless planning engine. It does not compile code or maintain local system caches. It relies entirely on structured markdown rule vectors and State Binaries to restore context.

### 1. `GEMINI.md` (The Project Master Plan)
*   **Purpose:** Configures global rules, persona variables, and baseline design instructions.
*   **Variable Shift:** `[TECH_STACK]`, `[GLOBAL_OBJECTIVE]`, `[ACTIVE_CONSTRAINTS]`
*   **Evolution Strategy (Architectural Pivot):**
    *   *Phase 1 (Prototyping):* Variables are set to: `[TECH_STACK]: Python, SQLite, rapid iteration, no strict typing`.
    *   *Phase 2 (Production):* The developer manually edits the variables to: `[TECH_STACK]: TypeScript, PostgreSQL, strict Prisma ORM validation, 100% test coverage`.
    *   **Usage Context:** By updating these variables in the master rules file, the Architect’s planning logic shifts immediately for all subsequent turns, eliminating the need to re-prime the system in a new chat.

### 2. `AGENTS.md` (The Squad Hierarchy)
*   **Purpose:** Defines sub-agent boundaries, role structures, and process isolation.
*   **Variable Shift:** `[AGENT_ROLES]`, `[NETWORK_PERMISSIONS]`
*   **Evolution Strategy (Resource Reallocation):**
    *   *Data Gathering Phase:* Configured with `[AGENT_ROLES]: Harvester (read_url permissions), Parser (local file sanitization)`.
    *   *Refactoring Phase:* Delete initial roles and redefine as `[AGENT_ROLES]: Auditor (read-only code scanning), Refactor_Specialist (write access restricted to /src/utils/)`.
    *   **Usage Context:** Shifts access and security privileges dynamically as the project moves from initial data ingestion to code cleanup, protecting directory boundaries from unauthorized edits.

### 3. `states/[DOMAIN_NAME]_V*.md` (The Cognitive State Binary)
*   **Purpose:** Houses the serialized snapshot representing the project's cumulative memory.
*   **Variable Shift:** `[CUMULATIVE_LOGIC_LEDGER]`, `[FAILURE_MODES]`
*   **Evolution Strategy (Context Serialization):**
    *   *V1.0 (Genesis):* Contains only the initial design blueprints, file topologies, and entry commands.
    *   *V4.2 (Iterated State):* Contains locked schemas, production-ready API pathways, and updated failure logs (e.g., `"Failure Mode: Memory leak in worker node during high throughput"`).
    *   **Usage Context:** Injecting `V4.2` directly into a clean chat instance instantly restores the model’s environment memory, bypassing the token overhead of parsing history from previous sessions.

---

## CATEGORY 2: VS CODE (Stateful Execution Core)

VS Code operates as the stateful working environment. It manages shell tasks, handles local file edits, runs validation scripts, and outputs trace logs.

### 1. `.vscode/settings.json` (Exclusion Anchors)
*   **Purpose:** Masks directories to prevent background watch racing.
*   **Variable Shift:** `"search.exclude"`, `"files.watcherExclude"`
*   **Usage Context:** Excludes dynamic workspaces (`logs/`, `temp/`, `*.csv`) so that high-frequency write operations by terminal tools do not trigger search loops or lock filesystem access.

### 2. `.vscode/tasks.json` (Command Wrappers)
*   **Purpose:** Maps command-line triggers to short execution commands.
*   **Variable Shift:** `"command"`, `"args"`
*   **Usage Context:** Provides the developer with one-click verification runners, automating script calls (like `validate_structure.py`) to enforce consistency.

### 3. `.state/DELTA_LOG.md` (Disk Delta Ledger)
*   **Purpose:** Maintains a chronological record of files modified during development.
*   **Variable Shift:** `[SESSION_DELTA]`, `[STATE_HASH]`
*   **Usage Context:** Provides VS Code sub-agents with a tracking baseline, logging what changes were committed and verifying structural hashes.

---

## CATEGORY 3: CO-PROCESSING WORKFLOW & SIMULATION

The two systems run side-by-side to construct features, verify code, and sync states.

```text
[Stage 1: GENESIS] ───────> [Stage 2: ENTRY HOLD] ───────> [Stage 3: EXECUTION] ───────> [Stage 4: EXIT SYNC]
- Compile raw goal          - Ingest State Binary          - Edit code in VS Code       - Run exit workflow
- Write V1.0 state file      - Await operator APPROVED      - Exclude logs and temp      - Output new state V1.1
                            - Hold console lock            - Sandboxed execution        - Log to index registry
```

### Operational Simulation: KRAS Mutation Tracker
To query mutation consequences from the Ensembl API and structural models from the Protein Data Bank (PDB):

1.  **Genesis Phase:** The developer pastes `.agents/workflows/01_genesis_prompt.md` into the Antigravity chat to create `.agents/states/GENOMICS_V1.0.md`.
2.  **Entry Hold Phase:** The developer initiates a working session using `.agents/workflows/02_entry_and_propose.md` and `GENOMICS_V1.0.md`. The planning engine outputs an Action Plan and halts on `[PENDING OPERATOR APPROVAL]`. The operator reviews it and enters **APPROVED**.
3.  **Execution Phase:** Code is edited in VS Code under `src/` and tested. Run trace metrics write to `logs/run.log` and sequence coordinates download to `temp/kras.pdb`. Symmetrical watch rules mask these updates, keeping the workspace stable.
4.  **Exit Sync Phase:** The developer pastes `.agents/workflows/03_exit_and_sync.md` to serialize modifications. Block 1 overwrites `.agents/states/GENOMICS_V1.1.md` and Block 2 appends the tracking metadata row to `.agents/states/_ACTIVE_INDEX.md`. The workspace is shut down securely.
