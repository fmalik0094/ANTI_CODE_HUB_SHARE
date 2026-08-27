# MODEL REFERENCE — VERIFY BEFORE DECIDING

Purpose: compact orientation for agents that must compare API model families or
write an exact API model ID. This is not an exhaustive catalog and is not loaded
for unrelated work.

Model catalogs, prices, limits, aliases, and availability change. The official
vendor pages below override every local value. Recheck the relevant section when
its verification date is older than 60 days or when a decision depends on an
exact number.

## Authoritative live sources

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

- `claude-haiku-4-5` is a convenience alias; the dated ID above is the pinned
  Claude API snapshot.
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
| Frontier | `gpt-5.6-sol` | 1.05M | 128K | $4.00 | $20.00 |
| Balanced | `gpt-5.6-terra` | 1.05M | 128K | $2.00 | $12.00 |
| Cost-sensitive | `gpt-5.6-luna` | 1.05M | 128K | $0.20 | $1.20 |

Notes:

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

