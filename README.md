# AI Engineering Fundamentals

A step-by-step curriculum for software engineers learning applied AI Engineering.

## What This Is

A collection of exercises teaching the core building blocks of AI Engineering: making LLM API calls, structuring outputs, engineering context, building retrieval pipelines, orchestrating agents, and evaluating AI systems in production. Every exercise uses native Python with provider SDKs (primarily OpenAI and Anthropic), with no framework abstractions.

## What This Is Not

This is not a machine learning, data science, or LLM research curriculum. We do not train models, fine-tune weights, or study transformer architectures. We build systems that use LLMs to emulate human reasoning and decision-making.

## Unifying Use Case

All exercises are grounded in a single use case: a customer service chatbot for **Acme Running**, a fictional premium running shoe brand. The same business problem is solved using different approaches and techniques as the curriculum progresses. See [docs/use_case.md](docs/use_case.md) for the full use case description.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) as the package manager
- API keys for OpenAI and Anthropic

## Setup

```bash
uv sync
```

See [RUNBOOK.md](RUNBOOK.md) for instructions on running exercises.
