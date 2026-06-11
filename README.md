# 🏆 OpenRouter LLM Cost-Effectiveness Ranking

> **Atualizado:** 2026-06-11 09:51 UTC  
> **Total de modelos no OpenRouter:** 338  
> **Modelos pagos analisados:** 308  
> **Metodologia:** Preço por 1M tokens (750K prompt + 250K completion). Dados via [OpenRouter API](https://openrouter.ai/api/v1/models).

---

## 📖 Sobre

Este ranking é gerado **automaticamente toda semana** e ordena os modelos disponíveis no [OpenRouter](https://openrouter.ai) por **custo-benefício**, organizados por caso de uso real:

- 💬 Chat cotidiano e assistente geral
- 💻 Programação e código
- 🧠 Raciocínio complexo (matemática, lógica)
- 🔍 Pesquisa e análise de documentos longos
- 🌐 Multimodal (imagem, vídeo, áudio)
- ⚡ Tarefas simples e alto volume

**Preços em USD.** Símbolos: 🟢 barato (<$0.15/M) 🟡 médio ($0.15-$0.50/M) 🟠 premium ($0.50-$1.50/M) 🔴 elite (>$1.50/M).

⭐ = Top 3 recomendações da categoria.

---

## 🏆 Top 3 Absolutos

| Posição | Modelo | Por quê |
|---------|--------|---------|
| 🥇 Melhor Global | `deepseek/deepseek-v4-pro` ($0.54/1M) | Melhor relação qualidade/preço em todas as categorias. |
| 🥈 Maior Barganha | `qwen/qwen3-235b-a22b-2507` ($0.09/1M) | 235B parâmetros (MoE) por apenas $0.09/1M tokens. |
| 🥉 Melhor Completo | `qwen/qwen3.7-plus` ($0.70/1M) | 1M contexto, multimodal, versátil, $0.70/1M. |


---

## 💡 Recomendações Rápidas

| Cenário | Melhor Escolha |
|---------|---------------|
| 💸 Quer gastar o mínimo? | `qwen/qwen3-235b-a22b-2507` ($0.09/M) e `qwen/qwen3-235b-a22b-thinking-2507` ($0.10/M) |
| ⭐ Melhor all-rounder? | `deepseek/deepseek-v4-pro` ($0.54/M) — faz tudo bem |
| 📚 Precisa de 1M de contexto? | `qwen/qwen3.7-plus` ($0.70/M) |
| 💻 Código? | `qwen/qwen3-coder-flash` ($0.39/M) ou `qwen/qwen3-coder` ($0.62/M) |
| 👁️ Multimodal / Visão? | `qwen/qwen3-vl-235b-a22b-instruct` ($0.37/M) |
| 🏔️ Topo de linha (sem limite de budget)? | `anthropic/claude-sonnet-4.5` ($6/M) ou `openai/gpt-5` ($3.44/M) |


---

## 💬 Chat Cotidiano / Assistente Geral
_Conversas, perguntas, resumos, tradução, escrita criativa_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Melhor custo-benefício global. Qualidade GPT-4o, preço de flash. |
| ⭐ 2 | `deepseek/deepseek-v3.2-exp` | 🟡 $0.3050 | $0.27 | $0.41 | 1.5x | 163,840 | DeepSeek experimental, raciocínio forte, barato. |
| ⭐ 3 | `qwen/qwen3.7-plus` | 🟠 $0.7000 | $0.40 | $1.60 | 4.0x | 1,000,000 | Qwen intermediário top. 1M contexto, ótimo custo. |
|  4 | `openai/gpt-5-mini` | 🟠 $0.6875 | $0.25 | $2.00 | 8.0x | 400,000 | GPT-5 Mini. 400K contexto, qualidade OpenAI acessível. |
|  5 | `x-ai/grok-4.3` | 🔴 $1.5625 | $1.25 | $2.50 | 2.0x | 1,000,000 | Grok 4.3. 1M contexto, web search nativa. |
|  6 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | GPT-5. Padrão ouro para tarefas complexas. |
|  7 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Claude Sonnet 4.5. 1M contexto, análise profunda. |
|  8 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Gemini Flash. Multimodal nativo, 1M contexto. |


---

## 💻 Programação / Código
_Geração de código, debugging, revisão, arquitetura de software_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Imbatível: código de qualidade a preço de flash. |
| ⭐ 2 | `qwen/qwen3-coder` | 🟠 $0.6150 | $0.22 | $1.80 | 8.2x | 1,048,576 | Coder 480B dedicado. Contexto 1M. |
| ⭐ 3 | `qwen/qwen3-coder-flash` | 🟡 $0.3900 | $0.20 | $0.97 | 5.0x | 1,000,000 | Coder Flash. Rápido e eficiente para tarefas de código. |
|  4 | `qwen/qwen3-coder-30b-a3b-instruct` | 🟢 $0.1200 | $0.07 | $0.27 | 3.9x | 160,000 | Ultra barato para código simples. $0.12/1M! |
|  5 | `mistralai/codestral-2508` | 🟡 $0.4500 | $0.30 | $0.90 | 3.0x | 256,000 | Codestral da Mistral. Focado em código. |
|  6 | `x-ai/grok-build-0.1` | 🟠 $1.2500 | $1.00 | $2.00 | 2.0x | 256,000 | Grok Build. Otimizado para engenharia de software. |
|  7 | `openai/gpt-5-codex` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | GPT-5 Codex. Especializado em código, topo OpenAI. |
|  8 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Claude Sonnet. Ótimo para refatoração e revisão de PRs. |


---

## 🧠 Raciocínio Complexo
_Matemática, lógica, ciência, problemas que exigem step-by-step_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | 🔥 Raciocínio forte, preço de modelo leve. |
| ⭐ 2 | `qwen/qwen3-235b-a22b-thinking-2507` | 🟢 $0.1000 | $0.10 | $0.10 | 1.0x | 262,144 | 235B MoE Thinking por $0.10/1M! Maior barganha. |
| ⭐ 3 | `deepseek/deepseek-v3.2-exp` | 🟡 $0.3050 | $0.27 | $0.41 | 1.5x | 163,840 | Excelente em benchmarks de raciocínio. |
|  4 | `qwen/qwen3-next-80b-a3b-thinking` | 🟡 $0.2681 | $0.10 | $0.78 | 8.0x | 262,144 | 80B MoE thinking, barato. |
|  5 | `qwen/qwen3.7-max` | 🔴 $1.8750 | $1.25 | $3.75 | 3.0x | 1,000,000 | Topo Qwen para raciocínio. 1M contexto. |
|  6 | `openai/o4-mini` | 🔴 $1.9250 | $1.10 | $4.40 | 4.0x | 200,000 | Raciocínio OpenAI acessível. |
|  7 | `anthropic/claude-opus-4.8` | 🔴 $10.0000 | $5.00 | $25.00 | 5.0x | 1,000,000 | Melhor da Anthropic, preço proibitivo. |
|  8 | `openai/o3-pro` | 🔴 $35.0000 | $20.00 | $80.00 | 4.0x | 200,000 | O mais potente da OpenAI para raciocínio. |


---

## 🔍 Pesquisa / Documentos Longos
_Análise de papers, documentos legais, relatórios extensos (requer >100K contexto)_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3.7-plus` | 🟠 $0.7000 | $0.40 | $1.60 | 4.0x | 1,000,000 | 🔥 1M contexto por $0.70. Melhor custo-benefício. |
| ⭐ 2 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Multimodal nativo, processa qualquer formato. |
| ⭐ 3 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Análise mais precisa e profunda de documentos. |
|  4 | `deepseek/deepseek-v4-pro` | 🟠 $0.5438 | $0.43 | $0.87 | 2.0x | 1,048,576 | Bom para docs médios (164K ctx). |
|  5 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | Qualidade OpenAI, 400K contexto. |


---

## 🌐 Multimodal (Imagem/Vídeo/Áudio)
_Análise de imagens, gráficos, capturas de tela, vídeos_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3-vl-235b-a22b-instruct` | 🟡 $0.3700 | $0.20 | $0.88 | 4.4x | 262,144 | 🔥 Visão 235B MoE. Preço imbatível. |
| ⭐ 2 | `google/gemini-3.5-flash` | 🔴 $3.3750 | $1.50 | $9.00 | 6.0x | 1,048,576 | Melhor multimodal: texto+imagem+áudio+video. |
| ⭐ 3 | `qwen/qwen3-vl-30b-a3b-instruct` | 🟡 $0.2275 | $0.13 | $0.52 | 4.0x | 262,144 | VL pequeno, muito barato ($0.23/1M). |
|  4 | `openai/gpt-5` | 🔴 $3.4375 | $1.25 | $10.00 | 8.0x | 400,000 | Imagem+arquivo, qualidade OpenAI. |
|  5 | `anthropic/claude-sonnet-4.5` | 🔴 $6.0000 | $3.00 | $15.00 | 5.0x | 1,000,000 | Imagem+arquivo, análise apurada. |


---

## ⚡ Tarefas Simples / Alto Volume
_Classificação, extração, batch processing, tarefas repetitivas_

| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |
|---|--------|------------|--------------|--------------|-----|----------|------|
| ⭐ 1 | `qwen/qwen3-235b-a22b-2507` | 🟢 $0.0925 | $0.09 | $0.10 | 1.1x | 262,144 | 🔥 Mais barato da lista! 235B por $0.09/1M. |
| ⭐ 2 | `openai/gpt-5-nano` | 🟢 $0.1375 | $0.05 | $0.40 | 8.0x | 400,000 | Qualidade OpenAI, barato ($0.14/1M). |
| ⭐ 3 | `google/gemini-2.5-flash-lite` | 🟡 $0.1750 | $0.10 | $0.40 | 4.0x | 1,048,576 | Google barato + 1M contexto. |
|  4 | `ibm-granite/granite-4.1-8b` | 🟢 $0.0625 | $0.05 | $0.10 | 2.0x | 131,072 | Barato extremo. $0.06/1M. |
|  5 | `mistralai/mistral-small-3.2-24b-instruct` | 🟢 $0.1062 | $0.07 | $0.20 | 2.7x | 128,000 | 24B multimodal barato. |
|  6 | `meta-llama/llama-4-scout` | 🟡 $0.1500 | $0.10 | $0.30 | 3.0x | 10,000,000 | 10M contexto! Maior do mercado. |


---

## 🔧 Metodologia

- **Fonte:** [OpenRouter API](https://openrouter.ai/api/v1/models) (dados em tempo real)
- **Cálculo de custo:** `(prompt_price × 750.000) + (completion_price × 250.000)` = custo por 1M tokens
- **Proporção:** Assume 75% prompt / 25% completion (uso típico de chat)
- **Ranking:** Ordenado por custo-benefício dentro de cada categoria, não apenas preço
- **Atualização:** Semanal (via GitHub Actions)

---

## 🤖 Automação

Este repositório é atualizado automaticamente via:
- **GitHub Actions:** Toda segunda-feira às 12:00 UTC
- **Hermes Agent:** Cron job semanal que gera e publica o ranking

Para rodar manualmente: `python generate_ranking.py`

---

*Criado por [@rafaellopes](https://github.com/rafaellopes) · [draxo.io](https://draxo.io)*
