# ANTI-CODE HUB: DUAL-IDE HYBRID ORCHESTRATION PROTOCOL

This document defines the unified, cross-platform workspace topology and operational protocols enabling Google Antigravity (Gemini) and VS Code (GPT/Codex) to run concurrently in the exact same workspace directory without logic collisions, data races, or token bloat.

---

## 1. Unified Directory Topology: ANTI-CODE HUB

The directory structure below details the integration points of both platforms, isolating IDE-specific control panels while sharing the centralized source code, states, and rule engines.

```text
TOPIC-WORK SPACE_F.M/
├── .vscode/                         <-- VS Code Environment Controls
│   ├── settings.json                <-- Exclude watch lists to stop disk thrashing
│   └── tasks.json                   <-- Command shortcuts for index syncing
├── .gemini/                         <-- Antigravity Native Rules Area
│   └── GEMINI.md                    <-- Core LLM behavioral parameters
├── .codex/                          <-- VS Code Agent Parameter Space
│   └── config.toml                  <-- Model thresholds and command exclusions
├── .agents/                         <-- SHARED PROCESS EXECUTION MANAGERS (Antigravity)
│   ├── rules/
│   │   └── global.md                <-- Baseline Permission Matrix (DENY > ASK > ALLOW)
│   ├── workflows/                   <-- State Control Node Protocols
│   │   ├── 01_genesis_prompt.md     <-- Genesis Compiler Node
│   │   ├── 02_entry_and_propose.md  <-- Entry Hold & Plan Approval Node
│   │   └── 03_exit_and_sync.md      <-- Session State Serialization Daemon
│   └── states/                      <-- Local Alphanumeric State Vaults
│       ├── _ACTIVE_INDEX.md         <-- Master Tracking Registry Ledger
│       └── [DOMAIN]_V*.md           <-- Compressed Session Snapshots
├── .state/                          <-- Persistent Ledger of Local Deltas (VS Code)
│   ├── BASELINE.md                  <-- Base Project Contract
│   ├── DELTA_LOG.md                 <-- Change Log Index
│   ├── DECISIONS.md                 <-- Settled Architectural Rules
│   └── TRACE_INDEX.md               <-- Validation Output Logs
├── validators/                      <-- Deterministic Validation Check Scripts
│   ├── validate_structure.py
│   ├── validate_config.py
│   ├── validate_tests.py
│   └── validate_release.py
├── .geminiignore                    <-- Exclusion Matrix for Antigravity Architect
├── .aiexclude                       <-- Root-level MCP Hard-Blocklist
├── .gitignore                       <-- Version Control Exclusion List
├── AGENTS.md                        <-- VS Code Agent behavioral rules
└── GEMINI.md                        <-- Antigravity Adapter Entrypoint Rules
```

---

## 2. Dual-IDE Synchronization Configuration

To prevent background file-watchers from racing, locking files on disk, or exhausting API tokens with infinite loops, the exclusion matrices must be configured symmetrically.

### 2.1. File Watcher Exclusions
Large output datasets, binary files, and active logs are locked out of search loops:

#### VS Code Settings (`.vscode/settings.json`)
```json
{
    "search.exclude": {
        "**/logs": true,
        "**/temp": true,
        "**/*.csv": true,
        "**/*.xlsm": true,
        "**/*.pdf": true,
        "**/.agents/states": true
    },
    "files.watcherExclude": {
        "**/logs/**": true,
        "**/temp/**": true,
        "**/.agents/states/**": true
    },
    "editor.formatOnSave": true
}
```

#### Antigravity Exclusions (`.geminiignore`)
```text
# EXCLUSION MATRIX: ANTIGRAVITY CONTEXT PROTECTION
logs/
temp/
*.csv
*.xlsm
*.pdf
.agents/states/
.vscode/
.codex/
```

### 2.2. Security Isolations

#### MCP File-System Blocklist (`.aiexclude`)
Functions as a hard security boundary. If a file path matches, the Model Context Protocol (MCP) server blocks reading at the file-system layer.
```text
# CRITICAL SOURCE BLOCKLIST FOR FRONT-END MODELS
**/*.secret
**/*.key
credentials/
```

---

## 3. Model Context Protocol (MCP) Cross-Platform Bridge

Both the VS Code sub-agents and the Antigravity Terminal/Browser execution loops share a local, credential-isolated pipeline via the Model Context Protocol (MCP).

```text
       [Google Antigravity IDE]              [VS Code + Codex Layer]
          (Pro/Flash Architecture)              (Task Runners/Extensions)
                     │                                     │
                     └───────────────────┬─────────────────┘
                                         ▼
                     [Model Context Protocol (MCP) Engine]
                                         │
                 ┌───────────────────────┼───────────────────────┐
                 ▼                       ▼                       ▼
     [Local Terminal Sub-Agent]  [File System Validator]  [External Tool Registry]
     - OS Command Line execution  - Type-safe schema check - Secure API handshakes
     - Shell script loops         - CSV validation via Python  - OAuth & Secret Vaults
```

### Operational MCP Policies
*   **Credential Isolation:** High-security variables (OAuth keys, passwords) are never committed to workspace configurations. They reside in local environment variables and are read strictly on-demand by the terminal runtime environment.
*   **Write Permission Isolation:** The MCP Server layer defaults to read-only. Any modification to system-critical states requires explicit user validation (`APPROVED`) via the **Authorization Hold Engine** before line-level edits occur.

---

## 4. Co-Processing State Protocol (The Workflow Loop)

When running both IDEs in parallel, the operator uses this workflow loop to prevent version branch divergence and maintain absolute disk state consistency:

```text
[1. GENESIS] ───> [2. RUN DUAL-IDE WORKSPACE] ───> [3. STATE LOCK & EXIT]
                     │  - Antigravity handles high-level  │  - Paste Exit Prompt to active chat.
                     │    Architect Planning tasks.       │  - Serializes current Delta state.
                     │  - VS Code tasks execute terminal  │  - Generates Registry table row.
                     │    and python automation code.     │
                     └────────────────<───────────────────┘
                       (New Session inherits clean token 
                        memory using state_vX.md file)
```

1.  **The Genesis Event:** Compile raw requirements into a structured tracking plan utilizing the `.agents/workflows/01_genesis_prompt.md` compiler. Save the resultant block as `states/[DOMAIN]_V1.0.md` inside your local drive structure.
2.  **The Dual-IDE Iteration:** 
    *   Keep **Antigravity open** on one monitor to guide architectural structure, using Gemini Pro as the high-level Architect and Flash for modular details.
    *   Keep **VS Code open** on another monitor to run local terminal commands, execute Python scripts, and process numeric checks.
    *   Both editors operate out of the same workspace folders safely due to strict mutual exclusions in `.geminiignore` and `.vscode/settings.json`.
3.  **The Exit & Sync Daemon:** Prior to closing the session, paste the contents of `.agents/workflows/03_exit_and_sync.md` into the active chat. Overwrite the local `states/[DOMAIN]_V*.md` snapshot file with the generated **Block 1**, and append the **Block 2** row to `.agents/states/_ACTIVE_INDEX.md`.

---

## 5. Failure Modes & Risks Avoided

*   **Watcher State Racing:** Occurs when parallel background file scanners watch the same files, causing infinite loop writes. Handled by matching `.geminiignore` boundaries to VS Code file exclusions.
*   **Token Saturation Contamination:** Occurs when heavy data assets (such as historical financial matrices or database dumps) fill up the context window. Keeping these prunings isolated forces both LLMs to read from type-safe structural configurations or schemas instead of raw binary data.
