# Codex compatibility — seed contract and incident evidence

Current guidance verified: **2026-09-10**. Read on demand when changing Codex
configuration, validators, or propagation tooling. This portable record ships
with the seed; dated observations are not a promise about future runtimes.

## Current contract

The generic seed deliberately omits `approval_policy`. It retains
`sandbox_mode = "workspace-write"` and
`sandbox_workspace_write.network_access = false`. These are project defaults,
not immutable host policy. The validator accepts a narrow seed allowlist, not
every key in the vendor schema.
[Official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference),
checked 2026-09-10.

Explicit `approval_policy = "untrusted"` is retired. Omission inherits approval
behavior; `on-request` does not require approval for every sandbox-allowed
command. For stricter approval, the documented alternative is **user-level**
`projects.<project-path>.trust_level = "untrusted"` with no explicit approval
policy. Execution-policy allow rules can bypass prompts, and this trust setting
also disables project-local configuration. Explicit `on-request` overrides the
derived policy; managed `allowed_approval_policies` must permit `untrusted`.
This is not the retired configuration value.
[Official migration and approval guidance](https://learn.chatgpt.com/docs/agent-approvals-security),
checked 2026-09-10.

REQUEST REVIEW and DENY > ASK > ALLOW remain the operator's governance rules.
The seed alone does **not** guarantee per-command review or a command-name deny
list. If stronger enforcement is required, the operator must approve a host-level
policy and verify its effective behavior, including sandbox/network defaults
when project configuration is disabled. Never change user/managed settings just
to make a check green.

## Mastercam incident — 2026-09-09 (operator-supplied evidence)

> Template, validator, and tests agreed on a retired setting; runtime startup
> failed despite green governance checks.

During approved governance remediation in
`C:\01_LOCAL_CODING_F.M\CNC\mastercam`, the live Anti-Code seed was copied as a
reference. Its config, the inherited validator, and project tests required the
retired approval value. Governance validation (including the seed validator)
and all 29 project tests passed, but creating a Codex task failed:

```text
failed to resolve feature override precedence:
approval_policy = "untrusted" is no longer supported; remove this setting
```

The reported runtime was `codex-cli 0.153.4`. Removing the explicit override
while retaining workspace-write/network-off, updating the validator/tests, and
appending project records restored the CLI loader check; all 29 tests passed
again. A temporary retired-value CLI override reproduced exit 1.

Dated provenance: operator's incident report supplied for this hub task;
Mastercam branch `cdx/mastercam-governance-sync`, recorded base `8e85870`.
These are not assertions about its live branch today. This hub pass did not
modify Mastercam or independently rerun its 29 tests. Desktop task creation
after the correction remained **unverified** in that report.

## Verification procedure — distinct gates

From the seeded project root:

```text
python -B validators/validate_structure.py
python -B -m unittest discover -s validators -p test_validate_structure.py
python -B validators/check_codex_runtime.py
```

1. Structural: required paths exist.
2. Semantic: seed config defaults and existing governance checks agree.
3. Regression: temporary mutations are caught; this does not prove vendor support.
4. Runtime: the installed executable loads the actual seed values via temporary
   CLI overrides; retired-policy, invalid-sandbox and invalid-network controls
   must fail usefully. The latter two prove the serialized keys were consumed.
5. Desktop: operator creates a fresh task and confirms startup separately.

The runtime probe uses `features list`, not `--help`. It first runs in the
project directory, then passes TOML values read from the seed as explicit `-c`
arguments. Ambient user/managed configuration remains in place. It does not
edit configuration, launch an agent, or submit a model request. A passing ordinary
invocation does **not** prove that the project-local file was included; trust and
precedence can prevent inclusion. Nor does this probe exercise actual command
approval, sandbox isolation, or desktop startup.

### Hub verification — 2026-09-10

Baseline `main` / `origin/main`: `b85a6c157568db3bb41ecb1194d3332d2c36729b`.
Work branch: `cdx/codex-approval-compatibility` (local only).
Python: `3.14.4`. Runtime: `codex-cli 0.153.4`, resolved at
`C:\Users\fmalik\AppData\Local\OpenAI\Codex\bin\fd4c151a749f3ab4\codex.exe`.

Before correction, both root and seed validators passed. Explicitly supplying
the retired policy to `codex features list` failed with exit 1 and the removal
message. An ordinary invocation from the old seed directory returned 0 despite
the invalid file. A temporary CLI trust override for the hub also returned 0;
neither observation establishes project-file inclusion or its effective trust.

The first probe draft quoted CLI key names. An invalid-sandbox control exposed
that those keys were ignored (exit 0), so that draft's positive result was
discarded. The corrected probe uses unquoted dotted keys and tests both sandbox
and network parsing. Probe-serialization regressions prevent this false green.

Post-change results are recorded in the hub's `.state/EXECUTION_LOG.md` under
`CDX-01-20260910-CODEX-COMPAT-01`. Corrected values loaded with exit 0; the retired
approval value, invalid sandbox enum and invalid network type each failed with
exit 1 and named the offending setting. This proves CLI override parsing in the
ambient configuration, not inclusion of the seed's project-local file. Desktop
startup was **not exercised** in this pass.

## Reference inventory and propagation boundary

Corrected active surfaces: seed config and validator; new regression/runtime
checks; seed orientation, Codex instructions, and blueprint's Codex example;
hub orientation, manual, and README. The blueprint now routes to the real
config instead of generating unsupported tables.

Retired-value occurrences intentionally remain in rejection logic, negative
tests/probes, this incident, and dated change/decision/execution records. Valid
`trust_level = "untrusted"` guidance is retained. Older `FM-NOTES/`, `agents/`
profiles and the V1.1 state snapshot remain historical, not configuration
sources. Do not globally replace the word `untrusted` or rewrite old evidence.

No in-hub config generator or managed-content hash pin was found in the scoped
inventory. A read-only check of Topic Hub's
`tools/standardize_all_workspaces.py` found managed governance hashes but no
Codex config target/pin. This was not a workstation-wide launcher/profile scan;
other generators remain a rollout-inventory concern. No external pins changed.

Proposed separate rollout: inventory affected projects and config sources;
preview exact diffs preserving project policy; obtain pilot approval; update
one project and verify local tests, effective config loading and desktop startup;
expand only after explicit operator approval. Never blindly replace whole
governance files or treat validation as authorization to propagate.
