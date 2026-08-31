# FM-NOTES — STATUS AND TRIAGE

**Read this before treating anything in this folder as current.**

These are the operator's own research and field manuals, written during the
**dual-IDE era** (Antigravity + VS Code, two engines). The workspace now runs a
**tri-engine** contract with Claude Code as a third engine, 3 permanent agents
plus 3 parametric slots, and branch-per-engine concurrency.

Measured on 2026-08-28: **14 of the 15 original files contain zero references
to Claude.** They pre-date the current architecture entirely.

Nothing here is authoritative. `.agents/ORIENTATION.md`,
`.agents/AGENT_REGISTRY.md`, `.agents/rules/global.md`, and `main.md` are. This
folder is retained as research and history, not as a source of current truth.

---

## Contains a factual error — correct before reuse

**`00.00-LEXICON.md`** has real reference value (per-file explanations of what
each config does and why), but its `.aiexclude` entry is wrong in a way the
current contract explicitly warns about. It claims:

> intercepted at the physical file-system layer by the local MCP server before
> any file read/write tool call is resolved … the MCP server aborts the action,
> returning an `IO_ACCESS_DENIED` error

`.aiexclude` does **not** do this. It is a context/ingestion filter, not an
enforcement boundary — it reduces what a model is shown, and denies nothing at
the tool-call layer. This is precisely the "configuration-as-security illusion"
described in `main.md` §5.5. The only enforced permission surface in this
repository is `.claude/settings.json`.

The same file also describes a Dual-IDE environment throughout and cites paths
under a `00-TEST-ONLY/` root that no longer exists.

---

## Historical — accurate for their era, superseded now

| File | What it is |
| :--- | :--- |
| `00-ANTI-CODE HUB.md` | Dual-IDE hub field manual |
| `00-ANTIGRAVITY.md` | Antigravity/Gemini field manual |
| `00-VSCODE.md` | VS Code/Codex field manual |
| `00-anticode-dual_ide_co_processing_manual.md` | Two-engine co-processing manual |
| `00-antigravity-state_manager_field_manual.md` | State-manager manual |
| `00-vscode-execution_core_field_manual.md` | Execution-core manual |
| `01_sidebyside comparaision_anti-vs.md` | Gemini vs. Codex comparison — still reasonable on those two engines, but has no third |

Their engine-role reasoning largely still holds. Their file topology, agent
counts, and concurrency model do not.

## Generation prompts — not documentation

| File | What it is |
| :--- | :--- |
| `02-NOTEBOOKLM-anti-code_hub.md` | Directive for NotebookLM to produce an audio overview |
| `02-NOTEBOOKLM-antigravity.md` | Same, Antigravity |
| `02-NOTEBOOKLM-vscode.md` | Same, VS Code |

These are inputs to a generator, not descriptions of the system. Reading them
as documentation will produce confident nonsense — they describe what a
narrator should *say*, in the dual-IDE era's terms.

## Templates — superseded by the live seed

| File | Status |
| :--- | :--- |
| `base_workspace_template.md` | Partially updated to the tri-engine contract |
| `anti-code hub-template.md` | Dual-IDE era |
| `antigravity-template.md` | Dual-IDE era |
| `vscode-template.md` | Dual-IDE era |

The authoritative template is the working directory `anti-code hub/`, not any
document here. A document describing a template drifts from the template; the
template itself cannot.

---

## If you update a file here

Add a status line at its top saying what era it describes and what supersedes
it, then update the row above. Do not silently modernize a historical document
— the record of what was believed at the time has its own value.
