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
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Entry / inventory | Read AGENTS, orientation, registry, global rules, lifecycle workflows, active index/state and all root ledgers; searched for claim/handoff records and config/policy/validator/generator/hash references with `rg` | Complete | No claim/handoff ledger found. Current config, validator, orientations, main/README and seed blueprint needed correction; history/profiles/FM-NOTES classified separately. Topic Hub standardizer read-only inspection: managed governance hashes, no Codex config target/pin |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Baseline | `git status --short --branch`; `git rev-parse main origin/main`; `git log -1 --format="%H %s"`; `Get-FileHash .claude/settings.local.json -Algorithm SHA256` | Confirmed | Both refs at `b85a6c157568db3bb41ecb1194d3332d2c36729b`; no tracked edits. Unrelated untracked local settings SHA256 `1EE2693C0EA200C62A47EAD8950F47AFC147E29B00C737891CBEFCD53EFFDA51`; preserved |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Baseline checks | `python validators/validate_structure.py`; `python "anti-code hub/validators/validate_structure.py"`; `python --version`; `codex --version` | Both validators exit 0 | Python 3.14.4, codex-cli 0.153.4. Seed had expected genesis warnings. Passing validators still required the retired setting |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Branch | `git switch -c cdx/codex-approval-compatibility` | Success after tool escalation | First attempt denied by protected Git directory; same scoped command succeeded through approved tool escalation. No staging/commit/merge/push |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Official references | Reopened `https://learn.chatgpt.com/docs/config-file/config-reference` and `https://learn.chatgpt.com/docs/agent-approvals-security` | Verified 2026-09-10 | Explicit untrusted approval retired; omission migration and distinct user-level project-trust tradeoffs recorded with source links in compatibility resource |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Pre-change runtime | `codex -c 'approval_policy="untrusted"' features list`; `codex features list` from seed directory | Expected rejection exit 1; ordinary check exit 0 | Removal message reproduced. Ordinary success despite invalid seed does not prove project-file inclusion. A temporary hub trust override also returned 0 without proving inclusion; no persistent trust/config edits |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Mutation | Applied scoped patches to seed config, validator, two new probes/tests, portable compatibility record, seed orientation/instructions/blueprint, hub orientation/manual/README/CHANGELOG and three root ledgers | Local, unstaged | ADR-0011; sandbox/network preserved, approval override omitted. No application, registry, baseline/checkpoint, global user configuration or external repository edits |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Probe self-check | `python -B "anti-code hub/validators/check_codex_runtime.py"` during development | Initial positive result discarded | An invalid sandbox sentinel unexpectedly returned 0 because the draft quoted CLI keys. Changed serializer to unquoted dotted keys; added serialization regressions and independent invalid-sandbox/invalid-network controls |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Structural / semantic | `python -B validators/validate_structure.py`; `python -B "anti-code hub/validators/validate_structure.py"` | Both exit 0 | Required paths and semantic contract passed; seed genesis placeholders warn as expected. These checks are not runtime proof |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Regression | `python -B -m unittest discover -s "anti-code hub/validators" -p test_validate_structure.py -v` | 24 tests passed, exit 0 | Correct seed, retired/other/profile overrides, unsupported keys, sandbox/network weakening, JSON/TOML errors, boot routing, registry, permission paths, existing approval gates, missing tomllib fallback and CLI serialization covered. Fixtures copy only required governance files into temporary directories |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Final runtime probe | `python -B "anti-code hub/validators/check_codex_runtime.py"` | Probe exit 0 | Codex 0.153.4: version/ordinary loader/corrected override values exit 0. Invalid sandbox enum, invalid network type and retired approval each exit 1 with useful messages. Source values exercised through CLI override layer over ambient user/managed defaults; no persistent settings edited |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Evidence boundary | Recorded operator-supplied Mastercam 2026-09-09 incident and local results separately | Desktop startup NOT EXERCISED | No claim of seed project-layer inclusion, effective command approval or sandbox isolation from CLI listing. Mastercam's reported 29 tests were not rerun here. No rollout performed; inventory/preview/pilot/runtime proof/operator approval proposed separately |
| 2026-09-10 | CDX-01-20260910-CODEX-COMPAT-01 | Final review | Re-ran both validators, 24 tests and runtime probe; `git diff --check`; `git diff --cached --name-only`; `git status --short --branch`; `git rev-parse HEAD main origin/main`; local-settings SHA256 recheck | All checks passed within stated limits | No staged files. HEAD/main/origin unchanged at `b85a6c157568db3bb41ecb1194d3332d2c36729b`; 12 tracked edits + 3 new task files, all unstaged. Unrelated local-settings hash unchanged. Sandbox Git-ignore read warnings did not affect checks; no global config change attempted |

## CDX-01-20260910-CODEX-COMPAT-01 — review manifest

Workspace: `C:\01_LOCAL_CODING_F.M\ANTI_CODE-HUB`.
Branch: `cdx/codex-approval-compatibility` (no upstream).
HEAD: `b85a6c157568db3bb41ecb1194d3332d2c36729b`.
All paths below are relative to this workspace. No task file is staged.

| Changed file | Working-tree status |
| :--- | :--- |
| `.agents/ORIENTATION.md` | Modified |
| `.state/DECISIONS.md` | Appended ADR-0011 |
| `.state/DELTA_LOG.md` | Appended |
| `.state/EXECUTION_LOG.md` | Appended evidence and manifest |
| `CHANGELOG.md` | Added unreleased entry; history preserved |
| `README.md` | Modified current guidance |
| `main.md` | Modified Codex posture claims |
| `anti-code hub/.agents/ORIENTATION.md` | Modified |
| `anti-code hub/.agents/rules/base_workspace_template.md` | Removed unsupported Codex example; routes to seed |
| `anti-code hub/.codex/config.toml` | Removed explicit approval override |
| `anti-code hub/.codex/instructions.md` | Added compatibility guidance |
| `anti-code hub/validators/validate_structure.py` | Updated seed contract checks |
| `anti-code hub/.agents/resources/CODEX_COMPATIBILITY.md` | New, untracked |
| `anti-code hub/validators/test_validate_structure.py` | New, untracked |
| `anti-code hub/validators/check_codex_runtime.py` | New, untracked |

Pre-existing `.claude/settings.local.json` remains untracked and unchanged;
it is not part of this change set. Commit, merge, push, desktop retry, global
policy changes and cross-workspace rollout remain separate operator actions.

## CDX-01-20260910-SEED-STATUS-02 — approved follow-up entry

- Identity: CDX-01; started 2026-09-10T20:49:11Z; status ACTIVE.
- User approved the proposed incomplete-verification repair, current publication
  evidence and private draft PR, with a Gemini continuation prompt.
- Scope: seed validator/result tests, current validation guidance, append-only
  ledgers and a new handoff. No sandbox/approval/configuration changes.
- Rechecked clean cdx/codex-approval-compatibility at
  44eb18a44fda1fe9908c25e3e88eb0724cfae726; private origin branch matches.
  Local/remote main remain b85a6c157568db3bb41ecb1194d3332d2c36729b.
- Earlier entries describing uncommitted work are dated history, not the current
  publication state. The 15-file commit already existed before this follow-up.
- No merge, public share push, history rewrite, global setting change, live
  harvest, cross-workspace propagation or application operation is authorized.
- Subagents review read-only beneath this identity. Exact allowlist staging only;
  local settings, baselines, decisions and source-state snapshots are preserved.

### Implementation and verification

- apply_patch changed only the approved seed validator/result tests, current
  validation guidance, handoff and append-only evidence. Existing seed config
  remains workspace-write/network-off with no explicit approval policy.
- Seed validator: missing TOML check reports UNVERIFIED/2; known errors still
  produce FAIL/1 first; other implemented checks run before either result.
- Parent regression run: 29/29 PASS (1.210s); root/seed validators report success.
- Independent review: 29/29 PASS, no skips (1.190s), Python 3.14.4. Separate
  synthetic matrix reproduced 0 verified, 2 missing parser, 1 missing parser
  with broken boot/missing config, then 0 on parser restoration. Fixture bytes
  unchanged in each case; seven watched source/config hashes unchanged.
- Missing-parser evidence uses a mock, not an actual older Python installation.
  Runtime prober/config were not changed or executed in this follow-up. Existing
  0.153.4 runtime records remain dated evidence; loading/enforcement/desktop
  behavior stay UNVERIFIED.
- Public share is confirmed public, private origin confirmed private. Publication
  will target only the existing private review branch and a draft PR against main.
- Gemini receives a review-only handoff. No merge, public release, project
  template propagation, global trust changes or application execution authorized.

### Publication and exit — 2026-09-10T20:57:57Z

- Final parent rerun: 29/29 PASS (1.222s); root validator exit 0; seed validator
  exit 0 with three expected generic placeholder warnings and scoped success.
- Independent eleven-file text review found no blocker or high-confidence
  credential-pattern match. Protected baseline/decision/state/policy paths have
  no diff against the pre-follow-up HEAD. Local-only settings were never staged.
- Exact eleven-file allowlist committed as
  59043e08999eefb03d03de209cd8148e05fc55f1 and pushed only to private origin's
  cdx/codex-approval-compatibility. Existing commit 44eb18a was not duplicated.
- Private draft PR #1 verified OPEN/draft, base main, matching review head,
  sixteen cumulative files. Private origin/main b85a6c1 and public share/main
  e106410 unchanged; no public compatibility branch appeared.
- Documentation-only publication receipt follows; no source/config changes.
- Status: COMPLETE_REVIEW_PUBLISHED. CDX-01 ownership released. GEM-01 handoff
  is review-only. No merge, public release, propagation or automatic continuation.
