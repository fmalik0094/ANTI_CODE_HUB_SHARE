# AGENTS & GOVERNANCE MATRIX

Three permanent leads — one per engine — plus one parametric slot per engine
that this project defines for itself.

## Permanent leads (inherited from the hub — do not edit)

| Agent ID | Engine | Primary Specialization | Authority Layer |
| :--- | :--- | :--- | :--- |
| **GEM-01** | Google Antigravity (Gemini) | Macro-Planning, Architecture, Topology | Planning Lead |
| **CDX-01** | VS Code / Codex (OpenAI) | Scaffolding, Diffs, Terminal Execution, Git Ops | Execution Lead |
| **CLD-01** | Claude Code (Anthropic) | Deep Refactoring, Correctness Review, QA Validation | Verification Lead |

A session claims **one** identity — never two at once.

## Parametric slots (define these for this project)

Fill in a specialization **and** an activation condition before claiming a
slot. An undefined slot is simply unused — leave it that way rather than
inventing a role for it.

| Slot | Engine | Specialization | Activates when |
| :--- | :--- | :--- | :--- |
| `GEM-02` | Google Antigravity (Gemini) | *(undefined)* | *(undefined)* |
| `CDX-02` | VS Code / Codex (OpenAI) | *(undefined)* | *(undefined)* |
| `CLD-02` | Claude Code (Anthropic) | *(undefined)* | *(undefined)* |

**Example** of a filled slot, from a financial-analysis project — note the
specialization and the activation condition are both concrete:

> **Slot:** CLD-02 (Claude Code)
> **Specialization:** Formula-level precision audit of the calculation engine,
> cross-checked against GEM-02's evidence classification.
> **Activates when:** A financial snapshot requires calculation-level audit
> rather than evidence-lineage review.

## Sub-agents

Internal sub-agents an engine spawns for its own work — Claude Task-tool
sub-agents, Codex's internal step orchestration, Antigravity background
subagents — stay **beneath** one registered ID. They never get their own row.
This registry lists accountable identities, not LLM call counts, so a vendor
changing internal fan-out never requires editing it.
