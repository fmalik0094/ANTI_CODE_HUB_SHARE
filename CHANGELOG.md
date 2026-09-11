# Changelog

Contract versions track `.agents/states/`. Reasoning behind each settled
decision lives in [`.state/DECISIONS.md`](.state/DECISIONS.md) as numbered ADRs;
this file records what changed and when.

---

## Unreleased — 2026-09-10 compatibility correction

- Follow-up: unavailable TOML parsing now produces UNVERIFIED/exit 2 after other
  checks run; confirmed failures retain exit 1 precedence. Success text is scoped
  to implemented seed-contract checks. Five new regressions expand the suite
  from 24 to 29 tests; existing configuration defaults are unchanged.

- Removed the retired explicit Codex approval policy from the seed; retained
  workspace-write and command network-off. Approvals are inherited, not
  guaranteed per command by the seed. ADR-0011 records the boundary.
- Updated the seed validator and current guidance; added regression tests and
  an independent runtime loader probe. The earlier V1.1 configuration claim
  below is historical and superseded, not current setup guidance.
- Recorded the [Mastercam incident and verification limits](anti-code%20hub/.agents/resources/CODEX_COMPATIBILITY.md).
  No cross-project propagation or desktop startup verification is claimed.

---

## V1.1 — 2026-08-31

Governance revamp. The contract described a system that did not match disk in
six documented ways; V1.1 reconciles them and adds validation that fails when
they drift apart again.

### Agent model

- **3 permanent leads + 3 parametric slots** replaces a fixed six-agent model.
  `GEM-01`, `CDX-01`, `CLD-01` are fixed and inherited by every project.
  `GEM-02`, `CDX-02`, `CLD-02` are slots each project defines for itself.
  *Why:* the hub pinned `GEM-02` as "Multimodal Ingestion" while a downstream
  project used the same ID for "Financial Evidence Reviewer" — same identity,
  unrelated jobs, neither wrong. (ADR-0007)
- Agent count previously read **6, 10, and 13 simultaneously** across
  `AGENT_REGISTRY.md`, `main.md`, and `agents/*/`. Now one number, validator
  enforced. `.agents/AGENT_REGISTRY.md` is sole authority; root `AGENTS.md` is a
  discovery stub. (ADR-0003)
- Internal sub-agents stay beneath one registered ID — the registry lists
  accountable identities, not LLM call counts.

### Concurrency

- **Branch-per-engine-per-item** (`gem/`, `cdx/`, `cld/`) replaces
  "re-read the shared index before writing," which was a time-of-check /
  time-of-use race, not a lock. Collisions now surface as git merge conflicts.
  Validated in practice when two engines edited the same validator on separate
  branches. (ADR-0004)

### Enforcement honesty

- **Three instances of decorative security config removed.** (ADR-0005)
  - A Codex `deny_list` for `rm`/`sudo`/`curl`/`wget` using keys absent from
    OpenAI's documented reference — it enforced nothing while `main.md` claimed
    it gated dangerous commands.
  - A `chat.permissions.default: autopilot` override contradicting the
    `DENY > ASK > ALLOW` baseline in `global.md`.
  - A claim in `FM-NOTES` that `.aiexclude` denies at the filesystem layer
    returning `IO_ACCESS_DENIED`. It is a context filter and denies nothing.
- Replaced with a **verified** `.codex/config.toml` in the seed using only
  documented keys (`approval_policy = "untrusted"`,
  `sandbox_mode = "workspace-write"`, `network_access = false`).
- Standing rule: never claim enforcement without naming the mechanism. An
  absent control is safer than a decorative one.

### Structure

- **Zone folders deleted.** `antigravity/`, `vscode/`, and `claude/` each
  carried a private duplicate of `.agents/` and/or `.state/` — four drifting
  copies of one governance set, the mechanism behind nearly every defect found.
  Verified they held nothing the seed lacked before deletion. `anti-code hub/`
  is now the single template. (ADR-0008)
- **`.agents/ORIENTATION.md` added** as the single entry point. Boot sequences
  previously pointed at 7 files totalling 42 lines that taught almost nothing,
  while 2,787 lines of actual knowledge went unmentioned — so every session
  re-explored the repo from scratch. All engine entry files now route here.

### Seed

- Brought `anti-code hub/` up to the full contract. It previously had none of
  the above, so a new project would have been born with every problem listed
  here. Added orientation, registry, all three engine configs, `.aiexclude`,
  `.gitignore`, state journals, and a project-neutral validator.
- Smoke-tested end to end: instantiated to a temp path, validated clean before
  and after genesis placeholder replacement.

### Tooling

- **Validators check semantics, not existence.** The previous version ran 16
  `.exists()` checks and passed green while the repo contradicted itself.
  Now verifies agent-count agreement, that permission grants point at real
  paths, that no boot file pins a parametric slot, checkpoint consistency, and
  Codex config key validity. (ADR-0009)
- Staleness **warns without failing** — an aging reference never blocks
  unrelated work.
- Seed validator degrades gracefully when `tomllib` is unavailable
  (Python < 3.11) rather than aborting every check.
- **`hub_manager.py` prune data-loss bug fixed.** Versions parsed as floats made
  `V1.10` sort below `V1.9`, so at version 10 prune would archive the newest
  state binary and keep an older one as "latest truth." Now parsed as an integer
  tuple. Exercised end to end.
- **`bundle` and `parse` removed from the CLI.** They printed "not implemented"
  and exited 0, so automation could record a phantom success. (ADR-0010)

### Documentation

- `main.md` rewritten against disk — it had described paths that did not exist,
  a validator that ran automatically on save, and the superseded concurrency
  model.
- Root exit workflow no longer invokes `TOPIC-HUB-ENGINE/multi_harvester.py`.
  That script *pulls* state from all registered projects into its own repo;
  calling it from here meant every hub session wrote into a different project's
  directory.
- `FM-NOTES/README.md` added. 14 of 15 files there never mention Claude — the
  folder is dual-IDE-era research, now triaged per file rather than deleted.
- `.state/DECISIONS.md` grew from one line to 10 ADRs carrying reasoning, so
  future sessions inherit *why*, not just *what*.

### Known open

- ~25 sibling projects still carry the legacy fixed-six registry. Deferred to a
  separate system-overhaul effort.
- The contract is verified but not yet battle-tested — no project has been
  created from this seed and worked in.

---

## V1.0 — 2026-08-14

Initial Anti-Code Hub Tier 1 topology. Dual-IDE era (Antigravity + VS Code),
later extended with a third engine whose governance described files that did not
yet exist anywhere in the repository — the gap V1.1 opened by closing.
