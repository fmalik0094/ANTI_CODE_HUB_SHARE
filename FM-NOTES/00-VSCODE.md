# VS CODE & GPT / CODEX OPERATING MANUAL

This document consolidates all documentation, directory tree topologies, configuration files, and detailed descriptions for the **VS Code / GPT (Codex)** workspace environment.

---

## 1. Directory Tree Topology

The following tree maps the VS Code / GPT configuration layer, which organizes tools, extension settings, tasks, and state trackers in parallel to production source files.

```text
[WORKSPACE_ROOT]/
├── .codex/                          <-- Agent Layer Orchestration Parameters
│   ├── config.toml                  <-- Orchestration & Token Config
│   ├── instructions.md              <-- Agent-Specific Workspace Guidelines
│   ├── agents/                      <-- Specialist Agent Profiles
│   │   ├── code_reviewer.toml
│   │   ├── test_runner.toml
│   │   ├── documentation_writer.toml
│   │   └── security_auditor.toml
│   └── skills/                      <-- Reusable System Knowledge Bases
│       ├── coding_standards.md
│       ├── validation.md
│       ├── testing.md
│       └── release_review.md
├── .vscode/                         <-- Local Editor Settings & Launch Schemes
│   ├── settings.json                <-- Excludes & Linter Control
│   ├── tasks.json                   <-- Automated Process Scripts
│   ├── extensions.json              <-- Workspace Extensions List
│   └── launch.json                  <-- Debugger Target Paths
├── .state/                          <-- Persistent Ledger of Local Deltas
│   ├── BASELINE.md                  <-- Base Project Contract
│   ├── DELTA_LOG.md                 <-- Change Log Index
│   ├── DECISIONS.md                 <-- Settled Architectural Rules
│   └── TRACE_INDEX.md               <-- Validation Output Logs
├── validators/                      <-- Deterministic Validation Check Scripts
│   ├── validate_structure.py        <-- Folder/File Ingestion Checker
│   ├── validate_config.py           <-- System Paths/Environment Checker
│   ├── validate_tests.py            <-- Local Code Test Suite
│   └── validate_release.py          <-- Release Verification Wrapper
└── AGENTS.md                        <-- Meta-Rules & Communication Contracts
```

---

## 2. Component Reference Dictionary

### 2.1. Agent Control Layer (`.codex/`)

#### `.codex/config.toml`
Configures the execution environment limits, model properties, and execution behaviors for GPT/Codex.
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

#### `.codex/instructions.md`
Contains specific codebase operational assumptions and validation rulesets that Codex must read before performing code mutations. Helps keep Codex aligned with local environment characteristics without repeating global rules.

#### `.codex/agents/`
TOML configurations specifying specialist personas loaded on-demand depending on context:
*   `code_reviewer.toml`: General standards, code formatting, style verification.
*   `test_runner.toml`: Test script executions, coverage checking, syntax validations.
*   `documentation_writer.toml`: Formatting outputs for external tools.
*   `security_auditor.toml`: Exposes structural safety and permission audits.

#### `.codex/skills/`
Procedure manuals and step-by-step checklists loaded dynamically into context during specific task types:
*   `coding_standards.md`: Rules for clean syntax, naming, and language-specific standards.
*   `validation.md`: Step-by-step verification process for file layouts and variables.
*   `testing.md`: Execution directives for regression verification and mocked data tests.
*   `release_review.md`: Checklists to block credentials leaks, check version strings, and verify package states.

---

### 2.2. IDE Control Layer (`.vscode/`)

#### `.vscode/settings.json`
Limits active workspace scopes to prevent files from being locked during high-velocity write actions and configures basic auto-formatting rules:
```json
{
    "search.exclude": {
        "**/logs": true,
        "**/temp": true,
        "**/src": true,
        "**/*.csv": true,
        "**/*.xlsm": true,
        "**/*.pptx": true
    },
    "files.watcherExclude": {
        "**/logs/**": true,
        "**/temp/**": true,
        "**/src/**": true
    },
    "editor.formatOnSave": true
}
```

#### `.vscode/tasks.json`
Declarative runners mapping automation inputs to PowerShell/terminal execution lines:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Sync Master Index",
            "type": "shell",
            "command": "powershell",
            "args": [
                "-ExecutionPolicy", "Bypass",
                "-Command", "Get-Content .agents/states/_ACTIVE_INDEX.md"
            ],
            "group": "none",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}
```

#### `.vscode/extensions.json`
Ensures all developer workstations share identical plugins, including linters, path extensions, and terminal-assisted shells.

#### `.vscode/launch.json`
Configures launch arguments, environments, and attachments for testing active Python validators under debug conditions.

---

### 2.3. State Control Layer (`.state/`)

Holds the system state directly inside the repository. This represents the local deterministic memory of the project:
*   `BASELINE.md`: Tracks core parameters, hashes, system platforms, and initial versions.
*   `DELTA_LOG.md`: Tracks turn-by-turn changes (who did what, date, changes made, resultant hashes).
*   `DECISIONS.md`: Stores locked design choices that should not be re-negotiated (e.g., specific formats or execution variables).
*   `TRACE_INDEX.md`: Maps output files, test reports, and verification check details back to the active log.

---

### 2.4. Validation Control Layer (`validators/`)

Houses local scripts run directly to mathematically and structurally check that the workspace satisfies all criteria, removing reliance on LLM reasoning for validation tasks:
*   `validate_structure.py`: Checks file existence and layout mappings.
*   `validate_config.py`: Verifies paths, permissions, and environments.
*   `validate_tests.py`: Runs local code test suites.
*   `validate_release.py`: Wrapper executing the full verification sequence before packaging.

---

### 2.5. Root Constraints: `AGENTS.md`
Enforces the same non-conversational style instructions as Antigravity, mapping the role segregation boundaries:
```markdown
# SYSTEM CORE: META-RULES & ROLE SEGREGATION
[ROLE: COGNITIVE STATE COMPILER]
*   **Operating Mandate:** This workspace acts strictly as a Local Meta-State Vault. It does not run production application binaries or compile source software. Its primary utility is to parse unstructured thought streams, compile them into deterministic State Binaries (.md), and update the Master Registry.
*   **Communication Constraint:** Strict engineer-level delivery. Concise. Zero fluff. You are barred from outputting conversational pleasantries, transitional commentary, or opening introductions (e.g., "Certainly, here is the..."). Return raw structural data maps.
*   **Formatting Guardrail:** Always utilize standard plain text and basic Markdown formatting for data matrices, numbers, and formulas to protect 100% data fidelity when copy-pasting directly into Microsoft Word, Excel, or Google Docs.
```
