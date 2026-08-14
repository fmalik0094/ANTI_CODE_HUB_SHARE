# ANTIGRAVITY & GEMINI IDE OPERATING MANUAL

This document consolidates all documentation, directory tree topologies, configuration files, workflows, and operational manuals for the **Google Antigravity / Gemini IDE** workspace environment.

---

## 1. Directory Tree Topology

The following structure represents the native Antigravity environment directory topology. All functional system scripts reside in `src/`, while the configuration files function as hard boundary surfaces.

```text
[WORKSPACE_ROOT]/
├── .gemini/                         <-- Primary Architect Core Context
│   └── GEMINI.md                    <-- Global AI Operating Parameters
├── .agents/                         <-- Shared Process Execution Managers
│   ├── rules/
│   │   └── global.md                <-- Baseline Permission Matrix (DENY > ASK > ALLOW)
│   ├── skills/                      <-- On-Demand Knowledge / Capability Packages
│   │   └── base-validator/          <-- Modular Capability Sandbox
│   │       ├── SKILL.md             <-- Trigger Keywords & Priority Weighting
│   │       └── scripts/
│   │           └── validate_data.py <-- Hardcoded Syntactical Testing Script
│   ├── workflows/                   <-- Session Lifecycle State Control Nodes
│   │   ├── 01_genesis_prompt.md     <-- New Topic Inception Protocol
│   │   ├── 02_entry_and_propose.md  <-- Authorization Hold Protocol
│   │   └── 03_exit_and_sync.md      <-- Context Serialization Execution Block
│   └── states/                      <-- Persistent Local Knowledge Vaults
│       ├── _ACTIVE_INDEX.md         <-- Master Domain Index Ledger Matrix
│       └── [DOMAIN_NAME]_V1.0.md    <-- Alphanumeric State Binary Snapshot
├── .geminiignore                    <-- Token Decay Guardrail (Ingestion Filter)
└── AGENTS.md                        <-- Multi-Agent Hierarchy & Segregation Definitions
```

---

## 2. Core Configuration Files & Rulesets

### 2.1. Ingestion Control: `.geminiignore`
*   **Function:** Declares the rigid token exclusion matrix for the Primary Architect agent.
*   **Purpose:** Prevents context window saturation. When heavy analytical processing loops generate expansive log data or flat CSV files, this file instructs the language server to drop these extensions entirely from active memory.
*   **Execution Mechanic:** Evaluated prior to the compilation of any task plan. If a path matches, its binary stream is pruned from the token compilation step.

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

---

### 2.2. Workspace Meta-Rules: `.gemini/GEMINI.md`
*   **Function:** Establishes the core meta-rules and non-conversational behavior parameters for the Antigravity environment.
*   **Purpose:** Disables stochastic conversational fluff. It forces the frontier reasoning engine to act purely as a stateless technical logic compiler.
*   **Execution Mechanic:** Automatically pre-pended as an immutable `[SYSTEM INSTRUCTION]` envelope to all workspace inquiries, anchoring the engine's temperature profiles and behavioral boundaries.

```markdown
# SYSTEM CORE: META-RULES & SAFETY CONTROLS
[ROLE: SYSTEM STATE MANAGER]
*   **Operating Mandate:** This workspace functions exclusively as a Meta-State Vault. It does not execute application code or compile production software. Its sole function is to process unstructured cognitive inputs, serialize cumulative logic into deterministic State Binaries (.md), and update the Master Registry.
*   **Response Style:** Strict engineer-level language. Concise. Zero fluff. You are completely barred from using conversational greetings, transitional pleasantries, or introductory sentences. Do not use phrases like "Based on your context" or "Since you are an architect". Deliver raw, structural outputs.
*   **Formatting Guardrail:** Always use standard plain text and basic Markdown for numbers and formulas to guarantee 100% data fidelity when copy-pasting directly into Microsoft Word, Excel, or Google Docs.
```

---

### 2.3. Permission Precedence: `.agents/rules/global.md`
*   **Function:** Specifies system-wide security, authorization, and permission logic.
*   **Purpose:** Enforces the baseline rule sequence `DENY > ASK > ALLOW`. This ensures that any automation task or model workflow trying to run terminal scripts must check this baseline first, stopping unauthorized actions unless explicitly approved by the operator.
*   **Execution Mechanic:** Consulted automatically prior to executing commands via local sub-agents.

```markdown
# GLOBAL PRECEDENCE CONSTRAINTS
*   **Rule Hierarchy:** Absolute constraint resolution: DENY > ASK > ALLOW. Workspace configurations or local scripts can only restrict, never expand, this safety baseline.
*   **Implicit Policies:** Write access implies Read access. Deny Read access immediately enforces Deny Write access.
*   **Terminal Execution:** Policy set to REQUEST REVIEW. Unvetted terminal commands are explicitly blocked.
```

---

### 2.4. Agent Roles & Boundaries: `AGENTS.md`
*   **Function:** Defines the multi-agent organizational hierarchy and role boundaries.
*   **Purpose:** Eliminates race conditions and logic contamination. It specifies the rigid boundaries between distinct operational node classes.
*   **Execution Mechanic:** Read during multi-agent instantiation loops.

```markdown
# MULTI-AGENT SEGREGATION FRAMEWORK
[ROLE: SYSTEM STATE MANAGER]
*   **Operating Mandate:** This workspace functions as a co-processing state manager. Google Antigravity acts as the high-level planning architect, and VS Code acts as the shell execution layer.
*   **Response Style:** Strict, non-conversational, engineer-level language. Concise. Deliver raw, structural outputs.
```

---

## 3. Session Lifecycle Workflows

### 3.1. Genesis Workflow (Inception)
*   **File:** `.agents/workflows/01_genesis_prompt.md`
*   **Purpose:** Compiles raw, unstructured engineering requirements into structured project plans.
*   **Execution:** Executed in a clean, stateless chat session with the unstructured idea pasted below the prompt header. Save the output to `states/[DOMAIN_NAME]_V1.0.md`.

```markdown
# COMMAND: INITIATE PROJECT GENESIS
# ENGINE: DETERMINISTIC_ARCHITECTURE_COMPILER
## DIRECTIVE
Process the raw unstructured objective injected below. Map the structural parameters utilizing raw logic. Do not output conversational brainstorming. Immediately compile the mapping into a V1 State Binary block.
## UNSTRUCTURED OBJECTIVE
[INSERT UNSTRUCTURED IDEAS OR TOPIC DATA HERE]
## COMPILATION SCHEMA
Output strictly as a single Markdown code block containing:
1. **STATE HASH / DOMAIN:** [V1.0 - Domain ID]
2. **GLOBAL OBJECTIVE:** [Immutable core goal]
3. **ARCHITECTURE & ENVIRONMENT:** [Tech Stack, constraints, dependencies]
4. **ACTIVE CONSTRAINTS:** [Operational thresholds, ruleset boundaries]
5. **FAILURE MODES & RISKS:** [Bottlenecks, token decay traps]
6. **NEXT EXECUTION NODE:** [The literal text prompt to initiate the next session]
```

---

### 3.2. Entry Workflow (Resumption & Hold)
*   **File:** `.agents/workflows/02_entry_and_propose.md`
*   **Purpose:** Enforces a physical human-in-the-loop authorization check (`[PENDING OPERATOR APPROVAL]`), halting all code execution until explicit approval is confirmed.
*   **Execution:** Paste the workflow template along with the latest state binary. The agent generates a bulleted Action Plan and waits for the command `APPROVED`.

```markdown
# COMMAND: INJECT STATE & PROPOSE ACTION
# ROLE: DETERMINISTIC SYSTEMS ARCHITECT
## DIRECTIVE
Initialize the active reasoning engine based strictly on the compiled state binary injected below. Acknowledge context silently.
**AUTHORIZATION HOLD:** Do NOT execute the Next Execution Node automatically. Analyze the current state and output a strict, bulleted Action Plan. Append `[PENDING OPERATOR APPROVAL]` at the bottom. Await the explicit user command "APPROVED" before mutating the workspace or running commands.
## INJECTED STATE BINARY
[PASTE THE STATE BINARY FROM THE MOST RECENT SESSION SNAPSHOT HERE]
```

---

### 3.3. Exit Workflow (Serialization & Sync)
*   **File:** `.agents/workflows/03_exit_and_sync.md`
*   **Purpose:** Serializes the current session delta into an updated state binary and generates a metadata row to append to the master ledger index.
*   **Execution:** Paste the template into the active chat window to generate the two outputs. Copy Block 1 to overwrite `states/[DOMAIN_NAME]_V*.md` and copy Block 2 to append to `_ACTIVE_INDEX.md`.

```markdown
# COMMAND: INITIATE FULL STATE SERIALIZATION & INDEX SYNC
# ENGINE: DETERMINISTIC_CONTEXT_SERIALIZATION
## DIRECTIVE
Execute an immediate hard stop on active session trajectories. Output exactly TWO distinct Markdown code blocks: Block 1 (State Binary) and Block 2 (Registry Row). No other text.
## BLOCK 1: THE STATE BINARY
Compile the cumulative project timeline and architecture into a single copy-pasteable Markdown block:
1. **STATE HASH / DOMAIN:** [Increment current version number]
2. **GLOBAL OBJECTIVE:** [Immutable core goal]
3. **CUMULATIVE LOGIC & DECISION LEDGER:** [Aggregated list of all architectural decisions]
4. **CURRENT SESSION DELTA:** [Strict list of files changed and logic verified during this turn]
5. **ACTIVE CONSTRAINTS:** [Current boundaries and environment constraints]
6. **FAILURE MODES & RISKS:** [Unresolved edge cases or system discrepancies]
7. **NEXT EXECUTION NODE:** [The literal prompt text to resume the pipeline next session]
## BLOCK 2: THE REGISTRY ROW
Output a single Markdown table row:
| [Domain Name] | [Version] | [Current System Date/Time] | [Next Node Summary] | [Highest Priority Failure Mode] |
```


---

## 4. State Management Registers

### 4.1. The Master Ledger: `.agents/states/_ACTIVE_INDEX.md`
Functions as the primary catalog, organizing Domain Names, Version Statuses, Last Modified Timestamps, and Failure Mode status flags.

```markdown
# TOPIC-HUB-ENGINE: MASTER REGISTRY
| DOMAIN / TOPIC | CURRENT VERSION | LAST MODIFIED | NEXT EXECUTION NODE | RISK STATUS |
| :--- | :--- | :--- | :--- | :--- |
```

---

### 4.2. Operational Field Manual: `.agents/states/README_GUIDE.md`

```markdown
# TOPIC-HUB-ENGINE V2.0: SYSTEM FIELD MANUAL
## TRIPLE-STAGE EXECUTION LOOP
**1. GENESIS (New Topic Inception)**
   * Open clean, stateless chat window.
   * Paste the contents of `.agents/workflows/01_genesis_prompt.md` + your unstructured idea payload.
   * Save the raw code block output to a file named `states/[DOMAIN_NAME]_V1.0.md`.
**2. ENTRY & AUTHORIZATION (Session Resumption)**
   * Open clean, stateless chat window.
   * Paste the contents of `.agents/workflows/02_entry_and_propose.md` + the text of your latest `states/[DOMAIN_NAME]_V*.md` binary file.
   * Review the AI's generated Action Plan. Reply "APPROVED" to release the authorization hold and begin production.
**3. EXIT & INDEX SYNC (Session Suspension & Cache Flush)**
   * Paste the contents of `.agents/workflows/03_exit_and_sync.md` into the active session.
   * Copy **Block 1** and save it as an absolute overwrite to your local `states/[DOMAIN_NAME]_V*.md` file (increment the version string in the filename).
   * Copy **Block 2** (the single table row) and append it to the bottom of the master registry array inside `.agents/states/_ACTIVE_INDEX.md`.
   * Close the chat window. Token memory is safely flushed.
```
