# WORKFLOW: 03_EXIT_AND_SYNC
## Branch Discipline (Concurrency Control)
Work happens on a dedicated branch per engine per work item (`gem/<item>`,
`cdx/<item>`, `cld/<item>`), not directly on `main`. This is the actual
concurrency control — two engines racing to write `.agents/states/` becomes a
normal git merge instead of a silent overwrite. The old "re-read the index
before writing" discipline is a secondary check, not the primary guard.
1. Confirm you are on your assigned branch, not `main`.
2. Re-read `.agents/states/_ACTIVE_INDEX.md` for a version newer than the one loaded at session start; reconcile before writing if one exists.
3. Update `.state/DELTA_LOG.md` with this session's changes.
4. Execute `python validators/validate_structure.py`.
5. Run state harvester script (`python C:\01_LOCAL_CODING_F.M\TOPIC-HUB-ENGINE\multi_harvester.py`).
6. Push the branch. Validation passing is not authorization to commit; committing is not authorization to merge to `main` or push to a remote — both require explicit operator approval.
