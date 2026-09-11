# DELTA LOG: ANTI_CODE_HUB_SPEC_VAULT
- Initialized Anti-Code Hub governance remediation.
- 2026-08-27: Added a compact, on-demand tri-vendor API model reference under `.agents/resources/`; linked it from the canonical global rules, added source-contract validation, and reserved Git-ignored `docs-cache/` for optional targeted offline snapshots.
- 2026-08-27: Extended the model reference with official tool-documentation entry points, manufacturer-only terminology, temporary-pricing annotations, Claude model-ID evidence, and current Antigravity CLI status; added non-blocking 60-day staleness warnings.
- 2026-08-28: Rewrote `main.md` from the live repository topology and canonical 3-permanent-plus-3-parametric contract; removed false squad, automatic-validation, optimistic-concurrency, hard-filter, and Codex-command-enforcement claims; deleted three obsolete seed `.gitkeep` placeholders beside real files.
- 2026-08-31: Added a manufacturer-verified seed Codex configuration using `approval_policy = "untrusted"`, `sandbox_mode = "workspace-write"`, and disabled command-spawned network access; added strict TOML key/value validation and documented that Codex has no general per-command deny-list setting.
- 2026-09-10 — CDX-01-20260910-CODEX-COMPAT-01: Superseded the retired explicit approval default without rewriting prior history. Updated `anti-code hub/.codex/config.toml`, its validator, seed orientation/Codex instructions/blueprint, root orientation/manual/README/CHANGELOG, and this session's decision/execution records. Added the portable `anti-code hub/.agents/resources/CODEX_COMPATIBILITY.md` incident, `validators/test_validate_structure.py` (24 tests) and `validators/check_codex_runtime.py` under the seed. Approvals now inherit app/user/managed policy; workspace-write/network-off remain. Root and seed structural/semantic checks and regression tests passed. Codex 0.153.4 accepted the corrected values through explicit CLI overrides; retired policy and invalid sandbox/network controls each failed. Project-file inclusion, effective command enforcement and desktop startup are not claimed. A quoted-key false-positive in the first probe was caught, corrected and recorded. No commit, merge, push, user-config change or cross-project propagation; unrelated `.claude/settings.local.json` preserved.

## 2026-09-10 — CDX-01-20260910-SEED-STATUS-02

Operator-approved follow-up fixes the seed validator's incomplete-verification
result, without changing its configuration or project permission defaults.
Missing TOML support now returns UNVERIFIED/2 after other checks continue;
confirmed failures retain exit 1 precedence and success is scoped to implemented
static checks. Five new regressions raise the suite from 24 to 29 tests.

Prior compatibility commit 44eb18a44fda1fe9908c25e3e88eb0724cfae726 was already
present and verified on the private origin branch before this follow-up. Earlier
entries reporting uncommitted work remain historical evidence. Root/seed
validators and 29 tests pass on Python 3.14.4; an independent synthetic matrix
confirmed 0/1/2 behavior and input-byte preservation. No actual old-Python runtime
or desktop enforcement certification is claimed.

Current validation guidance and a GEM-01 independent-review handoff were added.
Private draft publication is approved; merge, public share, global settings,
cross-workspace rollout and live harvest remain blocked. Baselines, decisions,
state snapshots, permission files, local settings and other repositories remain
unchanged. Final publication receipt follows after remote verification.

Publication verified: private draft PR #1 at
https://github.com/fmalik0094/ANTI_CODE_HUB/pull/1 is OPEN/draft against main.
Repair checkpoint 59043e08999eefb03d03de209cd8148e05fc55f1 matched local,
origin and PR heads. Main remains b85a6c1; public share remains e106410.
CDX-01 released ownership; Gemini receives read-only review, not release authority.
