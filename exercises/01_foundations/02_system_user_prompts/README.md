# Lesson 1.2: System Prompts, User Prompts, and Conversation History

## What You Will Learn

LLM APIs structure conversations as arrays of message objects with defined roles. This lesson covers how system prompts shape model behaviour, how to manage multi-turn conversations through message history, and how each provider handles these concepts differently. You will also learn Anthropic's assistant pre-filling technique for steering output format.

## Exercises

Each provider has two scripts:

| Script | Purpose |
|---|---|
| `call_anthropic.py` | Clean, OOP reference implementation for Anthropic |
| `call_anthropic_walkthrough.py` | Step-by-step exploration of system prompts and conversation history with Anthropic |
| `call_openai.py` | Clean, OOP reference implementation for OpenAI |
| `call_openai_walkthrough.py` | Step-by-step exploration of system instructions and conversation history with OpenAI |

**Clean scripts** (`call_*.py`) show the happy path: a client class that sets a system prompt and manages multi-turn conversation history. They are designed as reusable reference implementations you can copy into your own projects.

**Walkthrough scripts** (`call_*_walkthrough.py`) are the primary learning resources. They cover the same happy path as the clean scripts, then explore alternative scenarios (with vs without a system prompt, with vs without conversation history) and provider-specific features (Anthropic's assistant pre-filling). Run them once to build understanding, or step through them in VSCode's interactive window (Shift+Enter).

## Key Differences Between Providers

| Aspect | Anthropic | OpenAI (Responses API) |
|---|---|---|
| System prompt parameter | `system` (separate from messages) | `instructions` (separate from input) |
| Message list parameter | `messages` (list of role/content dicts) | `input` (string or list of role/content items) |
| Message roles | `user`, `assistant` | `user`, `assistant` |
| Conversation state | Stateless (send full history each request) | Stateless (send full history each request) |
| Output steering | Assistant pre-filling (partial assistant message) | Not supported in Responses API |
| `max_tokens` | Required on every request | Not required (uses model defaults) |

**Note on system prompt placement:** Both Anthropic's Messages API and OpenAI's Responses API use a separate parameter for the system prompt (`system` and `instructions` respectively). OpenAI's older Chat Completions API takes a different approach: the system prompt is a message with `role: "system"` inside the messages array. Many third-party libraries and tutorials still use the Chat Completions pattern, so you will encounter both styles.

**Note on OpenAI APIs:** OpenAI's Chat Completions API (`client.chat.completions.create()`) is still widely used and is the format that most provider-agnostic libraries (e.g. LiteLLM) standardise on. The Responses API used here is OpenAI's recommended API for new projects.

## Prerequisites

API keys for Anthropic and OpenAI must be configured in a `.env` file at the project root. See [RUNBOOK.md](../../../RUNBOOK.md) for setup instructions.

## Running the Exercises

```bash
uv run exercises/01_foundations/02_system_user_prompts/call_anthropic.py
uv run exercises/01_foundations/02_system_user_prompts/call_openai.py
uv run exercises/01_foundations/02_system_user_prompts/call_anthropic_walkthrough.py
uv run exercises/01_foundations/02_system_user_prompts/call_openai_walkthrough.py
```

## What This Lesson Does NOT Cover

- Prompt engineering techniques like few-shot prompting and chain-of-thought (Lesson 1.3)
- Structured output and response parsing (Lesson 1.4)
- Streaming responses (Lesson 1.5)
- Token management and context window limits (Lesson 1.6)
