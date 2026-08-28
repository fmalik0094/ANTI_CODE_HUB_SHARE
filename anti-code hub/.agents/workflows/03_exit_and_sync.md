# WORKFLOW: 03_EXIT_AND_SYNC

## Branch discipline (concurrency control)
Work happens on a dedicated branch per engine per work item (`gem/<item>`,
`cdx/<item>`, `cld/<item>`), never on `main`. This is the actual concurrency
control — two engines writing the same file becomes a git merge instead of a
silent overwrite.

1. Confirm you are on your assigned branch, not `main`.
2. Record what changed in `.state/DELTA_LOG.md`.
3. Record commands/validations in `.state/EXECUTION_LOG.md`. Never record
   credentials — use `[REDACTED]`.
4. If a decision was accepted this session, append it to `.state/DECISIONS.md`.
5. If you discovered something non-obvious, add it to `.agents/ORIENTATION.md`
   so the next session doesn't pay the same rediscovery cost.
6. Run `python validators/validate_structure.py`.
7. **Approval gates — none implied by the previous:** validation passing does
   not authorize a commit; committing does not authorize a merge to `main`;
   merging does not authorize a push. Each needs the operator to say so.
