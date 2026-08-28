# UAWC 1.0 Dynamic Flow Orchestration User Manual

================================================================================
          UNIFIED AGENT WORKSPACE CONTRACT (UAWC 1.0) - REPOSITORY SPEC
                     TRI-ENGINE GOVERNANCE AND EXECUTION
================================================================================

#### SECTION 1: MASTER DIRECTORY TOPOLOGY

`ANTI_CODE-HUB` is a rulebook and project seed, not an application. The tracked
topology below was regenerated from the directory listing on 2026-08-28. Local
untracked files and `.git/` internals are intentionally omitted.

```text
ANTI_CODE-HUB/
├── .agents/                              # Canonical hub contract
│   ├── AGENT_REGISTRY.md                 # 3 permanent leads + 3 parametric slots
│   ├── ORIENTATION.md                    # Single entry point
│   ├── resources/MODEL_REFERENCE.md      # On-demand vendor reference
│   ├── rules/global.md                   # DENY > ASK > ALLOW baseline
│   ├── states/                           # Hub checkpoint and active index
│   └── workflows/                        # Genesis, entry, exit/sync
├── .claude/settings.json                 # Enforced Claude Code permissions
├── .state/                               # Hub decisions, deltas, execution evidence
├── .vscode/settings.json                 # Root editor search/watcher exclusions
├── agents/                               # 13 historical, non-authoritative profiles
├── anti-code hub/                        # Copyable tri-engine project seed
│   ├── .agents/
│   │   ├── AGENT_REGISTRY.md
│   │   ├── ORIENTATION.md
│   │   ├── rules/
│   │   ├── states/
│   │   └── workflows/
│   ├── .claude/settings.json
│   ├── .codex/instructions.md
│   ├── .gemini/GEMINI.md
│   ├── .state/                           # Initialized project journals
│   ├── .vscode/settings.json
│   ├── docs/
│   ├── outputs/
│   ├── src/
│   ├── tests/
│   ├── validators/validate_structure.py  # Project-neutral validator
│   ├── .aiexclude
│   ├── .geminiignore
│   ├── .gitignore
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   └── hub_manager.py
├── antigravity/                          # Antigravity staging zone
│   ├── .agents/
│   ├── .gemini/GEMINI.md
│   └── AGENTS.md
├── claude/                               # Claude Code staging zone
│   ├── .agents/
│   ├── .claude/settings.json
│   ├── .state/
│   ├── outputs/
│   ├── src/
│   ├── AGENTS.md
│   └── CLAUDE.md
├── vscode/                               # VS Code/Codex staging zone
│   ├── .codex/
│   ├── .state/
│   ├── .vscode/
│   ├── src/
│   └── validators/
├── FM-NOTES/                             # Historical and reference manuals
├── validators/validate_structure.py      # Hub structural/semantic validator
├── .aiexclude                            # Codex context filter
├── .geminiignore                         # Gemini context filter
├── .gitignore                            # Git exclusions
├── AGENTS.md                             # Registry stub for Codex discovery
├── CLAUDE.md                             # Root Claude Code entry file
└── main.md                               # This derived manual
```

The seed now contains the orientation, registry, engine entry/configuration
files, filters, state journals, and project-neutral validator listed above.
The `antigravity/` and `claude/` zones contain no capability or path class
absent from the seed; they remain staging copies until their proven
configuration is folded into the seed and the zones can be deleted.

The VS Code zone has three unique operational files still awaiting that
decision: `vscode/.codex/config.toml`, `vscode/.vscode/tasks.json`, and
`vscode/validators/validate_config.py`. Its other files are staging mirrors or
legacy zone state. In particular, `vscode/.state/BASELINE_HASH.md` is not a
fourth engine capability and should not be promoted as one.

---

#### SECTION 2: CONTEXT FILTRATION AND REAL ENFORCEMENT BOUNDARIES

The repository uses three different mechanisms. They are not interchangeable.

##### 1. Context and indexing filters

- `.geminiignore` and `anti-code hub/.geminiignore` reduce files considered for
  Gemini context ingestion.
- `.aiexclude` and `anti-code hub/.aiexclude` reduce files presented to Codex
  context.
- `.vscode/settings.json` and `anti-code hub/.vscode/settings.json` reduce VS
  Code search and file-watcher activity for state, logs, temporary files, and
  heavy artifacts.

These are context and editor-performance filters. They do not deny direct file
access, authorize commands, or form a security boundary. Sensitive material
must still stay out of the repository and be protected by the operating system
and the tool's actual permission layer.

##### 2. Claude Code permissions

`.claude/settings.json` is the real repository-level Claude Code permission
surface for work on the hub. Its `allow`, `ask`, and `deny` lists are enforced
at Claude Code's tool-call layer. It requires approval for named Git,
destructive, elevated, download, and web-fetch operations and denies the named
system, parent, credential, key, and environment-file paths.

`anti-code hub/.claude/settings.json` provides the project-neutral equivalent
for a newly seeded project. `claude/.claude/settings.json` remains a staging
variant. A permission claim is valid only when the Claude session is governed
by the applicable file.

##### 3. Codex configuration status

`vscode/.codex/config.toml` currently contains staging keys for orchestration,
token management, terminal review, and a command list. Those keys are not in
OpenAI's documented Codex configuration reference, so this file must not be
described as enforcing them. The repository currently has no supported Codex
`config.toml` command deny list for `rm`, `sudo`, `curl`, or `wget`.

Codex safety therefore comes from the active host sandbox, approval policy,
operator instructions, and canonical workspace rules—not from the custom keys
in `vscode/.codex/config.toml`. Supported project configuration must be checked
against <https://developers.openai.com/codex/config-reference> before the VS
Code staging file is folded into the seed.

##### 4. Validator invocation

`python validators/validate_structure.py` is the hub quality gate. It runs when
an operator or agent invokes it. `vscode/.vscode/tasks.json` exposes manual VS
Code tasks, but no repository file runs the validator automatically on save and
validation does not unlock authorization gates.

---

#### SECTION 3: MULTI-AGENT INTERACTION MATRIX

The architecture runs **3 permanent agents**, one per engine, plus one
parametric slot per engine. `.agents/AGENT_REGISTRY.md` is canonical;
`AGENTS.md` is a discovery stub and does not duplicate the table.

```text
================================================================================
AGENT ID   ENGINE                 RESPONSIBILITY
================================================================================
PERMANENT — fixed in the hub and inherited by every project
GEM-01     Antigravity / Gemini   Macro-planning, architecture, topology
CDX-01     VS Code / Codex        Scaffolding, diffs, terminal, Git operations
CLD-01     Claude Code            Deep refactor, correctness review, QA validation
--------------------------------------------------------------------------------
PARAMETRIC — specialization and activation condition defined by each project
GEM-02     Antigravity / Gemini   Project-defined or unused
CDX-02     VS Code / Codex        Project-defined or unused
CLD-02     Claude Code            Project-defined or unused
================================================================================
```

A session claims one identity, never two. The hub does not assign a
specialization to any slot `02`. Before a project activates one, its own
`.agents/AGENT_REGISTRY.md` must state both the specialization and the upstream
condition that activates it.

Internal sub-agents remain beneath the registered identity that spawned them;
they do not create additional registry rows. The profiles beneath `agents/`
are historical reference material, not live squads, path permissions, or
additional identities.

The three permanent leads describe accountable ownership, not a rigid queue.
Planning, implementation, and verification may overlap when each work item is
isolated on its engine branch and handoffs are explicit.

---

#### SECTION 4: TRI-ENGINE LIFECYCLE

Every engine session starts at `.agents/ORIENTATION.md`. The engine instruction
surfaces `antigravity/.gemini/GEMINI.md`, `vscode/.codex/instructions.md`, and
`CLAUDE.md` all route sessions to that canonical entry point.

```text
[BOOT]                         [WORK]                         [EXIT]
1. Read ORIENTATION.md        1. Stay on assigned branch    1. Record deltas/evidence
2. Claim one identity         2. Make approved changes      2. Run the validator manually
3. Read relevant decisions   3. Keep scope engine-owned    3. Re-read shared state index
4. Create engine branch      4. Verify proportionally      4. Commit only if authorized
5. Obtain approval                                           5. Do not merge or push silently
```

##### Planning

`GEM-01` owns architecture, topology, and high-level sequencing. Planning
artifacts become explicit handoff inputs; they do not authorize another engine
to mutate files, commit, merge, or push.

##### Construction

`CDX-01` owns scaffolding, file changes, diffs, terminal execution, and Git
operations. It runs relevant validators after changes. VS Code tasks are
convenience launchers only; they are neither automatic nor approval gates.

##### Verification

`CLD-01` owns deep correctness review, refactoring, and QA validation. The
applicable `.claude/settings.json` constrains Claude Code tool calls, but a
successful validation still does not authorize a commit or any later Git
operation.

##### Exit and synchronization

`.agents/workflows/03_exit_and_sync.md` is the canonical exit procedure.
Work occurs on `gem/<item>`, `cdx/<item>`, or `cld/<item>`, never directly on
`main`. Re-reading `.agents/states/_ACTIVE_INDEX.md` before a state write remains
a useful stale-state check, but it is secondary to branch isolation and is not
a lock.

Validation, commit, merge, and push are separate gates. Permission for one does
not imply permission for the next.

---

#### SECTION 5: SYSTEMIC FAILURE MODES AND SAFEGUARDS

##### 1. Watcher and context churn

*Cause:* Heavy artifacts, transient output, and state history entering editor
indexes or model context increase disk activity and consume context without
improving the task.

*Safeguard:* Maintain the patterns in `.geminiignore`, `.aiexclude`, and
`.vscode/settings.json`. Treat them as performance/context controls, not access
denials. No automatic build runner or on-save validator is configured here.

##### 2. Semantic data inflation

*Cause:* Loading raw tables, CAD assets, archives, or long telemetry into a
general reasoning session crowds out the contract and current work item.

*Safeguard:* Load `.agents/resources/MODEL_REFERENCE.md` only for model/API
work, keep large formats behind the existing context filters, and use focused
local scripts beneath `validators/` when deterministic inspection is needed.

##### 3. Windows file-handle contention

*Cause:* Editors, indexers, and external applications can retain handles on
local or network files while another engine attempts a write.

*Safeguard:* Identify the process holding the file, close or pause the owning
application when safe, and obtain operator approval before terminating a
process. Context filters reduce scanning pressure but do not release file
handles or guarantee the absence of contention.

##### 4. Concurrent state collision

*Cause:* Multiple engines writing the same state or governance file on `main`
can silently overwrite one another.

*Safeguard:* Use one branch per engine per work item as required by
`.agents/workflows/03_exit_and_sync.md`. Git then exposes the collision as a
merge conflict. Re-read `_ACTIVE_INDEX.md` before a state write as a secondary
freshness check, reconcile any newer state, and never treat that read as the
primary concurrency mechanism.

##### 5. Configuration-as-security illusion

*Cause:* A comment, ignore pattern, or undocumented config key can look like a
hard gate even when no tool enforces it.

*Safeguard:* Tie every enforcement claim to an actual mechanism. In this
repository, Claude Code permissions are enforced by `.claude/settings.json`.
Gemini and Codex ignore files filter context. The custom policies currently in
`vscode/.codex/config.toml` are not an enforced Codex command gate.

---

#### SECTION 6: ARCHITECTURAL LESSONS AND PENDING CONSOLIDATION

##### 1. Orientation and state

`.agents/ORIENTATION.md` is the dense current contract. State journals preserve
decisions and execution evidence, but historical state never overrides the
orientation, registry, global rules, or workflows.

##### 2. Localized governance

Project configuration must be generated from paths and capabilities that
actually exist in that project. Governance files must not be hand-copied
between repositories. Context filtering, permission enforcement, and human
approval are separate layers and must be documented separately.

##### 3. Validation

The root validator checks this hub. The seed's
`anti-code hub/validators/validate_structure.py` is project-neutral and checks
the inherited contract after the seed is copied. Both are manually invoked;
neither proves application correctness or authorizes Git operations.

##### 4. State utility status

`anti-code hub/hub_manager.py` exists, but its `bundle` and `parse`
commands are not implemented. It is not a required lifecycle component and
must not be described as automatic context bundling. Its state-pruning behavior
should be treated as experimental until separately tested and accepted.

The seed's global rules also contain an on-demand model-reference instruction,
but no seed-local model-resource file is tracked. That packaging gap is outside
this manual-only correction pass and must not be mistaken for a working local
resource.

##### 5. Zone consolidation

The current settled plan is staged consolidation, not immediate deletion:

1. Verify an engine-specific configuration in its zone.
2. Adapt the proven configuration to the project-neutral seed.
3. Validate the seed.
4. Delete the redundant zone only in a separately approved pass.

For VS Code, the remaining operational review scope is exactly
`vscode/.codex/config.toml`, `vscode/.vscode/tasks.json`, and
`vscode/validators/validate_config.py`. The `antigravity/` and `claude/` zones
currently add no capability the seed lacks. All zones remain in place during
this correction pass.
