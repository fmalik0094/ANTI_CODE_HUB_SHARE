# DECISION REGISTER: ANTI_CODE_HUB_SPEC_VAULT

Accepted architectural and policy decisions, newest last. Canonical — a
decision here is not relitigated without new evidence. `.agents/ORIENTATION.md`
§4 carries the short form for session boot; this file carries the reasoning.

- **ADR-0001:** Standardized under Anti-Code Hub Tier 1 Topology.

- **ADR-0002 (2026-08-27): Claude Code registered as a third engine.**
  The workspace ran two engines with governance describing a third that had no
  files anywhere. Claude Code registered with real permission enforcement via
  `.claude/settings.json`.

- **ADR-0003 (2026-08-27): One canonical agent registry.**
  Agent counts read 6, 10, and 13 simultaneously across `AGENT_REGISTRY.md`,
  `main.md`, and `agents/*/`. `.agents/AGENT_REGISTRY.md` is now sole authority;
  root `AGENTS.md` is a discovery stub; the 13 profile files are historical.

- **ADR-0004 (2026-08-27): Branch-per-engine-per-item concurrency.**
  "Re-read the shared index before writing" is a time-of-check/time-of-use
  race, not a lock. Work happens on `gem/<item>`, `cdx/<item>`, `cld/<item>`;
  git surfaces collisions as merge conflicts. The re-read remains a secondary
  freshness check. Validated in practice when two engines edited the same
  validator on separate branches and git raised the conflict.

- **ADR-0005 (2026-08-27): Enforcement and filtering are distinct layers.**
  `.claude/settings.json` denies at the tool-call layer. `.geminiignore` and
  `.aiexclude` only reduce what a model is shown. Documentation must name the
  mechanism behind any enforcement claim. `.vscode/settings.json`'s `autopilot`
  override was removed for contradicting `global.md`'s REQUEST REVIEW policy.

- **ADR-0006 (2026-08-27): Governance files are never hand-copied between
  repositories.** Copy-paste twice silently dropped security rules and replaced
  project-specific content with generic boilerplate. Generate from paths that
  exist in the target.

- **ADR-0007 (2026-08-28): 3 permanent agents + 3 parametric slots.**
  A fixed six-agent model forced one specialization per ID workspace-wide. The
  hub defined `GEM-02` as multimodal ingestion while `CNC/ROI_Analysis` used the
  same ID for financial evidence review — same identity, unrelated jobs,
  neither wrong. Slot `02` is now defined per project, with a required
  activation condition. No hub file may pin it.

- **ADR-0008 (2026-08-28): `anti-code hub/` is the single template; per-engine
  zones are deleted.** `antigravity/`, `vscode/`, and `claude/` carried private
  duplicates of `.agents/` and `.state/` — four drifting copies of the same
  governance, the mechanism behind nearly every defect found in the 2026-08
  audits. Verified they held nothing the seed lacked before deletion. Zones must
  not be recreated.

- **ADR-0009 (2026-08-28): Validators check truth, not existence.**
  Sixteen `.exists()` checks passed green while the repository contradicted
  itself in six documented ways. Validators now check semantic agreement, and a
  failing check names the specific contradiction. Staleness warns rather than
  fails, so an aging reference never blocks unrelated work.

- **ADR-0010 (2026-08-28): A command that reports success without working is
  removed, not left callable.** `hub_manager.py`'s `bundle` and `parse` printed
  "not implemented" and exited 0. Removed from the CLI so automation fails
  loudly instead of recording a phantom success.
