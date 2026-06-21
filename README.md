# LangChain Learning

Hands-on experiments while learning [LangChain](https://python.langchain.com/). Each script in `src/langchain_basics/` covers one concept, runnable on its own.

---

## Setup

**Requirements:** Python 3.12+, [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/ahmedashfaq850/langchain-learning.git
cd langchain-learning

uv sync
```

Create a `.env` file in the project root (never commit this):

```env
OPENROUTER_API_KEY=your-key-here
OPENROUTER_MODEL=google/gemini-2.0-flash-001
```

Run any example:

```bash
uv run src/langchain_basics/llm_calling.py
```

---

## Project Structure

```
langchain-learning/
├── main.py                          # Placeholder entry point
├── pyproject.toml                   # Dependencies (LangChain, OpenRouter, etc.)
├── src/langchain_basics/
│   ├── llm_calling.py               # Basic LLM invoke + token usage & cost
│   ├── llm_prompting.py             # System & human messages
│   ├── prompt_templates.py          # ChatPromptTemplate with variables
│   ├── llm_chains.py                # LCEL chain (prompt | model)
│   └── text_streaming.py            # Stream tokens as they arrive
└── README.md
```

---

## What's Working

| Script | What it does |
|--------|--------------|
| `llm_calling.py` | Calls OpenRouter via `ChatOpenRouter`, prints the response, token usage, and estimated cost |
| `llm_prompting.py` | Sends a structured conversation using `SystemMessage` and `HumanMessage` |
| `prompt_templates.py` | Builds a reusable `ChatPromptTemplate` with a `{input}` placeholder |
| `llm_chains.py` | Chains prompt and model with LCEL (`prompt \| model`) |
| `text_streaming.py` | Streams the model output chunk by chunk with `llm.stream()` |

All scripts use **OpenRouter** as the model provider and load config from `.env`.

---

## Progress

| Topic | Status |
|-------|--------|
| LLM & chat models | ✅ |
| Prompts & message types | ✅ |
| Prompt templates | ✅ |
| Chains (LCEL) | ✅ |
| Streaming | ✅ |
| Output parsers | ⬜ |
| Memory | ⬜ |
| Agents & tools | ⬜ |
| RAG (retrieval) | ⬜ |
| Vector stores | ⬜ |
| Document loaders | ⬜ |
| LangGraph | ⬜ |

---

## Key Takeaways So Far

- **Messages** — LangChain uses typed messages (`SystemMessage`, `HumanMessage`, `AIMessage`) instead of raw strings for chat models.
- **Prompt templates** — Reusable prompts with variables keep instructions consistent and make inputs easy to swap.
- **LCEL** — The pipe operator (`prompt | model`) connects steps into a chain you can invoke like a single function.
- **Streaming** — `llm.stream()` yields chunks as the model generates, useful for responsive UIs.

---

## Resources

- [LangChain Python docs](https://python.langchain.com/docs/introduction/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [OpenRouter](https://openrouter.ai/)
