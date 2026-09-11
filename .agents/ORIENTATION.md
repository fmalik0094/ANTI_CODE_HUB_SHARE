# ORIENTATION — READ THIS FIRST

Single entry point for any engine session in this repository. Everything an
agent needs to not waste tokens rediscovering the workspace is below. If you
find yourself exploring to answer a question, that question's answer belongs
here — add it rather than re-deriving it next session.

---

## 1. What this repository is

**ANTI_CODE-HUB is a rulebook, not a project.** No application code ships from
here. `src/` is empty by design. Nothing in this repo runs in production.

It holds exactly three things:

| Thing | Where | Purpose |
| :--- | :--- | :--- |
| The contract | `.agents/rules/`, `.agents/AGENT_REGISTRY.md`, `.agents/workflows/` | Rules every project inherits |
| The seed | `anti-code hub/` | Copied verbatim to start a new project |
| The manual | `main.md`, `FM-NOTES/` | Human- and agent-readable explanation |

Real work happens in the ~26 project workspaces under
`C:\01_LOCAL_CODING_F.M\` (ROI_Analysis, CNC/mastercam, WATCHER, etc.),
each with its own git repo. Those are tracked by TOPIC-HUB-ENGINE, which is a
separate system — not this one.

**You are here for one of two reasons:** the contract needs changing, or a new
project is being seeded. If you're here for any other reason, you're probably
in the wrong repository.

---

## 2. Authoritative vs. historical

Reading a historical file as if it were current is the most common way sessions
waste tokens here. This table is the arbiter.

| File | Status |
| :--- | :--- |
| `.agents/AGENT_REGISTRY.md` | **Canonical** — 3 permanent leads + 3 parametric slots (see §3) |
| `.agents/rules/global.md` | **Canonical** — DENY > ASK > ALLOW precedence |
| `.agents/workflows/0*.md` | **Canonical** — session lifecycle |
| `main.md` | Current, but derived — reflects the above, doesn't override it |
| `AGENTS.md` (root) | Stub pointing at the registry. Do not put a table back in it |
| `agents/*/A*.md` (13 files) | **Historical.** Pre-date the agent-registry consolidation. Non-authoritative |
| `FM-NOTES/*.md` | **Historical.** Dual-IDE era; 14 of 15 never mention Claude. See `FM-NOTES/README.md` for per-file triage — one file contains an enforcement claim that is factually wrong |

---

## 3. The agents — 3 permanent + 3 parametric

One session claims **one** identity. Never two at once.

**Permanent** — fixed here, identical in every project:

| ID | Engine | Owns |
| :--- | :--- | :--- |
| `GEM-01` | Antigravity / Gemini | Macro-planning, architecture, topology |
| `CDX-01` | VS Code / Codex | Scaffolding, diffs, terminal, git ops |
| `CLD-01` | Claude Code | Deep refactor, correctness review, QA validation |

**Parametric** — one slot per engine, specialization defined by each project,
not here:

| Slot | Engine |
| :--- | :--- |
| `GEM-02` | Antigravity / Gemini |
| `CDX-02` | VS Code / Codex |
| `CLD-02` | Claude Code |

A project fills a slot in its own `.agents/AGENT_REGISTRY.md` with a
specialization *and* an activation condition. An unfilled slot is simply
unused. Don't activate one without writing both down.

This replaced a fixed 6-agent model in which the hub defined `GEM-02` as
"Multimodal Ingestion" while `CNC/ROI_Analysis` used the same ID for
"Financial Evidence Reviewer" — same identity, unrelated jobs, neither one
wrong. Parametric slots make both correct.

Sub-agents an engine spawns internally (Claude Task-tool sub-agents, Codex's
internal step orchestration, Antigravity background subagents) stay **beneath**
one registry row. They do not get their own IDs. This registry describes
accountable identities, not LLM call counts — it should not need editing when a
vendor changes internal fan-out.

---

## 4. Settled — do not relitigate

These were decided with evidence. Reopening them costs tokens and produces
churn. If you believe one is wrong, say so explicitly and give new evidence —
don't silently act against it.

- **Zone folders are gone — consolidation is complete.** `antigravity/`,
  `vscode/`, and `claude/` were staging areas carrying private duplicates of
  `.agents/` and `.state/`. Four drifting copies of the same governance caused
  nearly every bug found in the 2026-08 audits. Verified they held nothing the
  seed lacked, folded `tasks.json` into the seed, deleted all three.
  `anti-code hub/` is now the single template and must stay copyable as one
  clean folder. Do not recreate per-engine zones.
- **Branches are the concurrency control**, not markdown re-reads. See §5.
- **3 permanent agents + 3 parametric slots.** The count was previously stated
  as 6, 10, and 13 in different files simultaneously, then fixed at 6, then
  reduced to 3 permanent once it was clear slot `02` needed to vary per
  project. The validator enforces agreement between the registry and `main.md`.
- **`.claude/settings.json` is enforced, not advisory.** Unlike
  `.geminiignore`/`.aiexclude` (context filters), its `deny` entries are
  refused at the tool-call layer.
- **The seed Codex config uses documented controls only.**
  `anti-code hub/.codex/config.toml` omits explicit approval policy, retains
  `workspace-write`, and keeps command-spawned network access off when loaded.
  Approval behavior is inherited from app/user/managed policy, not guaranteed
  per command by the seed. New runtime evidence supersedes the old approval
  default: see the [Mastercam compatibility incident](../anti-code%20hub/.agents/resources/CODEX_COMPATIBILITY.md)
  and ADR-0011. No command-name deny list is claimed. Project trust can disable
  project-local config; it is not the retired explicit approval setting.
- **Never hand-copy a governance file between repos.** Doing so has twice
  silently dropped security rules and replaced project-specific content with
  generic boilerplate. Generate from what actually exists in the target.

---

## 5. How to work here

```
1. Claim ONE identity from §3, state it.
2. Branch:  git checkout -b <gem|cdx|cld>/<work-item>     # never work on main
3. Propose a plan. Halt for [PENDING OPERATOR APPROVAL] before mutating.
4. Work. Run `python validators/validate_structure.py` before claiming done.
5. Exit per .agents/workflows/03_exit_and_sync.md
```

**Approval gates — none of these are implied by the previous one:**
validation passing ≠ authorization to commit; committing ≠ authorization to
merge to `main`; merging ≠ authorization to push to a remote. Each needs the
operator to say so.

---

## 6. Validator

`python validators/validate_structure.py` checks structure *and* semantics:
required paths exist, `.claude/settings.json` parses and only grants paths that
are real, the agent count agrees between `AGENT_REGISTRY.md` and `main.md`, and
`_ACTIVE_INDEX.md` versions match the state files they reference.

The seed's project-neutral validator additionally parses its
`.codex/config.toml`, rejects keys outside the verified documented allowlist,
and requires omitted approval policy, workspace-write, and network-off. That
is seed-contract validation, not proof of effective host policy. Configuration
changes also require the seed's `validators/test_validate_structure.py` and
`validators/check_codex_runtime.py`; desktop task startup is a separate check.

The seed validator's result contract is 0 = implemented static checks completed,
1 = confirmed failure, 2 = incomplete verification (for example no TOML parser).
Missing TOML support does not stop other checks; failures take precedence over
incomplete verification. Seed placeholder warnings are not runtime certification.

If it fails, it names the specific contradiction. Fix that — don't work around
it.

---

## 7. Keeping this file honest

This file exists to prevent rediscovery. When you learn something during a
session that you had to dig for — a settled decision, a gotcha, a "why is it
like this" — add it here. A session that ends with this file unchanged after
discovering something non-obvious has left the next session to pay the same
cost again.
