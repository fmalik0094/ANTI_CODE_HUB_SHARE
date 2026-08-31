# EXECUTION LOG: ANTI_CODE_HUB_SPEC_VAULT

Reproducible record of commands, mutations, validations, and handoffs, per
`.agents/rules/global.md`'s Audit Trail requirement. Distinct from
`DELTA_LOG.md` (material repository changes) and `DECISIONS.md` (accepted
architectural decisions) — this file is the command/action/evidence trail.

Never record API keys, tokens, passwords, or restricted source content here —
use `[REDACTED]` and record only credential state.

| Timestamp | Agent ID | Operation | Command / Action | Exit Status | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-01 | Baseline | Read canonical boot files; verified clean target branch; ran structural validator | Success | `cdx/model-docs-reference`; validator passed before mutation |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-01 | Research | Verified current API model IDs, context/output limits, pricing, and lifecycle notes against official Anthropic, OpenAI, and Google documentation | Success | Live sources recorded in `.agents/resources/MODEL_REFERENCE.md` |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-01 | Mutation | Added on-demand model reference, global discovery rule, source-contract validation, ignored cache path, and delta record | Success | Working-tree diff on `cdx/model-docs-reference` |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-01 | Validation | Ran `python validators/validate_structure.py`, `python -m py_compile validators/validate_structure.py`, and `git diff --check` | Success | Semantic validation, Python compilation, and whitespace checks passed |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-02 | Commit | Committed the completed initial reference pass before further branch work | Success | Commit `74ca27c`; no merge or push |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-02 | Research | Reverified pricing, model-ID rules, tool-doc entry points, Google CLI transition, and cross-vendor terminology against current manufacturer documentation | Success | Official source URLs and verification dates recorded in `.agents/resources/MODEL_REFERENCE.md` |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-02 | Mutation | Added tool-doc and terminology resources, corrected time-sensitive pricing treatment, and implemented non-blocking reference-staleness warnings | Success | Uncommitted correction-pass diff on `cdx/model-docs-reference` |
| 2026-08-27 | CDX-01-20260827-MODEL-DOCS-02 | Validation | Ran the structure validator, Python compilation, whitespace checks, and a deterministic stale-date warning test | Success | Validator passed; stale dates produce warning data without a failure path |
| 2026-08-28 | CDX-01-20260828-MAIN-MD-01 | Baseline | Read canonical orientation; verified `main` at `9c15daf`; created `cdx/main-md-rewrite`; preserved unrelated untracked `.claude/settings.local.json` | Success | Work isolated from `main`; no merge or push |
| 2026-08-28 | CDX-01-20260828-MAIN-MD-01 | Research | Generated a live directory tree, compared all zone files with the seed, checked engine boot routing and manager stubs, and verified Codex configuration support against official OpenAI documentation | Success | On-disk topology and manufacturer configuration reference |
| 2026-08-28 | CDX-01-20260828-MAIN-MD-01 | Mutation | Rewrote `main.md` to match current topology, identities, lifecycle, enforcement, failure modes, and pending zone consolidation; removed three obsolete seed placeholder files | Success | Working-tree diff on `cdx/main-md-rewrite` |
| 2026-08-28 | CDX-01-20260828-MAIN-MD-01 | Validation | Ran root and seed structural validators and verified every repository path named in `main.md` exists | Success | Root passed; seed passed with expected genesis-placeholder warnings; named-path check passed |
| 2026-08-31 | CDX-01-20260831-CODEX-CONFIG-01 | Baseline | Read canonical orientation; verified `main` at `3e3c91c`; created `cdx/codex-config`; preserved unrelated untracked `.claude/settings.local.json` | Success | Work isolated from `main`; no merge or push |
| 2026-08-31 | CDX-01-20260831-CODEX-CONFIG-01 | Research | Verified project config loading, approval policies, sandbox modes, and workspace-write network control against official OpenAI documentation | Success | `https://developers.openai.com/codex/config-reference` and linked approval/security guidance |
| 2026-08-31 | CDX-01-20260831-CODEX-CONFIG-01 | Mutation | Added the supported seed `.codex/config.toml`; extended the seed validator with strict TOML schema/posture checks; updated canonical orientation and `main.md` enforcement claims | Success | Working-tree diff on `cdx/codex-config` |
| 2026-08-31 | CDX-01-20260831-CODEX-CONFIG-01 | Validation | Ran root and seed validators, whitespace checks, and deterministic positive/negative Codex-config checks | Success | Both validators passed; expected seed genesis warnings only; unknown keys and enabled command network were rejected |
