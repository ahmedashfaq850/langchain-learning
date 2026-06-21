# LangChain Learning

Personal notes, experiments, and code while learning [LangChain](https://python.langchain.com/).

---

## Goals

- [ ] Understand LangChain core concepts (chains, prompts, models, parsers)
- [ ] Build small projects to practice each concept
- [ ] Document what I learn as I go

---

## Setup

**Requirements:** Python 3.12+

```bash
# Clone and enter the repo
cd langchain

# Install dependencies (uses uv)
uv sync

# Run the starter script
uv run python main.py
```

Add LangChain packages as you need them:

```bash
uv add langchain langchain-openai
```

Create a `.env` file for API keys (never commit this):

```env
OPENAI_API_KEY=your-key-here
```

---

## Project Structure

```
langchain/
├── main.py           # Entry point / experiments
├── pyproject.toml    # Dependencies
├── README.md         # This file — learning log & notes
└── notes/            # Optional: longer write-ups per topic
```

---

## Learning Log

Add a new entry each time you study or build something. Most recent first.

---

### YYYY-MM-DD — Topic title

**Time spent:** _e.g. 1h 30m_

**What I did:**
- 

**What I learned:**
- 

**Questions / next steps:**
- 

**Links / references:**
- 

---

### YYYY-MM-DD — Topic title

**Time spent:**

**What I did:**
- 

**What I learned:**
- 

**Questions / next steps:**
- 

**Links / references:**
- 

---

## Topics Checklist

Track concepts as you cover them.

| Topic | Status | Notes |
|-------|--------|-------|
| Prompts & prompt templates | ⬜ | |
| LLM & chat models | ⬜ | |
| Output parsers | ⬜ | |
| Chains (LCEL) | ⬜ | |
| Memory | ⬜ | |
| Agents & tools | ⬜ | |
| RAG (retrieval) | ⬜ | |
| Vector stores | ⬜ | |
| Document loaders | ⬜ | |
| LangGraph | ⬜ | |

Status: ⬜ not started · 🟡 in progress · ✅ done

---

## Snippets & Patterns

Reusable code or patterns worth remembering.

### Example: basic chain

```python
# TODO: paste a minimal example once you write one
```

---

## Resources

- [LangChain Python docs](https://python.langchain.com/docs/introduction/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- 

---

## Notes

Free-form space for ideas, comparisons, or things to revisit later.

- 
