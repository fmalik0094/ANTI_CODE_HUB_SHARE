# GOOGLE ANTIGRAVITY STATE MANAGER - OPERATIONAL FIELD MANUAL (UAWC 1.0)

================================================================================
         ANTIGRAVITY METADATA VAULT & CONTEXT ORCHESTRATION CONTRACT
================================================================================

#### SECTION 1: ANTIGRAVITY DIRECTORY TOPOLOGY (THE PLANNING MAP)

The planning and meta-state tracking layer resides within the `antigravity/` scope of the `C:\01_LOCAL_CODING_F.M\00-TEST-ONLY\ANTI_CODE-HUB\` directory tree.

```text
antigravity/
├── .gemini/                         # Primary Architect Core Context Panel
│   └── GEMINI.md                    # Core Meta-Rules & Non-Conversational Directive
├── .agents/                         # Shared Process Execution Managers
│   ├── rules/                       # Always-On System Governance
│   │   └── global.md                # Precedence Constraints (DENY > ASK > ALLOW)
│   ├── workflows/                   # Session Lifecycle Turn Checklists
│   │   ├── 01_genesis_prompt.md     # Command: INITIATE PROJECT GENESIS
│   │   ├── 02_entry_and_propose.md  # Command: INJECT STATE & RESUME
│   │   └── 03_exit_and_sync.md      # Command: INITIATE FULL STATE SERIALIZATION
│   └── states/                      # Alphanumeric Memory Vaults
│       ├── _ACTIVE_INDEX.md         # Master Domain Registry Index
│       └── [DOMAIN_NAME]_V*.md      # Compressed Session Snapshots
├── .geminiignore                    # Ingestion Context Filter (Token Preserver)
└── AGENTS.md                        # Multi-Agent Segregation Definitions
```

---

#### SECTION 2: METADATA RULESETS & BOUNDARY FILTER BLOCKS

##### 1. Meta-State Rule Manifest (`.gemini/GEMINI.md`)
Forces the reasoning engine to function purely as a stateless technical context compiler.

```markdown
# SYSTEM CORE: META-RULES & SAFETY CONTROLS
[ROLE: SYSTEM STATE MANAGER]
*   **Operating Mandate:** This workspace functions exclusively as a Meta-State Vault. It does not execute application code or compile production software. Its sole function is to process unstructured cognitive inputs, serialize cumulative logic into deterministic State Binaries (.md), and update the Master Registry.
*   **Response Style:** Strict engineer-level language. Concise. Zero fluff. You are completely barred from using conversational greetings, transitional pleasantries, or introductory sentences. Deliver raw, structural outputs.
*   **Formatting Guardrail:** Always use standard plain text and basic Markdown for numbers and formulas to guarantee 100% data fidelity when copy-pasting directly into Microsoft Word, Excel, or Google Docs.
```

##### 2. Ingestion Context Guardrail (`.geminiignore`)
Trims the ingestion footprint to block context decay during broad scans.

```text
# EXCLUSION MATRIX: CORE PROTOCOL TOKEN PRESERVATION
logs/
temp/
output/
artifacts/
*.csv
*.xlsm
*.xlsx
*.pptx
*.pdf
.agents/states/
```

##### 3. Local Shell Precedence Matrix (`.agents/rules/global.md`)
Restricts system shell permissions, locking down local workspace command paths.

```markdown
# GLOBAL PRECEDENCE CONSTRAINTS
*   **Rule Hierarchy:** Absolute constraint resolution: DENY > ASK > ALLOW. Workspace configurations or local scripts can only restrict, never expand, this safety baseline.
*   **Implicit Policies:** Write access implies Read access. Deny Read access immediately enforces Deny Write access.
*   **Terminal Execution:** Policy set to REQUEST REVIEW. Unvetted terminal commands are explicitly blocked.
```

---

#### SECTION 3: ANTIGRAVITY SQUAD - AGENT PATHS & EXECUTION MATRIX

```text
===================================================================================================
ROLE                 IDE           PRIMARY OBJECTIVE             PATH ACCESS     PRIVILEGE LEVEL
===================================================================================================
1. Architect Core    Antigravity   Session Task Planner          .agent/         Read-Only
2. Harvester         Antigravity   MCP Data Ingest               External / API  Network Read-Only
3. Auditor           Antigravity   Cross-Session Token Validator .state/         Read-Only
4. Reporter          Antigravity   Log & Document Serializer     temp/           Write-Only
===================================================================================================
```

##### 1. Architect Core
*   **Task:** Parses high-level objectives and generates modular structural plans.
*   **Path Bounds:** Scans `.agents/rules/` and `.agents/skills/`. Prohibited from entering production `/src/` directories.
*   **Flow Constraint:** Writes plans to the state staging register, awaiting construction validation.

##### 2. Harvester
*   **Task:** Fetches external documentation and structural parameters via local Model Context Protocol (MCP) servers.
*   **Path Bounds:** Sandboxed from local folders. Only writes to `temp/raw_payloads/`.
*   **Flow Constraint:** Zero write permissions in `.agents/` or `/src/` directories.

##### 3. Auditor
*   **Task:** Conducts regression checking against historical ledger decisions to block design mutations.
*   **Path Bounds:** Targets `.agents/states/` and `.state/BASELINE_HASH.md`.
*   **Flow Constraint:** Raises alert flag and interrupts execution if unauthorized architectural rewrites are attempted.

##### 4. Reporter
*   **Task:** Compiles turn timeline updates and outputs registry summaries at the end of each session.
*   **Path Bounds:** Appends records directly inside `.agents/states/_ACTIVE_INDEX.md`.
*   **Flow Constraint:** Restricted to end-of-turn execution; flushes context buffers immediately post-write.

---

#### SECTION 4: THE ANTIGRAVITY OPERATIONAL LIFECYCLE (TRIPLE-STAGE LOOP)

```text
[PHASE 1: GENESIS]                    [PHASE 2: RESUMPTION & PROPOSE]       [PHASE 3: SYNC & EXIT]
- Input raw idea payload.             - Inject latest state binary.         - Run Exit prompt.
- Strip conversational fluff.         - Action Plan generated.              - Block 1: Snapshot updated.
- Output Domain_V1.0.md snapshot.     - Locked at AUTHORIZATION HOLD.       - Block 2: Table row appended.
- Save to local states/ folder.       - Operator enters APPROVED to run.    - Clear active memory buffers.
```

##### 1. Phase 1: Genesis (Topic Inception)
*   **Action:** Copy `.agents/workflows/01_genesis_prompt.md` into a clean chat.
*   **Input:** Append raw, unstructured notes under the `## UNSTRUCTURED OBJECTIVE` header.
*   **Output:** The model outputs a clean, structured `[DOMAIN]_V1.0.md` State Binary. Save this file directly inside `.agents/states/`.

##### 2. Phase 2: Resumption & Authorization Hold
*   **Action:** Paste `.agents/workflows/02_entry_and_propose.md` into the session.
*   **Input:** Attach the text of the latest `states/[DOMAIN]_V*.md` snapshot.
*   **Hold Mechanic:** The engine processes the snapshot and lists the immediate Action Plan. It halts execution and appends `[PENDING OPERATOR APPROVAL]`.
*   **Unlock Command:** The operator must manually review the plan and input `APPROVED` before any mutations or tool commands are executed.

##### 3. Phase 3: Synchronization & Exit
*   **Action:** Run `.agents/workflows/03_exit_and_sync.md` prior to closing the window.
*   **Output Block 1:** Overwrite the current local `states/[DOMAIN]_V*.md` snapshot (incrementing the version number).
*   **Output Block 2:** Copy the single-line table row and append it to `.agents/states/_ACTIVE_INDEX.md`.
*   **Result:** Chat window can be closed safely. All session state is preserved deterministically in local text files.

---

#### SECTION 5: FAILURE RISK MITIGATION & DUAL-IDE BOUNDARIES

##### 1. Context Saturation & Token Decay
*   *Risk:* Ingestion of large production datasets (CSV/PDF) degrades the reasoning capabilities of the planning model.
*   *Mitigation:* The `antigravity/` workspace enforces a hard `.geminiignore` matrix. Heavy data analysis is offloaded to the local VS Code environment sandbox running mathematical python checker files in `validators/`.

##### 2. Watcher Loop Lockout (Symmetric Exclusions)
*   *Risk:* Antigravity file writes trigger file-watcher scans in VS Code, causing terminal updates that generate more files, locking up system disk access.
*   *Mitigation:* Symmetrical exclusions are set in `.vscode/settings.json` and `.geminiignore`, isolating the state registers (`.state/` and `.agents/states/`) from live watchers.

##### 3. MUP Network Deadlocks
*   *Risk:* MUP handles lock folders during high-frequency API scans on network shares (`\\UNC_PATH`).
*   *Mitigation:* Block direct file editing loops. Force the model to generate the state files inside the local workspace first, then copy to target network nodes using path-hardened copy routines.
