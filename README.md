# 🏆 OpenRouter LLM Cost-Effectiveness Ranking

[![Update Ranking](https://github.com/Draxo-io/openrouter-ranking/actions/workflows/update-ranking.yml/badge.svg)](https://github.com/Draxo-io/openrouter-ranking/actions/workflows/update-ranking.yml)
[![Last Updated](https://img.shields.io/badge/updated-2026-08-03%2014:22%20UTC-blue)](https://github.com/Draxo-io/openrouter-ranking)

> **Updated:** 2026-08-03 14:22 UTC  
> **Total models on OpenRouter:** 337  
> **Paid models analyzed:** 315  
> **Methodology:** Price per 1M tokens (750K prompt + 250K completion). Data via [OpenRouter API](https://openrouter.ai/api/v1/models).

---

## 📖 About

This ranking is generated **automatically every week** and orders models available on [OpenRouter](https://openrouter.ai) by **cost-effectiveness**, organized by real-world use cases:

- 💬 Daily chat and general assistant
- 💻 Programming and code
- 🧠 Complex reasoning (math, logic)
- 🔍 Research and long document analysis
- 🌐 Multimodal (image, video, audio)
- ⚡ Simple tasks and high volume

**Prices in USD.** Symbols: 🟢 cheap (<$0.15/M) 🟡 medium ($0.15-$0.50/M) 🟠 premium ($0.50-$1.50/M) 🔴 elite (>$1.50/M).

⭐ = Top 3 recommendations per category.

---

## 🏆 Top 3 Overall

| Position | Model | Why |
|----------|------|-----|
| 🥇 Best Overall | `deepseek/deepseek-v4-pro` ($0.54/1M) | Best quality/price ratio across all categories. |
| 🥈 Best Bargain | `qwen/qwen3-235b-a22b-2507` ($0.26/1M) | 235B parameters (MoE) for only $0.09/1M tokens. |
| 🥉 Best All-Rounder | `qwen/qwen3.7-plus` ($0.56/1M) | 1M context, multimodal, versatile at $0.70/1M. |


---

## 💡 Quick Recommendations

| Scenario | Best Pick |
|----------|-----------|
| 💸 Cheapest possible? | `qwen/qwen3-235b-a22b-2507` ($0.09/M) and `qwen/qwen3-235b-a22b-thinking-2507` ($0.10/M) |
| ⭐ Best all-rounder? | `deepseek/deepseek-v4-pro` ($0.54/M) — does everything well |
| 📚 Need 1M context? | `qwen/qwen3.7-plus` ($0.70/M) |
| 💻 Code? | `qwen/qwen3-coder-flash` ($0.39/M) or `qwen/qwen3-coder` ($0.62/M) |
| 👁️ Multimodal / Vision? | `qwen/qwen3-vl-235b-a22b-instruct` ($0.37/M) |
| 🏔️ No budget limit? | `anthropic/claude-sonnet-4.5` ($6/M) or `openai/gpt-5` ($3.44/M) |


---

## 💬 Daily Chat / General Assistant
_Conversations, Q&A, summaries, translation, creative writing_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Best overall value. GPT-4o-class quality at flash prices. |
| ⭐ 2 | `deepseek/deepseek-v3.2-exp` | 🟡 $0.3050 | $0.27 | $0.41 | 1.5x | 163,840 | DeepSeek experimental. Strong reasoning, cheap. |
| ⭐ 3 | `qwen/qwen3.7-plus` | 🟠 $0.5600 | $0.32 | $1.28 | 4.0x | 1,000,000 | Qwen's mid-tier workhorse. 1M context, great value. |
|  4 | `openai/gpt-5-mini` | 🟠 $0.6875 | $0.25 | $2.00 | 8.0x | 400,000 | GPT-5 Mini. 400K context, affordable OpenAI quality. |
|  5 | `x-ai/grok-4.3` | 🔴 $1.5625 | $1.25 | $2.50 | 2.0x | 1,000,000 | Grok 4.3. 1M context, built-in web search. |
|  6 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | GPT-5. The gold standard for complex tasks. |
|  7 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Claude Sonnet 4.5. 1M context, deep analysis. |
|  8 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Gemini Flash. Native multimodal, 1M context. |


---

## 💻 Programming / Code
_Code generation, debugging, code review, software architecture_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Unbeatable: production-quality code at flash prices. |
| ⭐ 2 | `qwen/qwen3-coder` | 🟡 $0.4750 | $0.30 | $1.00 | 3.3x | 262,144 | Dedicated 480B coder. 1M context. |
| ⭐ 3 | `qwen/qwen3-coder-flash` | 🟡 $0.3900 | $0.20 | $0.97 | 5.0x | 1,000,000 | Coder Flash. Fast and efficient for code tasks. |
|  4 | `qwen/qwen3-coder-30b-a3b-instruct` | 🟢 $0.1225 | $0.07 | $0.28 | 4.0x | 262,144 | Ultra-cheap for simple code. $0.12/1M! |
|  5 | `mistralai/codestral-2508` | 🟡 $0.4500 | $0.30 | $0.90 | 3.0x | 256,000 | Mistral's Codestral. Code-focused, solid performance. |
|  6 | `x-ai/grok-build-0.1` | 🟠 $1.2500 | $1.00 | $2.00 | 2.0x | 256,000 | Grok Build. Optimized for software engineering. |
|  8 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Claude Sonnet. Excellent for refactoring and PR reviews. |


---

## 🧠 Complex Reasoning
_Math, logic, science, step-by-step problem solving_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Strong reasoning at lightweight model prices. |
| ⭐ 2 | `qwen/qwen3-235b-a22b-thinking-2507` | 🟠 $0.7475 | $0.23 | $2.30 | 10.0x | 262,144 | 235B MoE Thinking for $0.10/1M! The ultimate bargain. |
| ⭐ 3 | `deepseek/deepseek-v3.2-exp` | 🟡 $0.3050 | $0.27 | $0.41 | 1.5x | 163,840 | Excellent on reasoning benchmarks. |
|  4 | `qwen/qwen3-next-80b-a3b-thinking` | 🟡 $0.4125 | $0.15 | $1.20 | 8.0x | 262,144 | 80B MoE thinking, affordable. |
|  5 | `qwen/qwen3.7-max` | 🔴 $2.2125 | $1.48 | $4.42 | 3.0x | 1,000,000 | Qwen's top reasoning tier. 1M context. |
|  6 | `openai/o4-mini` | 🔴 $1.9250 | $1.10 | $4.40 | 4.0x | 200,000 | Accessible OpenAI reasoning. |
|  7 | `anthropic/claude-opus-4.8` | 🔴 $10.0000 | $5.00 | $25.00 | 5.0x | 1,000,000 | Anthropic's best. Pricey but unmatched depth. |
|  8 | `openai/o3-pro` | 🔴 $35.0000 | $20.00 | $80.00 | 4.0x | 200,000 | OpenAI's most powerful reasoning model. |


---

## 🔍 Research / Long Documents
_Paper analysis, legal docs, long reports (requires >100K context)_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3.7-plus` | 🟠 $0.5600 | $0.32 | $1.28 | 4.0x | 1,000,000 | 🔥 1M context for $0.70. Best value for long docs. |
| ⭐ 2 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Native multimodal, handles any format. |
| ⭐ 3 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Most precise and thorough document analysis. |
|  4 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | Solid for medium docs (164K ctx). |
|  5 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | OpenAI quality, 400K context. |


---

## 🌐 Multimodal (Image/Video/Audio)
_Image analysis, charts, screenshots, video understanding_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3-vl-235b-a22b-instruct` | 🟠 $0.6325 | $0.21 | $1.90 | 9.0x | 262,144 | 🔥 235B MoE vision. Unbeatable price. |
| ⭐ 2 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Best multimodal: text+image+audio+video natively. |
| ⭐ 3 | `qwen/qwen3-vl-30b-a3b-instruct` | 🟡 $0.2275 | $0.13 | $0.52 | 4.0x | 262,144 | Compact VL model, very cheap ($0.23/1M). |
|  4 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | Image+file support, OpenAI quality. |
|  5 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Image+file support, precise analysis. |


---

## ⚡ Simple Tasks / High Volume
_Classification, extraction, batch processing, repetitive tasks_

| # | Model | $/1M Tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Context | Notes |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3-235b-a22b-2507` | 🟡 $0.2616 | $0.15 | $0.60 | 4.0x | 262,144 | 🔥 Cheapest on the list! 235B for $0.09/1M. |
| ⭐ 2 | `openai/gpt-5-nano` | 🟢 $0.1375 | $0.05 | $0.40 | 8.0x | 400,000 | OpenAI quality, cheap ($0.14/1M). |
| ⭐ 3 | `google/gemini-2.5-flash-lite` | 🟡 $0.1750 | $0.10 | $0.40 | 4.0x | 1,048,576 | Google's budget option + 1M context. |
|  4 | `ibm-granite/granite-4.1-8b` | 🟢 $0.0625 | $0.05 | $0.10 | 2.0x | 131,072 | Extremely cheap. $0.06/1M. |
|  5 | `mistralai/mistral-small-3.2-24b-instruct` | 🟢 $0.1062 | $0.07 | $0.20 | 2.7x | 256,000 | 24B multimodal, affordable. |
|  6 | `meta-llama/llama-4-scout` | 🟡 $0.1500 | $0.10 | $0.30 | 3.0x | 1,310,720 | 10M context! Largest on the market. |


---

## 🔧 Methodology

- **Source:** [OpenRouter API](https://openrouter.ai/api/v1/models) (real-time data)
- **Cost formula:** `(prompt_price × 750,000) + (completion_price × 250,000)` = cost per 1M tokens
- **Ratio:** Assumes 75% prompt / 25% completion (typical chat usage)
- **Ranking:** Ordered by cost-effectiveness within each category, not just price
- **Updates:** Weekly (via GitHub Actions)

---

## 🤖 Automation

This repository is updated automatically via:
- **GitHub Actions:** Every Monday at 12:00 UTC
- **Hermes Agent:** Weekly cron job that generates and publishes the ranking

To run manually: `python generate_ranking.py`

---

*Created by [@Draxo-io](https://github.com/Draxo-io) · [draxo.io](https://draxo.io)*
