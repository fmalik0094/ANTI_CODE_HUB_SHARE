# VS CODE STATEFUL EXECUTION CORE: OPERATIONAL MANUAL & WORKFLOW TEMPLATE

This manual provides the structural definition, evolution strategies, and usage protocols for the stateful execution layer located in [vscode/](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode).

---

## 1. Directory Scaffolding & Component Role Matrix

The execution core isolates agent orchestration, IDE behaviors, and programmatic validation checks into structured layers:

```text
vscode/
├── .vscode/                         <-- IDE Control Layer
│   ├── settings.json                <-- Excludes & Linter Control
│   └── tasks.json                   <-- Automated Process Scripts
├── .codex/                          <-- Agent Control Layer
│   ├── config.toml                  <-- Orchestration & Token Limits
│   ├── instructions.md              <-- System Role & Constraints
│   └── agents/                      <-- Specialist Agent Profiles
│       └── security_auditor.toml    <-- Auditor Configuration
├── .state/                          <-- State Control Layer (Ledger)
│   ├── BASELINE_HASH.md             <-- Structural Blueprint Ground Truth
│   ├── DELTA_LOG.md                 <-- Change Log Index
│   └── DECISIONS.md                 <-- Settled Architectural Rules
├── validators/                      <-- Validation Control Layer
│   ├── validate_structure.py        <-- Structure Integrity Checks
│   └── validate_config.py           <-- Configuration Integrity Checks
└── src/                             <-- Source Code Directory
```

---

## 2. Stateful Execution Core Components & Evolution Strategies

The components in the execution core shift and tighten as the codebase moves from initialization to release-candidate status.

### 2.1. Local Codebase Rules (`.codex/instructions.md`)
*   **Purpose:** Configures syntax, standards, and rules applied directly by the agent during code mutations.
*   **Variable Shift:** `[FORMATTING_STANDARDS]`, `[LINTING_RULES]`
*   **Evolution Strategy (Constraint Tightening):**
    *   *Early Development:* Kept minimal or empty to allow the model to draft structures freely and execute rapid prototyping.
    *   *Late Development:* Appended with strict constraints to prevent type leaks and styling drift. E.g., *"Never use 'any' in TypeScript. All React components must use forwardRef. Append custom logging to all try/catch blocks."*

### 2.2. Specialist Profiles (`.codex/agents/security_auditor.toml`)
*   **Purpose:** Configures agent persona parameters, instructions, and tools allowed within sandboxed runs.
*   **Variable Shift:** `[SYSTEM_PROMPT]`, `[ALLOWED_TOOLS]`
*   **Evolution Strategy (Targeted Delegation):**
    *   As security surface areas grow, the operator creates domain-specific auditing agents. E.g., if a payment gateway is integrated, the operator creates a `payment_auditor.toml` specialist agent, defining a system prompt to check strictly for Stripe/API secret leakage and restricting its tools to read-only regex scans.

### 2.3. Deterministic Testing Logic (`validators/*.py`)
*   **Purpose:** Local, non-AI Python checks to mathematically guarantee code properties.
*   **Variable Shift:** `[ASSERTION_LOGIC]`, `[MOCK_PAYLOADS]`
*   **Evolution Strategy (Validation Maturation):**
    *   *Sprint 1:* Basic validation. `validate_structure.py` asserts that critical files like `app.js` and `db.js` simply exist on disk.
    *   *Sprint 3:* AST (Abstract Syntax Tree) validation. The validator programmatically parses the AST of the generated code to assert that specific security middleware is wrapped around every routing handler before the VS Code task allows a git commit.

### 2.4. Micro-Turn Ledger (`.state/DELTA_LOG.md`)
*   **Purpose:** Records incremental change transactions.
*   **Variable Shift:** `[FILE_HASHES]`, `[CHANGE_DESCRIPTIONS]`
*   **Evolution Strategy (Traceability):**
    *   Appended mechanically at the end of every active execution. The delta log must log precise timestamps, files modified, changes made, and resulting file hashes. E.g., `[2026-05-29] Agent modified src/auth.py - updated bcrypt hashing rounds from 10 to 12. Hash: 8f4e2a.`

---

## 3. Operational Walkthrough Simulation: Domain `DATA_PROCESSOR`

The lifecycle of implementing a new feature is tracked through the following stateful steps:

### Stage 1: Reading Baseline Ground Truth
The execution agent checks [.state/BASELINE_HASH.md](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.state/BASELINE_HASH.md) to align with the core directory structures.

### Stage 2: Evaluating Run Restrictions
The agent parses [.codex/config.toml](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.codex/config.toml) to enforce limits (e.g. `max_context_tokens = 1048576`) and execution blocklists (`rm`, `sudo`, `curl`).

### Stage 3: Feature Generation
Code is written to `src/processor.py`. The files generated are excluded from watcher cycles via [.vscode/settings.json](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.vscode/settings.json) to preserve system memory.

### Stage 4: Triggering Verification Tasks
The developer runs target validation tasks in [.vscode/tasks.json](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.vscode/tasks.json). Python validator scripts run programmatically to ensure structure and variables match expectations.

### Stage 5: Serialization
Once checks return exit code `0`, the delta is logged to [.state/DELTA_LOG.md](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.state/DELTA_LOG.md) and design rules are locked in [.state/DECISIONS.md](file:///C:/01_LOCAL_CODING_F.M/00-TEST-ONLY/ANTI_CODE-HUB/vscode/.state/DECISIONS.md).
