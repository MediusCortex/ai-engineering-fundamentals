# Runbook

## API Keys and Environment Variables

### What Are Environment Variables

Environment variables are key-value pairs available to processes running on your system. They are the standard way to provide secrets (such as API keys) to applications without hardcoding them in source code. In this curriculum, every script that calls an LLM provider needs an API key to authenticate.

### Why You Need API Keys

LLM providers (Anthropic, OpenAI) require API keys to authenticate requests. Each API call is billed to the account associated with the key. You will need:

- **`ANTHROPIC_API_KEY`**: For exercises that call Anthropic's Claude models.
- **`OPENAI_API_KEY`**: For exercises that call OpenAI's GPT models.

### Getting Your API Keys

**Anthropic:**

1. Create an account at [console.anthropic.com](https://console.anthropic.com/).
2. Navigate to **API Keys** in the dashboard.
3. Click **Create Key**, give it a name, and copy the key.

**OpenAI:**

1. Create an account at [platform.openai.com](https://platform.openai.com/).
2. Navigate to **API Keys** in your account settings.
3. Click **Create new secret key**, give it a name, and copy the key.

Both providers offer free trial credits for new accounts. Check their pricing pages for current details.

### Setting Up Your `.env` File

Create a `.env` file in the project root:

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here
```

This file is listed in `.gitignore` and will never be committed to version control. Every exercise script uses `python-dotenv` to load these variables automatically at runtime.

## Running Exercise Scripts

Each exercise script includes [uv inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies), making it self-contained and runnable without activating a virtual environment:

```bash
uv run exercises/01_foundations/01_basic_llm_api_calls/call_anthropic.py
```

`python-dotenv` loads the `.env` file from the project root automatically, so the API keys are available regardless of which directory you run the script from.

### Running Line-by-Line in VSCode

For interactive development using VSCode's Jupyter interactive window:

1. Make sure the `.venv` is created and synced: `uv sync`
2. Select the `.venv` Python interpreter in VSCode.
3. Open any exercise script and use **Shift+Enter** to run lines or selections interactively.

The `.venv` contains all dependencies from `pyproject.toml`, so all imports will resolve correctly in the interactive window.
