# MODEL REFERENCE — VERIFY BEFORE DECIDING

Purpose: compact orientation for agents that must compare API model families or
write an exact API model ID. This is not an exhaustive catalog and is not loaded
for unrelated work.

Model catalogs, prices, limits, aliases, and availability change. The official
vendor pages below override every local value. Recheck the relevant section when
its verification date is older than 60 days or when a decision depends on an
exact number.

## Authoritative live sources

Verified: 2026-08-27. Each URL resolved on that date.

| Vendor | API docs | Tool docs |
| :--- | :--- | :--- |
| Anthropic | https://platform.claude.com/docs/en/home | https://code.claude.com/docs/en/overview |
| OpenAI | https://developers.openai.com/api/docs | https://developers.openai.com/learn/codex and https://learn.chatgpt.com/docs |
| Google | https://ai.google.dev/gemini-api/docs | https://antigravity.google/docs/home |

| Vendor | Models | Pricing |
| :--- | :--- | :--- |
| Anthropic | https://platform.claude.com/docs/en/about-claude/models/overview | https://platform.claude.com/docs/en/about-claude/pricing |
| OpenAI | https://developers.openai.com/api/docs/models | https://developers.openai.com/api/docs/pricing |
| Google | https://ai.google.dev/gemini-api/docs/models | https://ai.google.dev/gemini-api/docs/pricing |

## Anthropic API snapshot

Last verified: 2026-08-27 against Claude Platform documentation.

Standard first-party API text-token prices are USD per 1M tokens. Provider,
batch, caching, fast-mode, and data-residency prices can differ.

| Tier | API model ID | Input limit | Max output | Input | Output |
| :--- | :--- | ---: | ---: | ---: | ---: |
| Complex agentic work | `claude-opus-5` | 1M | 128K | $5.00 | $25.00 |
| Speed/intelligence balance | `claude-sonnet-5` | 1M | 128K | $2.00 | $10.00 |
| Cost-sensitive throughput | `claude-haiku-4-5-20251001` | 200K | 64K | $1.00 | $5.00 |

Notes:

- Anthropic states that Claude Sonnet 5's $2.00 / $10.00 pricing is standard
  and that the previously scheduled 2026-09-01 increase to $3.00 / $15.00
  will not occur:
  https://platform.claude.com/docs/en/about-claude/pricing
- `claude-haiku-4-5` is a convenience alias; the dated ID above is the pinned
  Claude API snapshot. Anthropic states that pre-4.6 canonical IDs include a
  snapshot date:
  https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
- Dateless Claude 4.6-and-later IDs such as `claude-opus-5` are pinned model
  IDs, not evergreen aliases.
- Do not hard-code a default tier here. Select against task quality, latency,
  cost, tool, and account-availability requirements.

## OpenAI API snapshot

Last verified: 2026-08-27 against official OpenAI documentation.

Standard text-token prices are USD per 1M tokens. Cached input, Batch API,
long-input, tool-call, and other modality charges are excluded here.

| Tier | API model ID | Context | Max output | Input | Output |
| :--- | :--- | ---: | ---: | ---: | ---: |
| Frontier | `gpt-5.6-sol` | 1.05M | 128K | $4.00* | $20.00* |
| Balanced | `gpt-5.6-terra` | 1.05M | 128K | $2.00 | $12.00 |
| Cost-sensitive | `gpt-5.6-luna` | 1.05M | 128K | $0.20 | $1.20 |

Notes:

- \* OpenAI documents GPT-5.6 Sol's $4.00 / $20.00 pricing as promotional
  through at least 2026-11-21; prompts over 272K input tokens use a 2x input
  and 1.5x output multiplier:
  https://developers.openai.com/api/docs/models/gpt-5.6-sol
- `gpt-5.6` currently aliases `gpt-5.6-sol`; use the exact model ID when a
  stable explicit choice matters.
- API catalog availability does not prove that the same model is selectable in
  Codex, ChatGPT, or a particular account. Check the active product/runtime.

## Google Gemini API snapshot

Last verified: 2026-08-27 against Google AI for Developers documentation.

Standard paid-tier text-token prices are USD per 1M tokens. Batch, Flex,
Priority, caching, grounding, and non-text charges are excluded here.

| Tier | API model ID | Input limit | Max output | Input | Output |
| :--- | :--- | ---: | ---: | ---: | ---: |
| Pro preview | `gemini-3.1-pro-preview` | 1,048,576 | 65,536 | $2.00 <=200K; $4.00 >200K | $12.00 <=200K; $18.00 >200K |
| Stable Flash | `gemini-3.7-flash` | 1,048,576 | 65,536 | $0.75* | $3.75* |
| Stable Flash-Lite | `gemini-3.5-flash-lite` | 1,048,576 | 65,536 | $0.30 | $2.50 |

\* Gemini 3.7 Flash promotional Standard pricing is documented through
2026-12-31; Google lists $1.50 input and $7.50 output starting 2027-01-01.

Notes:

- Preview models can have tighter limits and shorter deprecation notice than
  stable models; verify lifecycle status before production selection.
- Gemini API availability does not prove that Antigravity exposes the same
  endpoint or configuration. Check the active product/runtime.

## Google toolchain status

Verified: 2026-08-27.

Antigravity CLI is the current general Google coding-agent CLI. Google states
that consumer Gemini CLI and Gemini Code Assist stopped serving free, Pro, and
Ultra requests on 2026-06-18; API-key and enterprise Gemini CLI access remains.

Sources:

- https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- https://antigravity.google/docs/home

## Cross-vendor terminology

Verified: 2026-08-27. Terms only; no inferred equivalents.

| Concept | Anthropic / Claude Code | OpenAI / Codex | Google / Antigravity |
| :--- | :--- | :--- | :--- |
| MCP (Model Context Protocol) | Model Context Protocol (MCP) | Model Context Protocol (MCP) | Model Context Protocol (MCP) |
| Connector / MCP server | MCP connector / MCP server | connector / MCP server | MCP server |
| Function calling / tool use | tool use / function calling | function calling / tools | function calling / tools |
| Skill | Skill | Skill | Agent Skill |
| Plugin | Plugin | Plugin | Plugin |
| Agent / agentic loop | agent / agentic loop | agent / agentic workflow | agent / agent loop |
| System prompt / context window | system prompt / context window | system message / context window | system instruction / context window |
| RAG (Retrieval-Augmented Generation) | RAG (Retrieval augmented generation) | retrieval-augmented generation (RAG) | Retrieval Augmented Generation (RAG) |
| Embeddings / vector store | embeddings / vector database | embeddings / vector store | embeddings / vector database |

Manufacturer terminology sources:

- Anthropic / Claude Code:
  https://code.claude.com/docs/en/features-overview,
  https://code.claude.com/docs/en/agent-sdk/agent-loop,
  https://platform.claude.com/docs/en/agents-and-tools/mcp-connector,
  https://platform.claude.com/docs/en/about-claude/glossary,
  https://platform.claude.com/docs/en/build-with-claude/context-windows,
  https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide
- OpenAI / Codex:
  https://learn.chatgpt.com/docs/extend/mcp,
  https://learn.chatgpt.com/docs/build-skills,
  https://learn.chatgpt.com/docs/build-plugins,
  https://developers.openai.com/api/reference/resources/responses/methods/create,
  https://developers.openai.com/api/reference/resources/vector_stores/methods/search,
  https://developers.openai.com/api/docs/guides/embeddings
- Google / Antigravity:
  https://antigravity.google/docs/mcp,
  https://antigravity.google/docs/skills,
  https://antigravity.google/docs/plugins,
  https://antigravity.google/docs/subagents,
  https://antigravity.google/product/antigravity-sdk,
  https://ai.google.dev/gemini-api/docs/function-calling,
  https://ai.google.dev/gemini-api/docs/tokens,
  https://ai.google.dev/gemini-api/docs/embeddings

## Token and freshness discipline

1. Do not preload this file for unrelated repository work.
2. Read only the relevant vendor section, then open the smallest official page
   that answers the task.
3. For recommendations, migrations, budgets, or production configuration,
   cite the live page and state its verification date.
4. Never treat a marketing model name as an API ID.
5. Never infer product entitlements, rate limits, or regional availability from
   this snapshot.
6. If temporary offline grep is necessary, place targeted vendor pages under
   `docs-cache/<vendor>/` with a retrieval-date manifest. `docs-cache/` is
   intentionally Git-ignored and must not become template payload.
