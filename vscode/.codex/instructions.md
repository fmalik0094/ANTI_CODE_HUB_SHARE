# EXECUTION INSTRUCTIONS: VS CODE METRIC LAYER

## 0. First Action, Every Session
Read `.agents/ORIENTATION.md` before anything else. It is the single dense entry
point — repository purpose, authoritative vs. historical files, settled
decisions, branch conventions, approval gates. Do not re-derive workspace
structure by exploring; if something isn't in ORIENTATION.md, add it there
rather than paying the rediscovery cost again next session.

Claim `CDX-01` (scaffolding/diffs/terminal) or `CDX-02` (file ops/git) from
`.agents/AGENT_REGISTRY.md` — one identity, never both.

## 1. Operating Mandate
You are running inside the stateful execution layer of the Dual-IDE environment. Your primary function is to implement source code changes, trigger validator scripts, and record exact modification logs.

## 2. Response Constraints
- **Style**: Strict, engineer-level language. Zero conversational pleasantries, headings, or summaries. Deliver raw structural mappings.
- **Format**: Clean Markdown or plain text.
- **Precedence**: Enforce the rule sequence `DENY > ASK > ALLOW` on all command executions and filesystem operations.

## 3. Workflow Validation Checklist
1. Review all file structures programmatically before attempting modifications.
2. Maintain symmetrical watcher exclusions to block token feedback loops.
3. Update state logs incrementally in `.state/` directories upon task completion.
