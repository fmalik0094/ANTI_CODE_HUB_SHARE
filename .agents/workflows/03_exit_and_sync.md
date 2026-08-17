# WORKFLOW: 03_EXIT_AND_SYNC
## Multi-Engine Concurrency Guard
1. Before compiling state, check `.agents/states/_ACTIVE_INDEX.md` for a version newer than the one loaded at session start.
2. Reconcile against remote/parallel deltas before overwriting (Optimistic Version Locking).
3. Update `.state/DELTA_LOG.md`.
4. Execute `python validators/validate_structure.py`.
5. Run state harvester script (`python C:\01_LOCAL_CODING_F.M\TOPIC-HUB-ENGINE\multi_harvester.py`).
6. Commit changes to Git remote repository if initialized.
