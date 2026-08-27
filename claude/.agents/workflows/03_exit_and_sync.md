# WORKFLOW: 03_EXIT_AND_SYNC
## Branch Discipline (Concurrency Control)
Work on a dedicated branch per work item (`cld/<item>`), not directly on
`main`. Antigravity and VS Code/Codex use their own `gem/...`/`cdx/...`
branches in parallel — this is the real concurrency control; re-reading the
index before writing is a secondary check, not the primary guard.
1. Confirm you are on your assigned `cld/...` branch, not `main`.
2. Re-read `.agents/states/_ACTIVE_INDEX.md` for a version newer than the one loaded at entry; reconcile before writing if one exists — never blind-overwrite a state binary.
3. Update `.state/DELTA_LOG.md`.
4. Execute `python ../validators/validate_structure.py`.
5. Run state harvester script (`python C:\01_LOCAL_CODING_F.M\TOPIC-HUB-ENGINE\multi_harvester.py`).
6. Push the branch. Merging to `main` and pushing to a remote both require explicit operator approval — neither is implied by validation passing.
