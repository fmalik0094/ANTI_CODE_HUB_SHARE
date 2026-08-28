# EXECUTION INSTRUCTIONS: VS CODE METRIC LAYER

## 0. First Action, Every Session
Read `.agents/ORIENTATION.md` **at the repository root**
(`ANTI_CODE-HUB/.agents/ORIENTATION.md`, not `vscode/.agents/`) before anything
else. It is the single dense entry point — repository purpose, authoritative
vs. historical files, settled decisions, branch conventions, approval gates. Do
not re-derive workspace structure by exploring; if something isn't in
ORIENTATION.md, add it there rather than paying the rediscovery cost again next
session.

Claim `CDX-01` (permanent — scaffolding, diffs, terminal, git ops) or `CDX-02`
(parametric slot — specialization defined by the project's own registry, not
fixed here) from the repository-root `.agents/AGENT_REGISTRY.md`. One identity,
never both.

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
