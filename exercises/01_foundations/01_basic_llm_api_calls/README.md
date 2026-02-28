# Lesson 1.1: Making Basic LLM API Calls

## What You Will Learn

The most fundamental building block of AI Engineering: sending a message to an LLM and receiving a response. This lesson covers the basic API call pattern for both Anthropic and OpenAI.

## Exercises

Each provider has two scripts:

| Script | Purpose |
|---|---|
| `call_anthropic.py` | Clean, OOP reference implementation for Anthropic |
| `call_anthropic_walkthrough.py` | Step-by-step exploration of the Anthropic response object |
| `call_openai.py` | Clean, OOP reference implementation for OpenAI |
| `call_openai_walkthrough.py` | Step-by-step exploration of the OpenAI response object |

**Clean scripts** (`call_*.py`) are minimal, production-style code using a client class. Copy these into your own projects.

**Walkthrough scripts** (`call_*_walkthrough.py`) are flat, line-by-line explorations with explanatory output. Run them once to understand the API response anatomy, or step through them in VSCode's interactive window (Shift+Enter).

## Key Differences Between Providers

| Aspect | Anthropic | OpenAI |
|---|---|---|
| Client class | `Anthropic()` | `OpenAI()` |
| Method | `client.messages.create()` | `client.responses.create()` |
| `max_tokens` | Required | Not required |
| Input format | `messages` list of role/content dicts | `input` string |
| Response type | `anthropic.types.Message` | `openai.types.responses.Response` |
| Response text | `response.content[0].text` (requires `isinstance` check) | `response.output_text` |
| Content structure | List of typed content blocks (`TextBlock`, `ToolUseBlock`, etc.) | List of typed output items (`ResponseOutputMessage`, `ResponseFunctionToolCall`, etc.) |

**Note on OpenAI APIs:** OpenAI's older Chat Completions API (`client.chat.completions.create()`) is still widely used and is the format that most provider-agnostic libraries (e.g. LiteLLM) standardise on. The Responses API used here is OpenAI's recommended API for new projects.

## Prerequisites

API keys for Anthropic and OpenAI must be configured in a `.env` file at the project root. See [RUNBOOK.md](../../../RUNBOOK.md) for setup instructions.

## Running the Exercises

```bash
uv run exercises/01_foundations/01_basic_llm_api_calls/call_anthropic.py
uv run exercises/01_foundations/01_basic_llm_api_calls/call_openai.py
uv run exercises/01_foundations/01_basic_llm_api_calls/call_anthropic_walkthrough.py
uv run exercises/01_foundations/01_basic_llm_api_calls/call_openai_walkthrough.py
```

## What This Lesson Does NOT Cover

- System prompts (Lesson 1.2)
- Structured output (Lesson 1.4)
- Streaming (Lesson 1.5)
- Error handling (Section 8)
