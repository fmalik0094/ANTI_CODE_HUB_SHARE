# WORKSPACE BLUEPRINT: CWI/CNC COMPLIANT BASE TEMPLATE

This document serves as the master blueprint to initialize new project workspaces under strict multi-agent (Antigravity/Codex/Claude) local governance rules.

> **Sync note:** this copy mirrors `antigravity/.agents/rules/base_workspace_template.md` and `anti-code hub/.agents/rules/base_workspace_template.md`, which are canonical. If this drifts from them again, treat those two as correct.

---

## 1. TARGET DIRECTORY MATRIX
```text
[PROJECT_ROOT]/
├── .agent/
│   └── skills/                         # Skill folders containing SKILL.md rules
├── .agents/
│   ├── rules/
│   │   └── global.md                   # Global identity & security constraints
│   ├── states/
│   │   ├── _ACTIVE_INDEX.md            # Master registry file
│   │   └── [DOMAIN]_V[X.Y].md          # Domain-specific state binaries
│   └── workflows/
│       ├── 01_genesis_prompt.md        # Genesis protocol template
│       ├── 02_entry_and_propose.md     # Entry protocol template
│       └── 03_exit_and_sync.md         # Exit/Sync protocol template
├── .codex/
│   ├── config.toml                     # Codex orchestration allowed/denied paths
│   └── [DOMAIN]_CODEX_RULES.md         # Codex preflight and safety checks
├── .claude/
│   └── settings.json                   # Claude Code permissions.allow/ask/deny enforcement
├── CLAUDE.md                           # Claude Code auto-loaded identity & boot sequence
├── AGENTS.md                           # VS Code / Codex Agent Contract
└── hub_manager.py                      # Local python CLI utility for pruning/merging
```

---

## 2. FILE TEMPLATES

### Template A: `AGENTS.md` (Root)
```markdown
# VS CODE / OPENAI CODEX AGENT CONTRACT
[ROLE: COGNITIVE STATE ENFORCER]
- Execution Mode: Incremental Diffs Only.
- Permission Ring: Workspace-Local file I/O = ALLOWED. External script actuation = ASK. Outside path execution = DENY.
- Exclusions: Never run file indexing over raw data directories. State tracking variables must read directly from `.agents/states/`.
- Tone Parameter: Engineer delivery. Zero filler statements or pleasantries.
- Raw Source Lock: The project root directory is the strict write boundary.
- Derived Output Root: All outputs must be written exclusively to allowed folders.
- Codex must apply `.codex/[DOMAIN]_CODEX_RULES.md` and all agent skills under `.agent/skills/`.
```

### Template B: `.codex/config.toml`
```toml
[agent_orchestration]
engine = "openai-codex"
sandbox_mode = true
network_access = false
max_file_edit_lines = 0

[workspace_governance]
allowed_write_roots = [".agent/skills/", ".agents/states/", "docs/", "src/", "outputs/"]
denied_write_roots = ["C:/Windows/", "C:/Program Files/"]
require_human_gate = true
```

### Template C: `.agents/rules/global.md`
```markdown
# GLOBAL IDENTITY AND SECURITY MATRIX
[GOVERNANCE LEVEL: STRICT]

## System Capability Ring
1. `DENY` -> Remote exfiltration nodes, third-party network ports, cloud integrations.
2. `ASK`  -> Local terminal command execution and script runs.
3. `ALLOW` -> Reading localized skill files and writing state variables to `.agents/states/`.

## Token Optimization Criteria
- Never allow raw database arrays or G-Code to loop into the prompt instruction array.
```

### Template D: `CLAUDE.md` (Root)
```markdown
# CLAUDE.md — [PROJECT] EXECUTION CONTRACT
[ROLE: DEEP REFACTORER / QA — THIRD ENGINE]

## Boot Sequence
1. Read `.agents/rules/global.md` — DENY > ASK > ALLOW is absolute.
2. Read `.agents/states/_ACTIVE_INDEX.md` and load the latest accepted state binary.
3. Inspect `.state/DECISIONS.md` and `.state/DELTA_LOG.md`.
4. Propose a plan and halt for [PENDING OPERATOR APPROVAL] before any mutation.

## Boundaries
- Writes confined to `src/**` and `outputs/**`. State binaries confined to `.agents/states/**`.
- Work on a dedicated branch per work item (`cld/<item>`) — this is the real concurrency control, not the re-read-before-write check below.
- Before writing a state binary, re-read `_ACTIVE_INDEX.md` for a version newer than the one loaded at boot — Antigravity and Codex may have written since. Never blind-overwrite.
- Destructive or unvetted terminal commands require explicit operator approval.

## Tone
Engineer delivery. Zero filler.
```

### Template E: `.claude/settings.json`
```json
{
  "permissions": {
    "allow": [
      "Read(.agents/**)",
      "Write(src/**)",
      "Write(outputs/**)",
      "Write(.agents/states/**)"
    ],
    "ask": [
      "Bash(rm:*)",
      "Bash(git push --force:*)",
      "Bash(git reset --hard:*)",
      "Bash(sudo:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "WebFetch"
    ],
    "deny": [
      "Write(C:/Windows/**)",
      "Write(C:/Program Files/**)",
      "Write(../**)",
      "Read(**/*.key)",
      "Read(**/*.pem)",
      "Read(**/*.secret)",
      "Read(credentials/**)",
      "Read(config/private/**)",
      "Read(.env)",
      "Read(.env.*.local)"
    ]
  }
}
```
