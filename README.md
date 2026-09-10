# ANTI-CODE HUB

**A governance contract and project seed for running three AI coding engines — Google Antigravity/Gemini, VS Code/Codex, and Claude Code — against the same codebase without them overwriting each other or losing context between sessions.**

`main` · Contract V1.1 · Unified Agent Workspace Contract (UAWC 1.0)

---

## What this is

A **rulebook and a starter kit**. Two things, nothing else.

It defines how three AI engines behave — what each is accountable for, where each may write, how they avoid colliding, and what requires human approval. It also holds the folder you copy to start a new project with all of that already wired in.

## What this is *not*

**This repository contains no application code and never will.** `src/` is empty by design. Nothing here runs in production, ships, or gets deployed.

Actual project work happens in separate repositories elsewhere on disk. This repo governs *how* engines behave in those projects — it is not one of them.

You are here for exactly two reasons: **the contract needs changing**, or **a new project is being seeded**. Anything else means you're in the wrong repository.

---

## The problem it solves

Running multiple AI coding agents against one codebase produces two failure modes that compound:

1. **Context loss.** Long sessions forget decisions made hours earlier, hallucinate file paths, and re-derive settled architecture from scratch — burning tokens rediscovering what the repo already knows.
2. **Silent clobbering.** Two engines edit the same file; the last writer wins and nobody notices what was lost.

The answers here are deliberately boring, because boring survives contact with reality:

- **Decisions live on disk**, not in chat memory — `.agents/` and `.state/` are the record.
- **One dense entry point** every engine reads first, so nothing is rediscovered per-session.
- **Git branches are the lock.** One branch per engine per work item turns a race condition into a merge conflict you can see.
- **Enforcement is named or it isn't claimed.** A config that looks protective but enforces nothing is worse than no config — it earns trust it cannot honor.

---

## The three engines

| ID | Engine | Accountable for |
| :--- | :--- | :--- |
| `GEM-01` | Antigravity / Gemini | Macro-planning, architecture, topology |
| `CDX-01` | VS Code / Codex | Scaffolding, diffs, terminal, git operations |
| `CLD-01` | Claude Code | Deep refactor, correctness review, QA validation |

Plus **one parametric slot per engine** — `GEM-02`, `CDX-02`, `CLD-02` — whose specialization each *project* defines for itself, never the hub. A financial project might make `CLD-02` a formula auditor; another might leave it unused. This exists because a fixed model forced one meaning per ID workspace-wide, and two projects legitimately needed the same ID for unrelated jobs.

**A session claims one identity. Never two.** Internal sub-agents an engine spawns stay beneath one registered ID — the registry lists accountable identities, not call counts.

---

## Repository structure

```
ANTI_CODE-HUB/
├── .agents/                        The contract
│   ├── ORIENTATION.md              ← single entry point; read this first
│   ├── AGENT_REGISTRY.md           canonical agent identities
│   ├── rules/global.md             DENY > ASK > ALLOW baseline
│   ├── workflows/                  genesis · entry · exit-and-sync
│   ├── resources/                  on-demand vendor/model reference
│   └── states/                     versioned checkpoints
├── .state/                         DECISIONS (ADRs) · DELTA_LOG · EXECUTION_LOG
├── .claude/settings.json           the one enforced permission surface
├── anti-code hub/                  ← THE SEED: copy this to start a project
├── agents/                         13 historical profiles (non-authoritative)
├── FM-NOTES/                       dual-IDE-era research — see its README
├── validators/                     semantic consistency checks
└── main.md                         full operations manual
```

---

## Starting a new project

```bash
cp -r "anti-code hub" /path/to/NEW_PROJECT
cd /path/to/NEW_PROJECT
python validators/validate_structure.py    # passes out of the box
```

Then follow `.agents/workflows/01_genesis_prompt.md` — it walks through replacing `[PROJECT NAME]` placeholders, defining any parametric slots the project needs, and `git init`.

The new project arrives with three engine entry points, orientation, permission settings, context filters, state journals, and a project-neutral validator. Codex sandbox/network defaults apply only when loaded; approval behavior is inherited from the host's policy.

This flow is smoke-tested: the seed is instantiated to a temp path and validated clean both before and after genesis.

---

## How work happens

```
1. Claim ONE identity
2. git checkout -b <gem|cdx|cld>/<work-item>     ← never work on main
3. Propose a plan → halt for operator approval
4. Work
5. python validators/validate_structure.py
6. Exit per .agents/workflows/03_exit_and_sync.md
```

**Approval gates, none implied by the previous:**

> validation passing ≠ authorization to commit
> committing ≠ authorization to merge
> merging ≠ authorization to push

Each requires the operator explicitly.

---

## Enforcement vs. filtering

These are not interchangeable, and conflating them is how a workspace acquires security theatre:

| File | Reality |
| :--- | :--- |
| `.claude/settings.json` | **Enforced.** Denies at the tool-call layer. |
| `anti-code hub/.codex/config.toml` | Seed sandbox/network defaults when loaded; approvals inherited from app/user/managed policy. No per-command review guarantee. |
| `.geminiignore` | Context filter. Reduces what a model is shown. Denies nothing. |
| `.aiexclude` | Context filter. Denies nothing. |

Three separate instances of config that *looked* protective and wasn't were found and removed during the V1.1 revamp. The standing rule: **never claim enforcement without naming the mechanism.**

---

## Validation

```bash
python validators/validate_structure.py                 # the hub
cd "anti-code hub" && python validators/validate_structure.py   # the seed
```

These check **semantics, not just file existence** — that agent counts agree across documents, that every permission grant points at a real path, that no engine entry file pins a parametric slot, that checkpoint versions match their state files, and that the Codex config uses only documented keys.

For Codex config changes, run the seed's regression suite and independent CLI
loader probe described in the [compatibility record](anti-code%20hub/.agents/resources/CODEX_COMPATIBILITY.md).
Template agreement does not prove runtime support; CLI loading does not prove
desktop task startup. The seed now rejects explicit approval overrides, including
the retired `untrusted` value, rather than enforcing one.

An earlier version performed 16 existence checks and passed green while the repository contradicted itself in six documented ways. That is the failure mode these replaced.

Staleness **warns without failing** — an aging reference should never block unrelated work.

*Requires Python 3.11+ for full coverage; on older interpreters the TOML check is skipped with an explicit warning and everything else still runs.*

---

## Where to read more

| Document | For |
| :--- | :--- |
| [`.agents/ORIENTATION.md`](.agents/ORIENTATION.md) | **Start here.** Dense current contract, settled decisions |
| [`main.md`](main.md) | Full operations manual: topology, lifecycle, failure modes |
| [`.state/DECISIONS.md`](.state/DECISIONS.md) | Accepted decisions and their reasoning |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |
| [`FM-NOTES/README.md`](FM-NOTES/README.md) | Triage of historical dual-IDE-era research |

---

## Status

**Contract V1.1** — structurally validated, both validators passing, seed smoke-tested.

Downstream use exposed a real compatibility defect: Mastercam's reported
2026-09-09 remediation passed governance checks and 29 tests yet failed Codex
startup on the seed's retired approval value. The [incident record](anti-code%20hub/.agents/resources/CODEX_COMPATIBILITY.md)
separates that operator report from the hub's local verification. Desktop startup
after correction has not been verified here.

**Known open:** ~25 sibling projects still carry the legacy fixed-six agent registry. Deferred to a separate system-overhaul effort rather than bolted on here.
