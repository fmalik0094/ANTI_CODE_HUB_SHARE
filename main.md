# UAWC 1.0 Dynamic Flow Orchestration User Manual

================================================================================
          UNIFIED AGENT WORKSPACE CONTRACT (UAWC 1.0) - REPOSITORY SPEC
                     TRI-ENGINE GOVERNANCE AND EXECUTION
================================================================================

#### SECTION 1: MASTER DIRECTORY TOPOLOGY

`ANTI_CODE-HUB` is a rulebook and project seed, not an application. The tracked
topology below was regenerated from the directory listing on 2026-08-31. Local
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
│   ├── .codex/
│   │   ├── config.toml                   # Sandbox defaults; approvals inherited
│   │   └── instructions.md               # Codex execution instructions
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
├── FM-NOTES/                             # Historical; see FM-NOTES/README.md
├── validators/validate_structure.py      # Hub structural/semantic validator
├── .aiexclude                            # Codex context filter
├── .geminiignore                         # Gemini context filter
├── .gitignore                            # Git exclusions
├── AGENTS.md                             # Registry stub for Codex discovery
├── CLAUDE.md                             # Root Claude Code entry file
└── main.md                               # This derived manual
```

The seed contains the orientation, registry, engine entry/configuration files,
filters, state journals, and project-neutral validator listed above. It is the
single template.

**Zone consolidation is complete.** The former `antigravity/`, `vscode/`, and
`claude/` staging zones were deleted on 2026-08-28 after verification that they
held no file class the seed lacked. Each had carried a private duplicate of
`.agents/` and/or `.state/` — four drifting copies of the same governance, which
was the mechanism behind nearly every defect found in the 2026-08 audits.
`vscode/.vscode/tasks.json` was adapted into the seed. The old
`validate_config.py` and undocumented `config.toml` were not carried. A
supported Codex configuration and semantic validation now live directly in the
seed; see §2.3. Per-engine zones must not be recreated.

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
for a newly seeded project. A permission claim is valid only when the Claude
session is actually governed by the applicable file — the hub's for work on the
hub, the project's own for work in a seeded project.

##### 3. Codex configuration status — DEFAULTS, NOT UNIVERSAL APPROVAL

`anti-code hub/.codex/config.toml` uses only keys verified against OpenAI's
documented Codex configuration reference on 2026-09-10:

- Explicit `approval_policy` is omitted. App/user/managed policy determines
  approvals; the seed does not guarantee review of every command.
- `sandbox_mode = "workspace-write"` permits work inside the active workspace
  while retaining the Codex sandbox boundary.
- `sandbox_workspace_write.network_access = false` keeps outbound access off
  for scripts, programs, and subprocesses launched by commands.

Codex loads project-scoped configuration only after the project is trusted.
The active host, managed requirements, and launch overrides can supersede this
posture, so this file is a supported project default—not an immutable security
policy.

The documented schema still provides **no general command-name deny list**.
`rm`, `sudo`, `curl`, and `wget` are not individually denied by this file and no
approximate replacement is claimed. REQUEST REVIEW is an operator rule, not
proof of automatic per-command gating by this config.

The seed validator parses TOML, rejects all explicit approval overrides and keys
outside its narrow allowlist, and checks sandbox/network defaults. It is not a
complete vendor schema or runtime test. Source:
[OpenAI configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

The old explicit `untrusted` policy is retired, not a supported default. Valid
user-level project trust is a different mechanism with configuration-loading
tradeoffs. See the [current boundary and Mastercam incident](anti-code%20hub/.agents/resources/CODEX_COMPATIBILITY.md)
for the official migration source, stricter-approval alternative, regression
checks and independent runtime probe. No user/managed settings are changed by
the seed. CLI loading and desktop startup must be reported separately.

##### 4. Validator invocation

`python validators/validate_structure.py` is the hub quality gate; the seed
carries its own project-neutral equivalent. Both run only when an operator or
agent invokes them. `anti-code hub/.vscode/tasks.json` exposes a manual VS Code
task as a convenience launcher. No repository file runs a validator
automatically on save, and validation does not unlock any authorization gate.

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

Every engine session starts at `.agents/ORIENTATION.md`. In this hub, root
`CLAUDE.md` routes there. In a seeded project, all three engine entry files —
`CLAUDE.md`, `.gemini/GEMINI.md`, and `.codex/instructions.md` — route to that
project's own copy.

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
Gemini and Codex ignore files filter context and enforce nothing. The seed's
`.codex/config.toml` supplies sandbox/network defaults, while approval behavior
is inherited. It is not a per-command deny list. Seed validation rejects
out-of-contract keys and retired policy overrides, but validators can share a
stale assumption with a template. Independently exercise the installed runtime;
see §2.3 for the concrete incident and evidence limits.

---

#### SECTION 6: ARCHITECTURAL LESSONS AND CONSOLIDATION STATUS

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

Completed on 2026-08-28. All three zones were verified to hold no file class the
seed lacked, `tasks.json` was adapted into the seed, and `antigravity/`,
`vscode/`, and `claude/` were deleted. Four drifting copies of the same
governance became one.

The zone's `validate_config.py` was not carried forward because it only checked
for file existence. Its undocumented `config.toml` was replaced—not copied—by
the supported seed configuration and semantic checks described in §2.3.

Per-engine zones must not be recreated. If an engine needs configuration, it
belongs in the seed alongside the other two, where one validator covers it.
