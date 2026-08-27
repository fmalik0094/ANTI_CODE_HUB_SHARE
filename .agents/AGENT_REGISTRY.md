# TRI-ENGINE AGENTS & GOVERNANCE MATRIX

Three permanent leads — one per engine — plus one parametric slot per engine
that each project defines for itself.

## Permanent leads (fixed, inherited by every project)

| Agent ID | Engine | Primary Specialization | Authority Layer |
| :--- | :--- | :--- | :--- |
| **GEM-01** | Google Antigravity (Gemini) | Macro-Planning, Architecture, Topology | Planning Lead |
| **CDX-01** | VS Code / Codex (OpenAI) | Scaffolding, Diffs, Terminal Execution, Git Ops | Execution Lead |
| **CLD-01** | Claude Code (Anthropic) | Deep Refactoring, Correctness Review, QA Validation | Verification Lead |

These three are the same in every workspace. A session claims **one** — never
two at once.

## Parametric slots (one per engine, defined per project)

| Slot | Engine | Specialization |
| :--- | :--- | :--- |
| `GEM-02` | Google Antigravity (Gemini) | Defined by the project's own registry |
| `CDX-02` | VS Code / Codex (OpenAI) | Defined by the project's own registry |
| `CLD-02` | Claude Code (Anthropic) | Defined by the project's own registry |

Slot `02` exists so a project can add one specialist per engine without
inventing a parallel identity scheme. The hub does **not** fix what these do —
each project states it in its own `.agents/AGENT_REGISTRY.md`, along with the
activation condition (what upstream input must be ready before the slot wakes).

A slot left undefined is simply unused. Do not activate one without a written
specialization and activation condition in the project's registry.

**Why parametric:** the hub previously fixed `GEM-02` as "Multimodal Ingestion
& Vision" while `CNC/ROI_Analysis` independently used the same ID for
"Financial and Evidence Reviewer." Same identity, unrelated jobs, no way for
either to be wrong. Slot `02` being project-defined makes both correct.

## Sub-agents

Internal sub-agents an engine spawns to do its own work — Claude Task-tool
sub-agents, Codex's internal step orchestration, Antigravity's background
subagents — stay **beneath** one registered ID. They never get their own row.
This registry lists accountable identities, not LLM call counts, so a vendor
changing internal fan-out never requires editing it.

## Historical

The 13 profile files under `agents/*/A*.md` predate this registry and are
non-authoritative. See the header note in each.
