# ORIENTATION — READ THIS FIRST

Single entry point for any engine session in this project. Everything an agent
needs to avoid rediscovering the workspace is below. If you find yourself
exploring to answer a question, that question's answer belongs here — add it
rather than re-deriving it next session.

> **Seeded from ANTI_CODE-HUB.** Fill in section 1 and the parametric slots in
> section 3 for this project. Delete this note once you have.

---

## 1. What this project is

**[PROJECT NAME]** — [one paragraph: what it does, who uses it, what "done"
looks like. Replace this.]

| Thing | Where |
| :--- | :--- |
| Production code | `src/` |
| Tests | `tests/` |
| Validators | `validators/` |
| Generated output | `outputs/` |
| Governance | `.agents/` |
| Session history | `.state/` |

---

## 2. Authoritative vs. historical

Reading a stale file as if it were current is the most common way sessions
waste tokens. This table is the arbiter. Keep it accurate.

| File | Status |
| :--- | :--- |
| `.agents/AGENT_REGISTRY.md` | **Canonical** — agent identities |
| `.agents/rules/global.md` | **Canonical** — DENY > ASK > ALLOW precedence |
| `.agents/workflows/0*.md` | **Canonical** — session lifecycle |
| `.agents/resources/MODEL_REFERENCE.md` | Reference — read on demand, not preloaded |
| `.agents/resources/CODEX_COMPATIBILITY.md` | Current Codex compatibility boundary and dated incident evidence — read when changing configuration |
| `.state/DECISIONS.md` | **Canonical** — accepted architectural decisions |
| `.state/DELTA_LOG.md` / `EXECUTION_LOG.md` | Historical evidence, not current authority |

---

## 3. The agents — 3 permanent + 3 parametric

One session claims **one** identity. Never two at once.

**Permanent** — inherited from the hub, identical in every project:

| ID | Engine | Owns |
| :--- | :--- | :--- |
| `GEM-01` | Antigravity / Gemini | Macro-planning, architecture, topology |
| `CDX-01` | VS Code / Codex | Scaffolding, diffs, terminal, git ops |
| `CLD-01` | Claude Code | Deep refactor, correctness review, QA validation |

**Parametric** — one slot per engine. Define these for *this* project, or leave
them unused. Both the specialization and the activation condition are required
before a slot may be claimed.

| Slot | Engine | Specialization | Activates when |
| :--- | :--- | :--- | :--- |
| `GEM-02` | Antigravity / Gemini | *(undefined — unused)* | — |
| `CDX-02` | VS Code / Codex | *(undefined — unused)* | — |
| `CLD-02` | Claude Code | *(undefined — unused)* | — |

Sub-agents an engine spawns internally (Claude Task-tool sub-agents, Codex's
internal step orchestration, Antigravity background subagents) stay **beneath**
one registry row. They never get their own IDs.

---

## 4. Settled — do not relitigate

Decisions made with evidence. Reopening them costs tokens and produces churn.
If you believe one is wrong, say so with new evidence — don't silently act
against it. Add this project's own settled decisions here as they accumulate.

- **Branches are the concurrency control.** One branch per engine per work item
  (`gem/<item>`, `cdx/<item>`, `cld/<item>`). Never work directly on `main`.
  Re-reading a shared index before writing is a race, not a lock.
- **`.claude/settings.json` is enforced, not advisory.** Unlike
  `.geminiignore`/`.aiexclude` (context filters), its `deny` entries are
  refused at the tool-call layer.
- **`.codex/config.toml` supplies sandbox defaults, not universal approval.**
  It omits explicit approval policy, retains `workspace-write`, and disables
  command-spawned network access when this project configuration is loaded.
  Approval behavior comes from app/user/managed policy. The retired explicit
  `untrusted` approval value must not return; valid project trust is a different
  control and can disable project-local config. No command-name deny list or
  per-command review guarantee is claimed. See
  [compatibility evidence](resources/CODEX_COMPATIBILITY.md).
- **Never hand-copy a governance file between repos.** It has repeatedly
  dropped security rules and replaced project-specific content with generic
  boilerplate. Generate from what actually exists in the target.
- **Slot 02 is project-defined.** No boot file may pin its specialization.

---

## 5. How to work here

```
1. Claim ONE identity from section 3, state it.
2. Branch:  git checkout -b <gem|cdx|cld>/<work-item>     # never work on main
3. Propose a plan. Halt for [PENDING OPERATOR APPROVAL] before mutating.
4. Work. Run `python validators/validate_structure.py` before claiming done.
5. Exit per .agents/workflows/03_exit_and_sync.md
```

**Approval gates — none is implied by the previous one:** validation passing ≠
authorization to commit; committing ≠ authorization to merge to `main`;
merging ≠ authorization to push. Each needs the operator to say so.

For Codex configuration changes, also run
`python -B -m unittest discover -s validators -p test_validate_structure.py`
and `python -B validators/check_codex_runtime.py`. Unit/semantic agreement is
not runtime proof, and the CLI probe does not prove desktop task startup.

---

## 6. Keeping this file honest

This file exists to prevent rediscovery. When you learn something you had to
dig for — a settled decision, a gotcha, a "why is it like this" — add it here.
A session that ends with this file unchanged after discovering something
non-obvious has left the next session to pay the same cost again.
