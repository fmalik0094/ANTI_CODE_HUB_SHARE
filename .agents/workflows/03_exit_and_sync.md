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
4. Record commands, validations, and evidence in `.state/EXECUTION_LOG.md`. Never record credentials — use `[REDACTED]`.
5. Execute `python validators/validate_structure.py`.
6. Push the branch. Validation passing is not authorization to commit; committing is not authorization to merge to `main` or push to a remote — both require explicit operator approval.

## Note on TOPIC-HUB-ENGINE

`TOPIC-HUB-ENGINE/multi_harvester.py` aggregates state from all registered
project workspaces — this hub is one of its targets. It **pulls**; it is run
from its own repository on its own schedule. Do not invoke it from this
workflow: a routine exit step here would mean every hub session writes into a
separate project's directory. Keeping `.agents/states/_ACTIVE_INDEX.md` current
is this repository's only obligation to that system.
