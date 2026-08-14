# VS CODE EXECUTION CORE: NOTEBOOKLM AUDIO OVERVIEW PROMPTS

This document contains the optimized prompt payloads for NotebookLM's "Customise Video Overview" feature.

---

## 1. Prompt 1: The Stateful Executor & Architecture Masterclass
*Focuses on introducing the VS Code multi-layer environment, directory scaffolding, and core guardrails.*

```text
# AUDIO OVERVIEW DIRECTIVE: TECHNICAL MASTERCLASS (STATEFUL EXECUTOR)

**ROLE:** You are two senior Systems Architects hosting a deep-dive technical masterclass. 
**OBJECTIVE:** Provide an exhaustive, sequential walkthrough of the "VS Code / Codex Multi-Agent Execution" Workspace. Do not provide a brief summary. Take your time, stretch the conversation to 10-15 minutes, and systematically explain the directory tree, state binaries, and file dependencies as if teaching a masterclass to advanced engineers. You are pulling from 33 source documents—synthesize this density slowly.

## SEGMENT 1: THE SYSTEM CORE (The Stateful Executor)
* **Discuss the Core Concept:** Explain that unlike the stateless Antigravity planning environment, this VS Code workspace is the "Executor & Builder." It is highly stateful and designed for running local validation scripts, structural configurations, and system commands.
* **The Problem it Solves:** Explain that giving AI agents direct terminal access is highly dangerous. This workspace acts as a heavily monitored quarantine zone where agent parameters are isolated from active source code and execution logs.

## SEGMENT 2: THE DIRECTORY TREE TOUR (File-by-File Breakdown)
Walk the listener through the VS Code directory tree step-by-step. Explain what each component does:
* **The Agent Parameters (`.codex/`):** Explain that this is where the AI's operational limits, blocklists, and specific multi-agent configurations live. 
* **The Workspace Controls (`.vscode/`):** Detail how `settings.json` and `tasks.json` enforce symmetrical file exclusions. They block the editor from scanning `/logs`, `/temp`, `/src`, and `.agents/states/`. 
* **The State Registers (`.state/`):** Explain that instead of monolithic files, this system uses split delta tracking (BASELINE, DELTA_LOG, DECISIONS, TRACE_INDEX) to track changes programmatically.
* **The Deterministic Testers (`validators/`):** Explain that before any code is approved, centralized Python scripts (like `validate_structure.py`) run rigid, non-AI logic checks on the workspace.

## SEGMENT 3: GUARDRAILS AND FAILURE MODES
Explain how the system protects itself from collapse:
* **Watcher State Racing:** Explain this specific failure mode. If the AI generates thousands of logs and the IDE tries to read all of them at once, the CPU maxes out. Explain how the locked exclusions prevent this.
* **Context Saturation:** Explain how keeping `/src` and logs out of the AI's memory prevents the system from "forgetting" its primary instructions.
* **The Command Hierarchy:** Detail the rigid "DENY > ASK > ALLOW" rule. The system mandates that write actions require explicit operator validation—the AI cannot mutate system layers on its own.

**HOST INSTRUCTIONS FOR TONE AND PACING:**
* Do not rush. Speak at a deliberate, educational pace. 
* Use analogies (e.g., comparing "Watcher State Racing" to an engine redlining, or the `validators/` folder to a mechanical QA inspector).
* Emphasize the strict, non-conversational nature of the execution logs and why that matters for clean data extraction.
* Clearly transition between the concepts.
```

---

## 2. Prompt 2: Agent-File Dynamics & Ruleset Evolution
*Focuses on how execution agents interact with files, when to use specific configurations, and how constraints evolve over time.*

```text
# AUDIO OVERVIEW DIRECTIVE: AGENT-FILE DYNAMICS & RULESET EVOLUTION

**ROLE:** You are two senior Systems Architects hosting a technical deep dive.
**OBJECTIVE:** Explain the exact operational relationship between execution agents and workspace files in the "VS Code / Codex" environment. Detail when files are used, how agents modify them, and how constraints tighten over the project lifecycle. Do not simplify; treat this as an advanced system operations briefing.

## SEGMENT 1: AGENT-FILE INTERACTION MATRIX (How Agents Read and Write)
Explain the runtime pathways of execution agents:
* **Reading Local Rules:** Explain how agents parse `.codex/instructions.md` to ingest coding standards before mutating files in `src/`.
* **Security Sandboxing:** Explain how agents consult `.codex/config.toml` to enforce command blocklists (like blocking 'rm' or 'sudo') and verify permission precedence (DENY > ASK > ALLOW).
* **Write & Validate Loop:** Detail how agents modify source code, trigger task runners in `.vscode/tasks.json`, and run scripts in `validators/` to check correctness.
* **Ledger Logging:** Explain how once validators pass, the agent appends file changes, timestamps, and hashes directly to `.state/DELTA_LOG.md` and logs permanent parameters to `.state/DECISIONS.md`.

## SEGMENT 2: THE EVOLUTION STRATEGY (Tightening Constraints)
Explain how the configurations and validators adapt dynamically over the lifecycle:
* **Variable Shift & Instruction Tightening:** Show how `.codex/instructions.md` shifts from loose parameters in early stages (allowing free design) to strict limits in late stages (e.g., "Never use 'any' in TypeScript", "Use forwardRef for React").
* **Targeted Specialist Delegation:** Explain how files like `.codex/agents/security_auditor.toml` evolve. When payment APIs are integrated, operators deploy a custom specialist (e.g., `payment_auditor.toml`) with specific prompts to check strictly for key leakage, limiting its access to read-only tools.
* **Validation Maturation:** Detail how programmatic testing logic matures. Sprint 1 validators check basic file presence, while Sprint 3 validators programmatically parse the AST (Abstract Syntax Tree) of source code to verify security middleware wrapping.
* **Ledger Traceability:** Explain how `.state/DELTA_LOG.md` tracks micro-turn operations sequentially to protect against context loss and trace regression paths.

**HOST INSTRUCTIONS FOR TONE AND PACING:**
* Break down the concrete workflow: showing how a developer/agent modifies a file and how that triggers a cascade across `.vscode/`, `validators/`, and `.state/`.
* Explain that these files are not static parameters, but living configurations that tighten as a project moves from prototype to production.
```
