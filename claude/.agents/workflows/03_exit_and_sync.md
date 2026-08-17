# WORKFLOW: 03_EXIT_AND_SYNC
1. Before writing, re-read `.agents/states/_ACTIVE_INDEX.md` for a version newer than the one loaded at entry. If Antigravity or VS Code/Codex wrote a newer version during this session, reconcile deltas before proceeding — never blind-overwrite a state binary.
2. Update `.state/DELTA_LOG.md`.
3. Execute `python ../validators/validate_structure.py`.
4. Run state harvester script (`python C:\01_LOCAL_CODING_F.M\TOPIC-HUB-ENGINE\multi_harvester.py`).
5. Commit changes to Git remote repository if initialized.
