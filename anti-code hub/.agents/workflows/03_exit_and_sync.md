# COMMAND: INITIATE FULL STATE SERIALIZATION & INDEX SYNC
# ENGINE: DETERMINISTIC_CONTEXT_SERIALIZATION
## DIRECTIVE
Confirm this session's work happened on its own branch (`gem/<work-item>`),
not directly on `main` — that is the actual concurrency control now, not a
markdown re-read. VS Code/Codex and Claude Code use their own `cdx/...` and
`cld/...` branches in parallel, so a shared ledger becomes a git merge instead
of a race. As a secondary check, also verify `.agents/states/_ACTIVE_INDEX.md`
has no version newer than the one loaded at session start; reconcile before
overwriting if it does. Then execute an immediate hard stop on active session
trajectories. Output exactly TWO distinct Markdown code blocks: Block 1 (State
Binary) and Block 2 (Registry Row). No other text.
## BLOCK 1: THE STATE BINARY
Compile the cumulative project timeline and architecture into a single copy-pasteable Markdown block:
1. **STATE HASH / DOMAIN:** [Increment current version number]
2. **GLOBAL OBJECTIVE:** [Immutable core goal]
3. **CUMULATIVE LOGIC & DECISION LEDGER:** [Aggregated list of all architectural decisions]
4. **CURRENT SESSION DELTA:** [Strict list of files changed and logic verified during this turn]
5. **ACTIVE CONSTRAINTS:** [Current boundaries and environment constraints]
6. **FAILURE MODES & RISKS:** [Unresolved edge cases or system discrepancies]
7. **NEXT EXECUTION NODE:** [The literal prompt text to resume the pipeline next session]
## BLOCK 2: THE REGISTRY ROW
Output a single Markdown table row:
| [Domain Name] | [Version] | [Current System Date/Time] | [Next Node Summary] | [Highest Priority Failure Mode] |
