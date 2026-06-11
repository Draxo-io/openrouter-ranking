#!/usr/bin/env python3
"""
OpenRouter LLM Cost-Effectiveness Ranking Generator
Fetches live pricing from OpenRouter API and generates a ranked README.md
organized by use case with cost-benefit analysis.

Usage: python generate_ranking.py [--output README.md]
"""

import json, urllib.request, sys, os
from datetime import datetime, timezone
from collections import defaultdict

OPENROUTER_API = "https://openrouter.ai/api/v1/models"
OUTPUT_FILE = "README.md"

# ── Task definitions ──────────────────────────────────────────────

TASKS = {
    "💬 Chat Cotidiano / Assistente Geral": {
        "desc": "Conversas, perguntas, resumos, tradução, escrita criativa",
        "models": [
            "deepseek/deepseek-v4-pro",
            "deepseek/deepseek-v3.2-exp",
            "qwen/qwen3.7-plus",
            "openai/gpt-5-mini",
            "x-ai/grok-4.3",
            "openai/gpt-5",
            "anthropic/claude-sonnet-4.5",
            "google/gemini-3.5-flash",
        ],
        "notes": {
            "deepseek/deepseek-v4-pro": "🔥 Melhor custo-benefício global. Qualidade GPT-4o, preço de flash.",
            "deepseek/deepseek-v3.2-exp": "DeepSeek experimental, raciocínio forte, barato.",
            "qwen/qwen3.7-plus": "Qwen intermediário top. 1M contexto, ótimo custo.",
            "openai/gpt-5-mini": "GPT-5 Mini. 400K contexto, qualidade OpenAI acessível.",
            "x-ai/grok-4.3": "Grok 4.3. 1M contexto, web search nativa.",
            "openai/gpt-5": "GPT-5. Padrão ouro para tarefas complexas.",
            "anthropic/claude-sonnet-4.5": "Claude Sonnet 4.5. 1M contexto, análise profunda.",
            "google/gemini-3.5-flash": "Gemini Flash. Multimodal nativo, 1M contexto.",
        }
    },
    "💻 Programação / Código": {
        "desc": "Geração de código, debugging, revisão, arquitetura de software",
        "models": [
            "deepseek/deepseek-v4-pro",
            "qwen/qwen3-coder",
            "qwen/qwen3-coder-flash",
            "qwen/qwen3-coder-30b-a3b-instruct",
            "mistralai/codestral-2508",
            "x-ai/grok-build-0.1",
            "openai/gpt-5-codex",
            "anthropic/claude-sonnet-4.5",
        ],
        "notes": {
            "deepseek/deepseek-v4-pro": "🔥 Imbatível: código de qualidade a preço de flash.",
            "qwen/qwen3-coder": "Coder 480B dedicado. Contexto 1M.",
            "qwen/qwen3-coder-flash": "Coder Flash. Rápido e eficiente para tarefas de código.",
            "qwen/qwen3-coder-30b-a3b-instruct": "Ultra barato para código simples. $0.12/1M!",
            "mistralai/codestral-2508": "Codestral da Mistral. Focado em código.",
            "x-ai/grok-build-0.1": "Grok Build. Otimizado para engenharia de software.",
            "openai/gpt-5-codex": "GPT-5 Codex. Especializado em código, topo OpenAI.",
            "anthropic/claude-sonnet-4.5": "Claude Sonnet. Ótimo para refatoração e revisão de PRs.",
        }
    },
    "🧠 Raciocínio Complexo": {
        "desc": "Matemática, lógica, ciência, problemas que exigem step-by-step",
        "models": [
            "deepseek/deepseek-v4-pro",
            "qwen/qwen3-235b-a22b-thinking-2507",
            "deepseek/deepseek-v3.2-exp",
            "qwen/qwen3-next-80b-a3b-thinking",
            "qwen/qwen3.7-max",
            "openai/o4-mini",
            "anthropic/claude-opus-4.8",
            "openai/o3-pro",
        ],
        "notes": {
            "deepseek/deepseek-v4-pro": "🔥 Raciocínio forte, preço de modelo leve.",
            "qwen/qwen3-235b-a22b-thinking-2507": "235B MoE Thinking por $0.10/1M! Maior barganha.",
            "deepseek/deepseek-v3.2-exp": "Excelente em benchmarks de raciocínio.",
            "qwen/qwen3-next-80b-a3b-thinking": "80B MoE thinking, barato.",
            "qwen/qwen3.7-max": "Topo Qwen para raciocínio. 1M contexto.",
            "openai/o4-mini": "Raciocínio OpenAI acessível.",
            "anthropic/claude-opus-4.8": "Melhor da Anthropic, preço proibitivo.",
            "openai/o3-pro": "O mais potente da OpenAI para raciocínio.",
        }
    },
    "🔍 Pesquisa / Documentos Longos": {
        "desc": "Análise de papers, documentos legais, relatórios extensos (requer >100K contexto)",
        "models": [
            "qwen/qwen3.7-plus",
            "google/gemini-3.5-flash",
            "anthropic/claude-sonnet-4.5",
            "deepseek/deepseek-v4-pro",
            "openai/gpt-5",
        ],
        "notes": {
            "qwen/qwen3.7-plus": "🔥 1M contexto por $0.70. Melhor custo-benefício.",
            "google/gemini-3.5-flash": "Multimodal nativo, processa qualquer formato.",
            "anthropic/claude-sonnet-4.5": "Análise mais precisa e profunda de documentos.",
            "deepseek/deepseek-v4-pro": "Bom para docs médios (164K ctx).",
            "openai/gpt-5": "Qualidade OpenAI, 400K contexto.",
        }
    },
    "🌐 Multimodal (Imagem/Vídeo/Áudio)": {
        "desc": "Análise de imagens, gráficos, capturas de tela, vídeos",
        "models": [
            "qwen/qwen3-vl-235b-a22b-instruct",
            "google/gemini-3.5-flash",
            "qwen/qwen3-vl-30b-a3b-instruct",
            "openai/gpt-5",
            "anthropic/claude-sonnet-4.5",
        ],
        "notes": {
            "qwen/qwen3-vl-235b-a22b-instruct": "🔥 Visão 235B MoE. Preço imbatível.",
            "google/gemini-3.5-flash": "Melhor multimodal: texto+imagem+áudio+video.",
            "qwen/qwen3-vl-30b-a3b-instruct": "VL pequeno, muito barato ($0.23/1M).",
            "openai/gpt-5": "Imagem+arquivo, qualidade OpenAI.",
            "anthropic/claude-sonnet-4.5": "Imagem+arquivo, análise apurada.",
        }
    },
    "⚡ Tarefas Simples / Alto Volume": {
        "desc": "Classificação, extração, batch processing, tarefas repetitivas",
        "models": [
            "qwen/qwen3-235b-a22b-2507",
            "openai/gpt-5-nano",
            "google/gemini-2.5-flash-lite",
            "ibm-granite/granite-4.1-8b",
            "mistralai/mistral-small-3.2-24b-instruct",
            "meta-llama/llama-4-scout",
        ],
        "notes": {
            "qwen/qwen3-235b-a22b-2507": "🔥 Mais barato da lista! 235B por $0.09/1M.",
            "openai/gpt-5-nano": "Qualidade OpenAI, barato ($0.14/1M).",
            "google/gemini-2.5-flash-lite": "Google barato + 1M contexto.",
            "ibm-granite/granite-4.1-8b": "Barato extremo. $0.06/1M.",
            "mistralai/mistral-small-3.2-24b-instruct": "24B multimodal barato.",
            "meta-llama/llama-4-scout": "10M contexto! Maior do mercado.",
        }
    },
}


def fetch_models():
    """Fetch all models from OpenRouter API."""
    req = urllib.request.Request(OPENROUTER_API, headers={"User-Agent": "openrouter-ranking/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["data"]


def build_model_index(models_data):
    """Build a lookup of model_id -> pricing info."""
    index = {}
    for m in models_data:
        mid = m["id"]
        p = m.get("pricing", {})
        prompt = float(p.get("prompt", 0))
        completion = float(p.get("completion", 0))

        # Skip free, router-only, or invalid pricing
        if ":free" in mid or prompt < 0 or completion < 0 or (prompt == 0 and completion == 0):
            continue

        mixed = prompt * 750_000 + completion * 250_000
        index[mid] = {
            "name": m["name"],
            "context": m.get("context_length", 0),
            "prompt_cost": prompt,
            "completion_cost": completion,
            "cost_per_1M": mixed,
            "ratio": completion / prompt if prompt > 0 else 0,
        }
    return index


def price_bar(cost):
    if cost < 0.15:
        return "🟢"
    elif cost < 0.50:
        return "🟡"
    elif cost < 1.50:
        return "🟠"
    else:
        return "🔴"


def format_price(price_per_token):
    """Format price per token to display as $X.XX/1M tokens equivalent in cents."""
    cost_1M = price_per_token * 1_000_000
    if cost_1M < 0.01:
        return f"${cost_1M:.4f}"
    elif cost_1M < 1:
        return f"${cost_1M:.2f}¢"
    else:
        return f"${cost_1M:.2f}"


def generate_tables(model_index):
    """Generate markdown tables for each task category."""
    sections = []

    for task_name, task_info in TASKS.items():
        lines = []
        lines.append(f"## {task_name}")
        lines.append(f"_{task_info['desc']}_")
        lines.append("")
        lines.append("| # | Modelo | $/1M tokens | Prompt (¢/1M) | Compl (¢/1M) | P/C | Contexto | Nota |")
        lines.append("|---|--------|------------|--------------|--------------|-----|----------|------|")

        for i, mid in enumerate(task_info["models"]):
            m = model_index.get(mid)
            if not m:
                continue

            star = "⭐" if i < 3 else ""
            bar = price_bar(m["cost_per_1M"])
            note = task_info["notes"].get(mid, "")

            lines.append(
                f"| {star} {i+1} | `{mid}` | {bar} ${m['cost_per_1M']:.4f} | "
                f"${m['prompt_cost']*1_000_000:.2f} | ${m['completion_cost']*1_000_000:.2f} | "
                f"{m['ratio']:.1f}x | {m['context']:,} | {note} |"
            )

        lines.append("")
        sections.append("\n".join(lines))

    return sections


def generate_summary(model_index):
    """Generate executive summary with top picks."""
    top_models = [
        ("🥇 Melhor Global", "deepseek/deepseek-v4-pro", "Melhor relação qualidade/preço em todas as categorias."),
        ("🥈 Maior Barganha", "qwen/qwen3-235b-a22b-2507", "235B parâmetros (MoE) por apenas $0.09/1M tokens."),
        ("🥉 Melhor Completo", "qwen/qwen3.7-plus", "1M contexto, multimodal, versátil, $0.70/1M."),
    ]

    lines = [
        "## 🏆 Top 3 Absolutos",
        "",
        "| Posição | Modelo | Por quê |",
        "|---------|--------|---------|",
    ]
    for pos, mid, reason in top_models:
        m = model_index.get(mid, {})
        price = f"${m.get('cost_per_1M', 0):.2f}/1M" if m else "N/A"
        lines.append(f"| {pos} | `{mid}` ({price}) | {reason} |")

    lines.append("")
    return "\n".join(lines)


def generate_cheatsheet():
    """Generate the quick-reference cheat sheet."""
    tips = [
        ("💸 Quer gastar o mínimo?", "`qwen/qwen3-235b-a22b-2507` ($0.09/M) e `qwen/qwen3-235b-a22b-thinking-2507` ($0.10/M)"),
        ("⭐ Melhor all-rounder?", "`deepseek/deepseek-v4-pro` ($0.54/M) — faz tudo bem"),
        ("📚 Precisa de 1M de contexto?", "`qwen/qwen3.7-plus` ($0.70/M)"),
        ("💻 Código?", "`qwen/qwen3-coder-flash` ($0.39/M) ou `qwen/qwen3-coder` ($0.62/M)"),
        ("👁️ Multimodal / Visão?", "`qwen/qwen3-vl-235b-a22b-instruct` ($0.37/M)"),
        ("🏔️ Topo de linha (sem limite de budget)?", "`anthropic/claude-sonnet-4.5` ($6/M) ou `openai/gpt-5` ($3.44/M)"),
    ]

    lines = [
        "## 💡 Recomendações Rápidas",
        "",
        "| Cenário | Melhor Escolha |",
        "|---------|---------------|",
    ]
    for scenario, pick in tips:
        lines.append(f"| {scenario} | {pick} |")

    lines.append("")
    return "\n".join(lines)


def main():
    print("🔄 Fetching models from OpenRouter API...", file=sys.stderr)
    models_data = fetch_models()
    model_index = build_model_index(models_data)
    print(f"✅ Loaded {len(model_index)} paid models", file=sys.stderr)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_models = len(models_data)

    tables = generate_tables(model_index)
    summary = generate_summary(model_index)
    cheatsheet = generate_cheatsheet()
    joined_tables = "\n\n---\n\n".join(tables)

    readme = f"""# 🏆 OpenRouter LLM Cost-Effectiveness Ranking

> **Atualizado:** {now}  
> **Total de modelos no OpenRouter:** {total_models}  
> **Modelos pagos analisados:** {len(model_index)}  
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

{summary}

---

{cheatsheet}

---

{joined_tables}

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
"""

    output = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_FILE
    with open(output, "w") as f:
        f.write(readme)

    print(f"✅ Written to {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
