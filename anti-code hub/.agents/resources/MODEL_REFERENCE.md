# MODEL REFERENCE — VERIFY BEFORE DECIDING

Compact orientation for agents that must compare model families or write an
exact API model ID. Read on demand for model/API work only; do not preload it
for unrelated tasks.

**This seed copy deliberately carries no pricing or model-ID tables.** Those
change every few months, and a snapshot inherited at project creation would be
stale before the project's first real session — presented with the authority of
a committed file. Fetch current numbers from the live pages below and record
them here, with a verification date, only if this project actually needs them
pinned.

## Authoritative live sources

These URLs are stable; the content behind them is not.

| Vendor | API docs | Tool / agent docs |
| :--- | :--- | :--- |
| Anthropic | https://platform.claude.com/docs/en/home | https://code.claude.com/docs/en/overview |
| OpenAI | https://developers.openai.com/api/docs | https://developers.openai.com/learn/codex · https://learn.chatgpt.com/docs |
| Google | https://ai.google.dev/gemini-api/docs | https://antigravity.google/docs/home |

| Vendor | Models | Pricing |
| :--- | :--- | :--- |
| Anthropic | https://platform.claude.com/docs/en/about-claude/models/overview | https://platform.claude.com/docs/en/about-claude/pricing |
| OpenAI | https://developers.openai.com/api/docs/models | https://developers.openai.com/api/docs/pricing |
| Google | https://ai.google.dev/gemini-api/docs/models | https://ai.google.dev/gemini-api/docs/pricing |

API docs are for *building things that call these APIs*. Tool docs are for
*using the engines this workspace runs on* — for agent-behavior questions, the
tool docs are usually the right half.

## Cross-vendor terminology

Terms only, taken from each manufacturer's own documentation. No inferred
equivalents — where a vendor has no equivalent, that is recorded rather than
mapped loosely.

| Concept | Anthropic / Claude Code | OpenAI / Codex | Google / Antigravity |
| :--- | :--- | :--- | :--- |
| MCP (Model Context Protocol) | Model Context Protocol (MCP) | Model Context Protocol (MCP) | Model Context Protocol (MCP) |
| Connector / MCP server | MCP connector / MCP server | connector / MCP server | MCP server |
| Function calling / tool use | tool use / function calling | function calling / tools | function calling / tools |
| Skill | Skill | Skill | Agent Skill |
| Plugin | Plugin | Plugin | Plugin |
| Agent / agentic loop | agent / agentic loop | agent / agentic workflow | agent / agent loop |
| System prompt / context window | system prompt / context window | system message / context window | system instruction / context window |
| RAG | RAG (Retrieval augmented generation) | retrieval-augmented generation (RAG) | Retrieval Augmented Generation (RAG) |
| Embeddings / vector store | embeddings / vector database | embeddings / vector store | embeddings / vector database |

Terminology verified 2026-08-27 against manufacturer documentation. Terms drift
more slowly than prices, but they do drift — treat a table older than a year as
suspect.

## Discipline

1. Do not preload this file for unrelated repository work.
2. Read only the relevant vendor section, then open the smallest official page
   that answers the task.
3. For recommendations, migrations, budgets, or production configuration, cite
   the live page and state its verification date.
4. Never treat a marketing model name as an API ID.
5. Never infer entitlements, rate limits, or regional availability from any
   local snapshot.
6. If offline grep is genuinely necessary, place targeted vendor pages under
   `docs-cache/<vendor>/` with a retrieval-date manifest. `docs-cache/` is
   Git-ignored on purpose and must never become committed payload.
