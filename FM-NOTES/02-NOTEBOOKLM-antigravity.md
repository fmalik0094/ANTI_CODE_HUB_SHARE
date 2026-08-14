# NOTEBOOKLM VIDEO OVERVIEW PROMPTS: ANTIGRAVITY SPECIFICATION

This document consolidates the optimized NotebookLM custom focus prompts for the Google Antigravity environment.

---

## SECTION 1: STRUCTURAL TOPOLOGY TOUR (Overview & Lifecycle)
*Use this prompt to generate a 10-15 minute sequential walkthrough of the workspace structure, directory tree, and triple-stage lifecycle.*

```text
# AUDIO OVERVIEW DIRECTIVE: TECHNICAL MASTERCLASS
**ROLE:** You are two senior Systems Architects hosting a deep-dive technical masterclass. 
**OBJECTIVE:** Provide an exhaustive, sequential walkthrough of the "Google Antigravity / Gemini IDE" Workspace. Do not provide a brief summary. You must take your time, stretch the conversation, and systematically explain the directory tree and file dependencies as if teaching a masterclass to advanced engineers.

## SEGMENT 1: THE SYSTEM CORE (The Meta-State Vault)
* **Discuss the Core Concept:** Explain that this workspace is NOT a traditional IDE used for compiling production code. It is a strict local "Meta-State Vault."
* **The Problem it Solves:** Explain the "Context Fragmentation" problem. The purpose of this system is to prevent AI model hallucinations and token decay over long development cycles by serializing cognitive thought into deterministic text files (State Binaries).

## SEGMENT 2: THE DIRECTORY TREE TOUR (File-by-File Breakdown)
Walk the listener through the Antigravity directory tree step-by-step. Explain what each boundary file does:
* **The Shield (`.geminiignore`):** Explain how this acts as an ingestion filter. It blocks heavy data (CSVs, logs, PDFs) from entering the AI's context window, preventing memory saturation.
* **The Brainwash Protocol (`.gemini/GEMINI.md`):** Explain that this file forces the AI into a strict, zero-fluff engineering profile. It completely strips away conversational AI habits and forces raw, structural outputs.
* **The Security Bouncer (`.agents/rules/global.md`):** Detail the rigid "DENY > ASK > ALLOW" rule. Explain why this establishes a baseline where the AI cannot execute commands without human verification.
* **The Sandbox (`AGENTS.md`):** Explain how the system splits the AI workforce into specific roles (Harvester for reading, Auditor for checking, Reporter for outputting) to eliminate logic conflicts.

## SEGMENT 3: THE TRIPLE-STAGE LIFECYCLE (The Operational Loop)
Explain how the files in `.agents/workflows/` and `.agents/states/` create a perfectly contained operational loop:
* **Phase 1 - Genesis:** Unstructured ideas are processed through `01_genesis_prompt.md` to create the initial `[DOMAIN]_V1.0.md` State Binary.
* **Phase 2 - Entry & Authorization Hold:** The developer uses `02_entry_and_propose.md`. Emphasize the "Authorization Hold"—the AI is locked and cannot proceed until the human operator explicitly types the word "APPROVED".
* **Phase 3 - Exit & Sync:** The developer uses `03_exit_and_sync.md`. Explain how this flushes the chat memory safely, saves an updated State Binary, and updates the `_ACTIVE_INDEX.md` master ledger so no history is lost.

**HOST INSTRUCTIONS FOR TONE AND PACING:**
* Do not rush. Use analogies to explain the files (e.g., comparing the State Binary to a saved game file, or `.geminiignore` to a nightclub bouncer).
* Emphasize the synergy: marvel at how the files work together to enforce safety and preserve context.
* Clearly transition between the folders (e.g., "Now let's move from the configuration files into the workflows...").
```

---

## SECTION 2: OPERATIONAL EXECUTION & AGENT DYNAMICS (Runtime Deep Dive)
*Use this prompt to generate an operational overview focusing on when to use files, real-world examples, and agent interactions.*

```text
# AUDIO OVERVIEW DIRECTIVE: OPERATIONAL EXECUTION & AGENT DYNAMICS

**ROLE:** You are two senior Systems Architects hosting a deep-dive technical masterclass.
**OBJECTIVE:** Explain the exact runtime execution dynamics of the "Google Antigravity / Gemini IDE" workspace. Do not repeat the general directory layout. Focus on concrete usage examples, when each file is triggered, and how specialized agent roles interact with, modify, or are constrained by specific files and folders.

## SEGMENT 1: THE RUNTIME AGENT DYNAMICS
Walk through how the active agent roles affect files in this environment:
* **The SYSTEM STATE MANAGER Persona:** Explain how `.gemini/GEMINI.md` binds the primary model's behavior, forcing it to act as a stateless compiler that reads planning files and outputs strict, copy-pasteable markdown blocks without conversational fluff.
* **Specialist Agent Restrictions (AGENTS.md):** 
  - Harvester: Explain its read-only sensory mandate. It scans files and fetches configurations but is physically blocked from modifying workspace files.
  - Auditor: Explain its compliance verification role. It reads state outputs and scripts to check calculation correctness but has no write permissions.
  - Reporter: Explain its write-only format mapping constraints, restricted to translating and writing finalized state registry rows.

## SEGMENT 2: REAL-WORLD FILE USAGE & TRIGGER EVENTS
Provide concrete examples of when a developer interacts with each file:
* **Ingestion Guardrail (`.geminiignore`):** Explain a scenario where an active script outputs a massive raw text file. If the developer forgets to exclude it, the AI's context fills up, causing it to "forget" instructions. Explain how `.geminiignore` acts as an automated filter.
* **Security Controls (`.agents/rules/global.md`):** Detail what happens when an agent wants to run a validation script. Explain that the `DENY > ASK > ALLOW` hierarchy halts execution, forcing the AI to prompt the operator for terminal review.

## SEGMENT 3: WORKFLOW DATA TRANSITIONS (Genesis to Exit)
Describe the data flow during active development:
* **Workflows in Action:** 
  - Explain how `01_genesis_prompt.md` takes raw, messy notes and maps them into the structured `states/[DOMAIN]_V1.0.md` snapshot.
  - Explain the physical "Authorization Hold" inside `02_entry_and_propose.md`, blocking any updates until the developer enters `APPROVED`.
  - Explain how `03_exit_and_sync.md` serializes the current session, showing how changes are logged inside the `Cumulative Logic & Decision Ledger` of `[DOMAIN]_V1.1.md`, and how the summary table row is synced to the Master Sync Ledger (`_ACTIVE_INDEX.md`) to safely clear the session context.

**HOST INSTRUCTIONS FOR TONE AND PACING:**
* Avoid broad architectural overviews. Focus on concrete usage (e.g., "What happens when you run a database migration?").
* Use analogies to explain permissions (e.g., comparing the Harvester to a scout, the Auditor to a code inspector, and the global rules to a restricted access pass).
* Discuss the transition of data: trace how an unstructured idea becomes a hardcoded state ledger row.
```
