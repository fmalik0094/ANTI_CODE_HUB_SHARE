# Claude Code Project Initialization Sequence

When invoked in this workspace:
1. **Security Verification:** Confirm `.claude/settings.json` is loaded and active.
2. **Context Intake:** Read `.agents/rules/global.md`, `.state/BASELINE.md`, and `.agents/states/_ACTIVE_INDEX.md`.
3. **Role Assignment:** Claim `CLD-01` (Deep Refactorer) or `CLD-02` (QA Validator) from `AGENTS.md`.
4. **Planning Protocol:** Propose an action plan and halt on `[PENDING OPERATOR APPROVAL]` prior to mutating source code.
5. **Session Close:** Execute `03_exit_and_sync.md` with optimistic state reconciliation.
