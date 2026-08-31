# ANTI_CODE_HUB_SPEC_VAULT V1.1

**STATE CHECKPOINT:** `ANTI_CODE_HUB_SPEC_VAULT-V1.1`
**DOMAIN STATUS:** GOVERNANCE ACTIVE — no application code runs from this repository
**WORKSPACE:** `C:\01_LOCAL_CODING_F.M\ANTI_CODE-HUB`
**SUPERSEDES:** V1.0 (2026-08-14)

## Global objective

Maintain the rulebook and project seed that govern the tri-engine workspace
contract (Antigravity/Gemini, VS Code/Codex, Claude Code) across the operator's
project portfolio. This repository ships no application code; `src/` is empty
by design.

## Cumulative decision ledger

See `.state/DECISIONS.md` for the full register. Standing decisions as of V1.1:

- 3 permanent agents (`GEM-01`, `CDX-01`, `CLD-01`) plus 3 parametric slots
  (`GEM-02`, `CDX-02`, `CLD-02`) whose specialization each project defines.
- `.agents/ORIENTATION.md` is the single entry point; all engine boot files
  route to it.
- Branch-per-engine-per-item (`gem/`, `cdx/`, `cld/`) is the concurrency
  control. Re-reading `_ACTIVE_INDEX.md` is a secondary freshness check.
- `.claude/settings.json` is the only enforced permission surface.
  `.geminiignore` and `.aiexclude` are context filters, not access denials.
- `anti-code hub/` is the single template. Per-engine zones are deleted and
  must not be recreated.
- Governance files are never hand-copied between repositories.

## Session delta (V1.0 → V1.1)

- Reconciled a three-way agent-count contradiction (6 / 10 / 13), then reduced
  the fixed model to 3 permanent + 3 parametric.
- Added `.agents/ORIENTATION.md` and routed all engine entry points to it.
- Removed the `autopilot` override contradicting `global.md`'s REQUEST REVIEW.
- Rewrote `.claude/settings.json` against paths that actually exist.
- Created `.state/EXECUTION_LOG.md` and root `.gitignore`.
- Brought `anti-code hub/` up to the full contract; smoke-tested instantiation.
- Added `.agents/resources/MODEL_REFERENCE.md` (hub and seed variants).
- Consolidated and deleted the `antigravity/`, `vscode/`, and `claude/` zones.
- Upgraded `validators/validate_structure.py` from existence checks to semantic
  checks; added boot-file and slot-pinning checks.
- Fixed `hub_manager.py` prune version sort (float comparison ranked V1.10
  below V1.9) and removed two commands that reported success without working.
- Rewrote `main.md` to match disk; triaged `FM-NOTES/` as historical.

## Active constraints

- Writes confined to the paths allowed in `.claude/settings.json`.
- Validation, commit, merge, and push are separate gates; none implies the next.
- One identity claimed per session, never two.

## Known open items

- `vscode/.codex/config.toml` declared keys absent from OpenAI's documented
  configuration reference. The file was not carried into the seed; a verified
  Codex configuration still needs authoring against the live reference.
- `hub_manager.py` prune version-sort fix was exercised end to end during this
  checkpoint: it correctly kept V1.1 and archived V1.0, leaving no dangling
  index reference. The V1.10-vs-V1.9 ordering path itself is verified by
  reasoning, not by a run against a domain that has actually reached V1.10.
- 25 sibling projects still carry the legacy fixed-six registry. Deferred to a
  separate fleet-governance effort.

## Next execution node

Author a verified Codex configuration for the seed, or begin the separate
fleet-governance workstream.
