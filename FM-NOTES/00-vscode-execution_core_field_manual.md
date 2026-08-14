# VS CODE STATEFUL EXECUTION CORE - OPERATIONAL FIELD MANUAL (UAWC 1.0)

================================================================================
          VS CODE BUILDER VAULT & STATEFUL EXECUTION CONTRACT
================================================================================

#### SECTION 1: VS CODE DIRECTORY SCAFFOLDING (THE EXECUTION MAP)

The stateful construction layer, local verification scripts, and editor panel configurations reside inside the `vscode/` scope of the repository.

```text
vscode/
├── .vscode/                         # Editor Configuration Layer
│   ├── settings.json                # Index Exclusions & Linter Controls
│   └── tasks.json                   # Command Shortcuts & Validation Runners
├── .codex/                          # Execution Agent Configuration panel
│   ├── config.toml                  # Session Limits & Terminal command Blocklist
│   ├── instructions.md              # Active Syntax Guidelines & Coding Rules
│   └── agents/                      # Specialist Agent Profiles
│       └── security_auditor.toml    # Sandbox Auditor Configuration
├── .state/                          # State Control Layer (Split Ledgers)
│   ├── BASELINE_HASH.md             # Structural Ground Truth Hash Key
│   ├── DELTA_LOG.md                 # micro-Turn Transaction Log
│   └── DECISIONS.md                 # Immutable Architectural Rules Registry
├── validators/                      # Sandbox Verification Scripts
│   ├── validate_structure.py        # Structural Path Ingest Check
│   └── validate_config.py           # Environment Variables & Path Verify
└── src/                             # Production Source Code Directory
```

---

#### SECTION 2: CORE CONFIGURATIONS & EVOLUTION STRATEGIES

##### 1. Local Codebase Guidelines (`.codex/instructions.md`)
Declares structural syntax rules and design principles used directly during active construction turns.

*   *Evolution Strategy:*
    *   **Prototyping:** Instructions are kept flexible to allow the model to draft prototypes and explore library features.
    *   **Release Candidate:** Guidelines are appended with strict typings, strict error boundaries, and design constraints (e.g., *"All exports must utilize explicit types; no implicit 'any' declarations permitted."*).

##### 2. Agent Execution Constraints (`.codex/config.toml`)
Restricts terminal commands and manages token ceilings.

```toml
[agent_orchestration]
framework = "VSCode-Codex-MultiAgent"
version = "V1.0"
default_mode = "PLANNING"
confidence_threshold = 0.85

[token_management]
max_context_tokens = 1048576
buffer_tokens = 24576
exclusion_mode = "STRICT"

[execution_policies]
terminal_access = "REQUEST_REVIEW"
deny_list = ["rm", "sudo", "curl", "wget"]
```

##### 3. Script Validation Lifecycle (`validators/`)
Separates validation checks from LLM heuristics. Centralized Python scripts run deterministic algorithms to guarantee codebase correctness.

*   *Maturation Strategy:*
    *   **Sprint 1:** Structural checks. Validates file location targets on disk.
    *   **Sprint 3:** AST (Abstract Syntax Tree) checks. Validator parses python/VBA structures programmatically, verifying that required middleware wrappers or licensing headers are present prior to repository commit authorization.

##### 4. Split Delta Tracking Ledger (`.state/`)
Maintains a granular, chronological ledger of all project modifications to prevent history decay.
*   `BASELINE_HASH.md`: Locks down the initial workspace structure.
*   `DELTA_LOG.md`: Records micro-turn change records including exact files changed, modification summaries, and target SHA256 hashes.
*   `DECISIONS.md`: Stores locked design variables to halt retroactive logic rewriting.

---

#### SECTION 3: VS CODE SQUAD - AGENT PATHS & EXECUTION MATRIX

```text
===================================================================================================
ROLE                 IDE           PRIMARY OBJECTIVE             PATH ACCESS     PRIVILEGE LEVEL
===================================================================================================
5. Orchestrator      VS Code       Specialist Task Allocator     AGENTS.md       Read-Only
6. VBA Specialist    VS Code       Single-Module Script Compiler src/vba/        Read/Write
7. Python Validator  VS Code       AST Analysis Automation Engine src/python/     Read/Write
8. Shell Specialist  VS Code       PowerShell Task Builder       src/powershell/ Read/Write
===================================================================================================
```

##### 1. Orchestrator
*   **Task:** Evaluates tasks and delegates work files to specific language specialists.
*   **Path Bounds:** Reads `AGENTS.md` and `.codex/config.toml`. Prohibited from modifying source code.
*   **Flow Constraint:** Coordinates multi-file updates by routing parameters to secondary agents.

##### 2. VBA Specialist
*   **Task:** Compiles clean VBA macro files, applying late-binding compile constraints.
*   **Path Bounds:** Restricted to `src/vba/`.
*   **Flow Constraint:** Blocked from accessing system PowerShell utilities or making network requests.

##### 3. Python Validator
*   **Task:** Analyzes script typings and coordinates testing validations.
*   **Path Bounds:** Confined to `src/python/` and `validators/`.
*   **Flow Constraint:** Automatically triggers AST and testing checkers on-save.

##### 4. Shell Specialist
*   **Task:** Builds PowerShell file manipulation and system maintenance scripts.
*   **Path Bounds:** Confined to `src/powershell/`.
*   **Flow Constraint:** Prohibited from executing primitives matching the TOML blocklist.

---

#### SECTION 4: OPERATION LIFE CYCLE (WALKTHROUGH SIMULATION)

```text
[STAGE 1: ALIGN] ───> [STAGE 2: EVALUATE] ───> [STAGE 3: CODE] ───> [STAGE 4: VERIFY] ───> [STAGE 5: LOCK]
Check BASELINE.md     Read config.toml         Modify /src/ files.  Run tasks.json        Update DELTA_LOG.md
to confirm paths.     to verify blocklist.     Ignore temp/logs.    validators.           and DECISIONS.md.
```

1.  **Stage 1: Aligning to Baseline:** The agent reads `.state/BASELINE_HASH.md` to confirm folder mappings are correct.
2.  **Stage 2: Parsing Sandboxing Rules:** The agent checks `.codex/config.toml` to ensure the session limits and command blocklists are applied.
3.  **Stage 3: Coding & Isolation:** Modifies source files in `src/`. The files generated are excluded from watcher cycles via `.vscode/settings.json` to preserve system memory.
4.  **Stage 4: Programmatic Verification:** The developer/agent runs targets in `.vscode/tasks.json` to execute validation check scripts in `validators/` (e.g. `validate_structure.py`).
5.  **Stage 5: Serialization Lock:** If validators exit with code `0`, the delta is logged to `.state/DELTA_LOG.md` and design rules are locked in `.state/DECISIONS.md`.

---

#### SECTION 5: SYSTEMIC SECURITY GUARDRAILS

##### 1. Watcher Index Racing Exclusions
Large output datasets, binary files, and active logs are excluded from active search scopes to stop drive lockups:
*   *Settings Matrix:* Never remove `/logs`, `/temp`, or `.state/` directories from `search.exclude` and `files.watcherExclude` inside `.vscode/settings.json`.

##### 2. Command Filter Security Policies
Commands processed via Model Context Protocol (MCP) or local tasks are intercepted. Primitives matching `rm`, `sudo`, `curl`, or `wget` are blocked at the configuration layer (`config.toml`), preventing unauthorized access to local environments or network sockets.
