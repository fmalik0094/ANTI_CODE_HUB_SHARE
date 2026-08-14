# ANTIGRAVITY TEMPLATE: OPERATIONAL USER MANUAL

This manual provides detailed system instructions, workspace configuration guides, and cross-IDE handover protocols for the Google Antigravity local state manager environment.

---

## 1. Operating Paradigm
The `antigravity/` workspace functions strictly as a stateless **Meta-State Vault**. It is designed to prevent context window fragmentation and token decay by tracking development states in structured Markdown snapshots instead of live shell environments.

---

## 2. Directory Tree Topology
The following directory tree maps the Google Antigravity local state manager structure:

```text
antigravity/
├── .gemini/                         <-- Primary Architect Core Context
│   └── GEMINI.md                    <-- Global AI Operating Parameters
├── .agents/                         <-- Shared Process Execution Managers
│   ├── rules/
│   │   └── global.md                <-- Baseline Permission Matrix (DENY > ASK > ALLOW)
│   ├── workflows/                   <-- Session Lifecycle State Control Nodes
│   │   ├── 01_genesis_prompt.md     <-- New Topic Inception Protocol
│   │   ├── 02_entry_and_propose.md  <-- Authorization Hold Protocol
│   │   └── 03_exit_and_sync.md      <-- Context Serialization Execution Block
│   └── states/                      <-- Persistent Local Knowledge Vaults
│       ├── _ACTIVE_INDEX.md         <-- Master Domain Index Ledger Matrix
│       └── [DOMAIN_NAME]_V*.md      <-- Alphanumeric State Binary Snapshot
├── .geminiignore                    <-- Token Decay Guardrail (Ingestion Filter)
└── AGENTS.md                        <-- Multi-Agent Hierarchy & Segregation Definitions
```

---

## 3. Workspace File Reference

### 3.1. Ingestion Control: `.geminiignore`
*   **Context of Usage:** Filters reasoning inputs to prevent context window saturation during high-volume calculations or indexing operations.
*   **Behavioral Matrix:**
    *   Evaluated automatically prior to compiling any session delta plan.
    *   Excludes binary files, raw database outputs (`.csv`, `.xlsx`), and local operational caches (`logs/`, `temp/`) from the model ingestion pipeline.

### 3.2. Core Ruleset: `.gemini/GEMINI.md`
*   **Context of Usage:** Standardizes the model persona inside the Antigravity IDE, forcing it to act purely as a non-conversational context compiler.
*   **Behavioral Matrix:**
    *   Strips greeting dialogue, introductory filler, and conversational prefaces from all model outputs.
    *   Enforces standard plain-text formatting for data tables to protect copy-paste data integrity.

### 3.3. Precedence Rule: `.agents/rules/global.md`
*   **Context of Usage:** Restricts local system permissions to safeguard the host OS.
*   **Behavioral Matrix:**
    *   Defines security sequence: `DENY > ASK > ALLOW`.
    *   Requires explicit operator approval for any terminal/shell invocations.

### 3.4. Division of Labor: `AGENTS.md`
*   **Context of Usage:** Maps agent roles and communication rules to eliminate permission escalation risk.
*   **Behavioral Matrix:**
    *   Specifies the system mandate for the `SYSTEM STATE MANAGER` role, configuring co-processing boundaries.

---

## 4. Session Lifecycle Workflows (Usage Guide)

### Stage 1: Genesis (Inception)
*   **Trigger:** Initiating a new topic tracking sequence.
*   **Steps:**
    1. Open a clean chat session.
    2. Load `.agents/workflows/01_genesis_prompt.md`.
    3. Paste the raw unstructured requirements below the prompt header.
    4. Save the compiled output block as `states/[DOMAIN_NAME]_V1.0.md`.

### Stage 2: Entry (Resumption & Authorization Hold)
*   **Trigger:** Resuming a previously tracked task.
*   **Steps:**
    1. Open a clean chat session.
    2. Load `.agents/workflows/02_entry_and_propose.md`.
    3. Paste the latest target state binary `[DOMAIN_NAME]_V*.md`.
    4. **Wait for Hold:** The model will output an Action Plan and halt at `[PENDING OPERATOR APPROVAL]`.
    5. Input the command `APPROVED` to unlock the editor.

### Stage 3: Exit (Serialization & Sync)
*   **Trigger:** Suspending a work session.
*   **Steps:**
    1. Load `.agents/workflows/03_exit_and_sync.md` in the active chat.
    2. Copy **Block 1** (State Binary) to overwrite the local `states/[DOMAIN_NAME]_V*.md` file (increment the version string).
    3. Copy **Block 2** (Registry Row) and append it to `.agents/states/_ACTIVE_INDEX.md`.
    4. Close the session to flush temporary memory buffers.

---

## 5. DUAL-IDE HYBRID HANDOVER (Category 3)
Because this workspace templates a co-processing system, state variables are designed to coordinate handovers between the planning layer (Antigravity) and the execution layer (VS Code).

### 5.1. Master Sync Ledger: `.agents/states/_ACTIVE_INDEX.md`
*   **Key Variables:** `[NEXT_EXECUTION_NODE]`, `[RISK_STATUS]`
*   **Cross-Platform Handover Strategy:**
    1.  **Antigravity Planning Phase (Output):** The developer plans a system modification (e.g., a database schema change). Once defined, the developer updates the index row:
        *   `NEXT_EXECUTION_NODE`: *"VS Code to execute Prisma migration script and run validators/validate_db.py"*
        *   `RISK_STATUS`: Set to highlight database integrity migration checks.
    2.  **VS Code Execution Phase (Intake):** The developer launches VS Code, reviews the active index instruction, and executes the designated script migration and testing validation task.

### 5.2. Execution Boundaries: `.codex/config.toml`
*   **Key Variables:** `[TERMINAL_ACCESS]`, `[DENY_LIST]`
*   **Dynamic Sandboxing Strategy:**
    1.  **Safe/Standard Verification Phase:**
        *   Configure: `terminal_access = "REQUEST_REVIEW"`
        *   Effect: The VS Code Codex agent must ask for operator confirmation before running any script.
    2.  **High-Risk Processing Phase:**
        *   Configure: `terminal_access = "DENIED"`
        *   Effect: The Codex agent is blocked from executing terminal operations. It must output the validation commands as raw text inside the chat pane, forcing the operator to run the commands manually inside an external, isolated sandbox environment.

