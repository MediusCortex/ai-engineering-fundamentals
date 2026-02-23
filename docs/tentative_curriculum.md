# AI Engineering Fundamentals: Tentative Curriculum

## Purpose

This document defines the structured curriculum for teaching software engineers how to become applied AI Engineers. The curriculum is organised into logical sections that reflect the actual engineering disciplines involved in building AI systems, ordered from foundational to advanced.

## Guiding Principles

1. **AI Engineering is not ML/Data Science.** We build systems that emulate human reasoning using LLMs and other methods. We do not train models, fine-tune weights, or perform statistical induction.
2. **Native Python, no framework abstractions.** Every concept is taught using provider SDKs (primarily OpenAI and Anthropic) and native Python. Frameworks like LangChain and LlamaIndex are studied for their patterns, never used as dependencies.
3. **Applied, not theoretical.** Every topic must result in a working code exercise that solves a concrete problem. No academic exercises without practical application.
4. **Provider-agnostic understanding.** Each topic is taught using both OpenAI and Anthropic SDKs where applicable, so engineers understand the underlying patterns rather than memorising a single API surface.
5. **Progressive complexity.** Sections build on one another. Each topic within a section assumes mastery of the preceding topics.

## Curriculum Structure

The curriculum is divided into **9 sections**, containing a total of **37+ topics**. Each section represents a distinct engineering discipline within applied AI Engineering.

---

### Section 1: Foundations

The irreducible building blocks. Every AI system starts here. This section teaches how to communicate with LLMs, shape their responses, and manage the fundamental constraints of the medium.

#### 1.1 Making Basic LLM API Calls

The most fundamental building block. Send a message to an LLM, get a response. Covers OpenAI's Chat Completions API (`client.chat.completions.create()`) and Anthropic's Messages API (`client.messages.create()`). Key differences: Anthropic requires explicit `max_tokens`, uses a separate `system` parameter, and returns typed content blocks. OpenAI's newer Responses API (`client.responses.create()`) is also covered.

**Documentation:**

- OpenAI Chat Completions API Reference: https://platform.openai.com/docs/api-reference/chat
- OpenAI Text Generation Guide: https://platform.openai.com/docs/guides/text
- Anthropic Messages API Reference: https://docs.anthropic.com/en/api/messages
- Anthropic Client SDKs: https://docs.anthropic.com/en/api/client-sdks

**Code Examples:**

- OpenAI Cookbook: https://cookbook.openai.com/
- Anthropic Cookbook: https://github.com/anthropics/anthropic-cookbook

**Reference Repos:**

- `openai/openai-python`: https://github.com/openai/openai-python
- `anthropics/anthropic-sdk-python`: https://github.com/anthropics/anthropic-sdk-python

#### 1.2 System Prompts, User Prompts, and Conversation History

LLM APIs structure conversations as arrays of message objects with defined roles. OpenAI uses system/user/assistant roles in the messages array; Anthropic separates the system prompt into its own parameter. The API is stateless, so the full conversation history must be sent with each request. Covers message list management, truncation strategies, sliding window approaches, and Anthropic's assistant pre-filling technique for steering output format.

**Documentation:**

- OpenAI Text Generation (message roles): https://platform.openai.com/docs/guides/text
- Anthropic Messages API: https://docs.anthropic.com/en/api/messages
- Anthropic Prompt Templates and Variables: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

**Code Examples:**

- Anthropic Courses (API Fundamentals): https://github.com/anthropics/courses
- OpenAI Cookbook: https://github.com/openai/openai-cookbook

#### 1.3 Prompt Engineering Techniques

The practice of crafting instructions that guide LLMs to produce desired outputs consistently. Covers few-shot prompting, chain-of-thought reasoning, role-based prompting, XML tagging (Anthropic's recommended approach), and the differences between prompting reasoning models (high-level guidance) vs. standard models (precise instructions).

**Documentation:**

- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic Prompt Engineering Overview: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Anthropic Claude 4.x Best Practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

**Code Examples:**

- Anthropic Interactive Prompt Engineering Tutorial: https://github.com/anthropics/prompt-eng-interactive-tutorial
- Anthropic Courses: https://github.com/anthropics/courses

#### 1.4 Structured Output and Response Parsing

Ensuring LLM responses conform to predefined schemas, eliminating manual parsing. OpenAI's Structured Outputs guarantee schema-adherent JSON via constrained grammar sampling, integrating directly with Pydantic. Anthropic uses a tool-based approach for structured extraction. The Instructor library provides a unified Pydantic-based wrapper across providers. This is the foundation for building typed, reliable LLM pipelines.

**Documentation:**

- OpenAI Structured Outputs Guide: https://platform.openai.com/docs/guides/structured-outputs
- Anthropic Messages API (tool-based structured output): https://docs.anthropic.com/en/api/messages
- Instructor Documentation: https://python.useinstructor.com/
- PydanticAI Documentation: https://ai.pydantic.dev/

**Reference Repos:**

- `jxnl/instructor`: https://github.com/jxnl/instructor
- `dottxt-ai/outlines`: https://github.com/dottxt-ai/outlines
- `pydantic/pydantic-ai`: https://github.com/pydantic/pydantic-ai

#### 1.5 Streaming Responses

Receiving and processing LLM output incrementally as tokens are generated, using Server-Sent Events (SSE). OpenAI streams `chat.completion.chunk` objects; Anthropic uses a richer event protocol (`message_start`, `content_block_start`, `content_block_delta`, `message_stop`). Both support streaming with tool calls. Critical for interactive applications and for avoiding HTTP timeouts on large responses.

**Documentation:**

- OpenAI Streaming Guide: https://platform.openai.com/docs/api-reference/streaming
- Anthropic Streaming Messages: https://docs.anthropic.com/en/api/messages-streaming

#### 1.6 Token Counting, Context Windows, and Cost Optimisation

Tokens are the fundamental units of LLM processing, determining both context limits and costs. Covers `tiktoken` (OpenAI's BPE tokeniser), Anthropic's `client.messages.count_tokens()`, context window sizes across models, and cost structures. Output tokens cost 3 to 8x more than input tokens, making output length control the highest-leverage cost optimisation.

**Documentation:**

- Anthropic Prompt Caching: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Anthropic Message Batches API: https://docs.anthropic.com/en/docs/build-with-claude/message-batches
- OpenAI Prompt Caching: https://platform.openai.com/docs/guides/text

**Reference Repos:**

- `openai/tiktoken`: https://github.com/openai/tiktoken
- `BerriAI/litellm`: https://github.com/BerriAI/litellm

#### 1.7 Provider-Agnostic LLM Clients

Abstracting differences between OpenAI, Anthropic, Google, and other APIs into a unified interface. LiteLLM standardises 100+ providers into OpenAI's chat completions format. The key abstraction pattern: unified message format, provider-specific transformers for request/response mapping, and routing based on model string prefixes. Also covers building your own abstraction layer.

**Documentation:**

- LiteLLM Documentation: https://docs.litellm.ai/docs/
- LiteLLM Supported Providers: https://docs.litellm.ai/docs/providers

**Reference Repos:**

- `BerriAI/litellm`: https://github.com/BerriAI/litellm

---

### Section 2: Context Engineering

How to construct, compose, and manage what goes into the LLM's context window. This is arguably the most important engineering discipline in applied AI, since the quality of an LLM's output is bounded by the quality of its input context.

#### 2.1 Prompt Templating and Management

Creating parameterised prompt structures with dynamic placeholders filled at runtime. Covers Python f-strings (simplest), Jinja2 templates (conditionals, loops, filters), and mustache/handlebars. Also covers Anthropic's Console tools: prompt generator, prompt improver, and one-click code export. Prompts are treated as versioned, testable artefacts.

**Documentation:**

- Anthropic Prompt Improver: https://www.anthropic.com/news/prompt-improver
- Anthropic Prompt Generator: https://www.anthropic.com/news/prompt-generator
- DSPy Official Documentation: https://dspy.ai/

**Reference Repos:**

- `stanfordnlp/dspy`: https://github.com/stanfordnlp/dspy
- `langfuse/langfuse`: https://github.com/langfuse/langfuse

#### 2.2 Dynamic Prompt Injection

Programmatically injecting context, data, and instructions into prompts at runtime based on the current request. This includes injecting retrieved documents (from RAG), user profile data, tool descriptions, conversation summaries, and any other runtime-determined content into the prompt before it reaches the LLM. The key engineering challenge is selecting the right content, respecting token limits, and maintaining prompt coherence.

**Documentation:**

- Anthropic Prompt Templates and Variables: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
- OpenAI Text Generation Guide: https://platform.openai.com/docs/guides/text

#### 2.3 Dynamic Prompt Composition

Building complete prompts by assembling modular components at runtime. Unlike static templates with placeholders, dynamic composition constructs the entire prompt structure conditionally: selecting which sections to include, ordering them based on relevance, choosing between different instruction sets based on routing decisions, and composing multi-part prompts from reusable building blocks. This is the pattern that enables adaptive, context-aware AI systems.

**Documentation:**

- Anthropic Prompt Engineering Overview: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering

#### 2.4 Context Window Management and Optimisation

Engineering strategies for making the most of finite context windows. Covers conversation history truncation, summarisation of old context into condensed messages, sliding window approaches, priority-based content selection, and techniques for structuring long contexts so the LLM attends to the most important information. Also covers extended thinking (Anthropic) and reasoning tokens (OpenAI o-series) and how they consume context budget.

**Documentation:**

- Anthropic Extended Thinking: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- OpenAI Reasoning Models: https://platform.openai.com/docs/guides/reasoning

#### 2.5 Prompt Caching Strategies

Reusing computation for repeated prompt prefixes. Anthropic requires explicit `cache_control` breakpoints (up to 90% cost reduction, 5-minute or 1-hour TTL). OpenAI caches automatically for prompts over 1024 tokens (50% cost discount). Covers when to use provider-level caching, how to structure prompts to maximise cache hits, and the interaction between caching and dynamic prompt composition.

**Documentation:**

- Anthropic Prompt Caching: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- OpenAI Prompt Caching Guide: https://developers.openai.com/api/docs/guides/prompt-caching/

**Code Examples:**

- OpenAI Prompt Caching 101: https://cookbook.openai.com/examples/prompt_caching101

#### 2.6 DSPy: Programmatic Prompt Optimisation

DSPy treats LLM prompts as optimisable programs rather than hand-crafted text. Signatures declare input/output behaviour, Modules encapsulate strategies (Predict, ChainOfThought, ReAct), and Optimisers automatically improve prompts by tuning instructions and selecting few-shot examples using training data and metrics. The core insight is that prompts should be compiled artefacts optimised against metrics, not manually engineered strings.

**Documentation:**

- DSPy Official Docs: https://dspy.ai/
- DSPy Signatures: https://dspy.ai/learn/programming/signatures/
- DSPy Optimisers: https://dspy.ai/learn/optimization/optimizers/

**Reference Repos:**

- `stanfordnlp/dspy`: https://github.com/stanfordnlp/dspy

---

### Section 3: Data Persistence

How to store, index, and organise data so that AI systems can retrieve it effectively. Covers both vector-based and graph-based storage paradigms.

#### 3.1 Embeddings and Vector Representations

Dense numerical vector representations of text that capture semantic meaning. OpenAI offers `text-embedding-3-small` and `text-embedding-3-large` with a `dimensions` parameter. Anthropic partners with Voyage AI for embeddings. Covers embedding generation, dimensionality trade-offs, distance metrics (cosine similarity, L2, inner product), and the distinction between query and document embeddings.

**Documentation:**

- OpenAI Embeddings Guide: https://developers.openai.com/api/docs/guides/embeddings/
- OpenAI Embeddings API Reference: https://platform.openai.com/docs/api-reference/embeddings/create
- Anthropic/Voyage AI Embeddings Guide: https://github.com/anthropics/claude-cookbooks/blob/main/third_party/VoyageAI/how_to_create_embeddings.md

**Reference Repos:**

- `facebookresearch/faiss`: https://github.com/facebookresearch/faiss
- `UKPLab/sentence-transformers`: https://github.com/UKPLab/sentence-transformers

#### 3.2 Vector Databases and Indexing Strategies

Specialised storage systems optimised for indexing and querying high-dimensional vectors using approximate nearest neighbour (ANN) algorithms. Covers the spectrum from lightweight (Chroma, SQLite-backed) to production-scale (Pinecone, billions of vectors), with pgvector (PostgreSQL extension) as the practical middle ground. Key indexing strategies: HNSW (graph-based, best general-purpose) and IVF (cluster-based partitioning). Also covers metadata filtering for combining vector similarity with structured attribute queries.

**Documentation:**

- Chroma Documentation: https://docs.trychroma.com/
- pgvector: https://github.com/pgvector/pgvector
- Pinecone: https://docs.pinecone.io/
- Qdrant: https://qdrant.tech/documentation/

**Reference Repos:**

- `chroma-core/chroma`: https://github.com/chroma-core/chroma
- `pgvector/pgvector`: https://github.com/pgvector/pgvector
- `facebookresearch/faiss`: https://github.com/facebookresearch/faiss

#### 3.3 Knowledge Graph Storage and Modelling

Organising entities and relationships into structured, interconnected representations. Covers graph data modelling (nodes, edges, properties), graph databases (Neo4j as the leading option), and LLM-assisted graph construction: extracting entities and relationships from unstructured text, building hierarchical graphs with community detection. Also covers Microsoft's GraphRAG approach to graph construction.

**Documentation:**

- Microsoft GraphRAG: https://microsoft.github.io/graphrag/
- Microsoft GraphRAG Blog: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
- Neo4j GenAI Ecosystem: https://neo4j.com/labs/genai-ecosystem/

**Reference Repos:**

- `microsoft/graphrag`: https://github.com/microsoft/graphrag
- `neo4j-labs/llm-graph-builder`: https://github.com/neo4j-labs/llm-graph-builder

#### 3.4 Document Chunking Strategies

Breaking documents into segments suitable for embedding and retrieval. Covers fixed-size windows with overlap, recursive splitting that respects paragraph/sentence boundaries, semantic chunking by embedding similarity, and document-structure-aware parsing. Chunk size and overlap directly affect retrieval quality. Also covers Anthropic's Contextual Retrieval technique: adding LLM-generated context to each chunk before embedding, reducing retrieval failure by up to 67%.

**Documentation:**

- Anthropic Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval

---

### Section 4: Retrieval

How to query stored data and compose it into LLM context. Builds directly on Data Persistence.

#### 4.1 Semantic Search with Embeddings

Querying vector databases to find semantically similar content. Covers query embedding generation, similarity search with distance thresholds, top-k retrieval, and the engineering of search quality: query reformulation, hypothetical document embeddings (HyDE), and the impact of embedding model choice on retrieval precision and recall.

**Documentation:**

- OpenAI Embeddings Guide: https://developers.openai.com/api/docs/guides/embeddings/

#### 4.2 RAG: Retrieval-Augmented Generation

The end-to-end pipeline: query embedding, retrieval, reranking, context injection, and LLM generation. Covers the offline ingestion pipeline (chunking, embedding, indexing) and the online query pipeline. Key patterns: hybrid search combining dense retrieval (vector similarity) with sparse retrieval (BM25 keyword matching) via Reciprocal Rank Fusion. Reranking with cross-encoder models that score query-document pairs jointly.

**Documentation:**

- Anthropic Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval
- Anthropic Cookbook RAG: https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/
- OpenAI Cookbook RAG with Pinecone: https://cookbook.openai.com/examples/vector_databases/pinecone/gen_qa
- Prompt Engineering Guide RAG: https://www.promptingguide.ai/research/rag

#### 4.3 Graph Traversal and Knowledge Graph Querying

Exploiting structured relationships for multi-hop reasoning that pure vector search cannot achieve. Covers natural language to Cypher query translation (Neo4j's GraphCypherQAChain pattern), Microsoft GraphRAG's four query modes (Global Search, Local Search, DRIFT Search, Basic Search), and combining graph traversal results with vector retrieval results for superior retrieval quality.

**Documentation:**

- LlamaIndex KG RAG Query Engine: https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/
- Neo4j GenAI Ecosystem: https://neo4j.com/labs/genai-ecosystem/

#### 4.4 Hybrid Retrieval and Reranking

Combining multiple retrieval strategies for optimal results. Dense retrieval (vector similarity) finds semantically related content; sparse retrieval (BM25) finds exact keyword matches; graph traversal finds structurally related content. Reciprocal Rank Fusion merges results from multiple sources. Cross-encoder reranking re-scores the top candidates to select the final context. This layered approach consistently outperforms any single retrieval method.

**Documentation:**

- Anthropic Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval

---

### Section 5: Memory

How AI systems maintain state across interactions. Memory is a cross-cutting concern that intersects with persistence, retrieval, and context engineering, but the engineering patterns are distinct enough to warrant dedicated treatment.

#### 5.1 Short-Term Memory: Conversation History

The most basic form of memory: maintaining the message list within a single session. Covers in-memory message list management, the last-N-messages approach, and the interaction between conversation history and context window limits. This is the default "memory" that every chat application implements.

**Documentation:**

- LangGraph Memory: https://docs.langchain.com/oss/python/langgraph/add-memory

#### 5.2 Working Memory: Agent Scratchpad

Intermediate state held during a single task execution. Covers scratchpad patterns for holding active task state, tool results, intermediate reasoning, and transient data that the agent needs during processing but that does not persist beyond the current task. Working memory is what enables multi-step reasoning within a single agent run.

#### 5.3 Long-Term Memory: Cross-Session Persistence

Persisting information across sessions using external storage. Covers vector-database-backed recall of past interactions, key-value stores for user preferences, and graph databases for relationship-rich knowledge. Key engineering patterns: memory summarisation (LLM-condenses history when context fills up), "hot path" vs. "background" memory formation, and hybrid retrieval combining semantic search with structured queries for memory recall.

**Documentation:**

- LangMem Conceptual Guide: https://langchain-ai.github.io/langmem/concepts/conceptual_guide/
- Redis AI Agent Memory Management: https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/

**Reference Repos:**

- `mem0ai/mem0`: https://github.com/mem0ai/mem0
- `langchain-ai/langmem`: https://github.com/langchain-ai/langmem

#### 5.4 Memory Summarisation and Compression

Using LLMs to condense conversation history and stored memories into compact representations. Covers progressive summarisation (summarising older messages while keeping recent ones verbatim), hierarchical summarisation (summaries of summaries for very long histories), and intelligent memory filtering (deciding what is worth remembering and what can be discarded).

---

### Section 6: Orchestration

How to build agents and coordinate them. This section progresses from the simplest agentic pattern (an LLM with a tool) to complex multi-agent systems with dynamic task decomposition.

#### 6.1 Tool and Function Definition

Enabling LLMs to interact with external systems by defining structured tool schemas. Both OpenAI and Anthropic implement this via a `tools` parameter with JSON Schema definitions. Covers schema design, `strict` mode (OpenAI), parallel tool calls, and `tool_choice` for controlling tool invocation. This is the gateway to building agents.

**Documentation:**

- OpenAI Function Calling Guide: https://developers.openai.com/api/docs/guides/function-calling/
- Anthropic Tool Use Overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Anthropic Implement Tool Use: https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use
- Anthropic Advanced Tool Use: https://www.anthropic.com/engineering/advanced-tool-use

**Code Examples:**

- OpenAI Cookbook Function Calling: https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models

#### 6.2 Tool Execution Loops

The core agentic pattern: send message with tools, LLM requests tool call, execute tool locally, append result, call API again, repeat until final response. Covers the `while` loop structure, parallel tool call handling, error reporting via tool result content, and termination conditions. This is the irreducible unit of agency.

**Documentation:**

- OpenAI Function Calling (loop pattern): https://developers.openai.com/api/docs/guides/function-calling/
- Anthropic Implement Tool Use (agentic loop): https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use

**Reference Repos:**

- `openai/openai-agents-python`: https://github.com/openai/openai-agents-python

#### 6.3 Building Simple Agents with the ReAct Pattern

The foundational agent: an LLM running in a loop with tools, following the Think, Act, Observe cycle. Covers the ReAct paradigm, termination conditions (final answer, max iterations, stop signals), and Anthropic's guidance that production agents use simple, composable patterns rather than complex frameworks.

**Documentation:**

- Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic Cookbook Agent Patterns: https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- ReAct Paper: https://arxiv.org/abs/2210.03629

**Reference Repos:**

- `openai/openai-agents-python`: https://github.com/openai/openai-agents-python
- `openai/swarm`: https://github.com/openai/swarm

#### 6.4 Narrow-Task Agent Nodes with Predefined Schemas

Single-purpose LLM calls with strict input and output schemas (Pydantic models). Each node performs one specific transformation: classification, extraction, summarisation, or routing. Unlike general-purpose agents, these are deterministic in structure with guaranteed output shape. Enables composability, testability, and reliability. The Instructor library is the de facto standard for this pattern.

**Documentation:**

- OpenAI Structured Outputs: https://openai.com/index/introducing-structured-outputs-in-the-api/
- Instructor Response Models: https://python.useinstructor.com/concepts/models/

**Reference Repos:**

- `jxnl/instructor`: https://github.com/jxnl/instructor
- `pydantic/pydantic-ai`: https://github.com/pydantic/pydantic-ai

#### 6.5 Routing and Classification

Using an LLM or embedding model to classify incoming requests and direct them to specialised sub-systems. Semantic routing uses embedding similarity for sub-millisecond decisions without an LLM call. LLM-based classification uses structured output for richer routing decisions. In production, routing enables cost optimisation (simple queries to cheaper models) and specialisation (domain queries to domain agents).

**Documentation:**

- Semantic Router: https://github.com/aurelio-labs/semantic-router
- RouteLLM Blog: https://lmsys.org/blog/2024-07-01-routellm/
- Anthropic Structured Outputs (for classification): https://platform.claude.com/docs/en/build-with-claude/structured-outputs

**Reference Repos:**

- `aurelio-labs/semantic-router`: https://github.com/aurelio-labs/semantic-router
- `lm-sys/RouteLLM`: https://github.com/lm-sys/RouteLLM

#### 6.6 Agent Orchestration: Sequential, Parallel, and Conditional Workflows

Structured control flow for multi-step LLM operations. Anthropic's five workflow patterns: prompt chaining (sequential pipeline with optional gates), routing (classify to specialised handlers), parallelisation (concurrent subtasks), orchestrator-workers (central LLM delegates dynamically), and evaluator-optimiser (iterative refinement). This is "agents on rails": LLM intelligence within deterministic, debuggable execution paths.

**Documentation:**

- Anthropic Building Effective Agents (5 workflow patterns): https://www.anthropic.com/research/building-effective-agents
- OpenAI Agents SDK Multi-Agent Orchestration: https://openai.github.io/openai-agents-python/multi_agent/

**Code Examples:**

- Anthropic Cookbook Agent Patterns: https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
- OpenAI Agents SDK Pattern Examples: https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns

#### 6.7 Static vs. Dynamic Task Decomposition

The spectrum from predefined pipelines to runtime-determined task graphs. Static decomposition (prompt chaining) offers predictability; dynamic decomposition (orchestrator-workers) offers flexibility. Advanced approaches: plan-then-execute, iterative refinement, and ADAPT (recursive decomposition only when simpler execution fails). Production systems typically use a hybrid: static scaffolding with dynamic flexibility at specific decision points.

**Documentation:**

- Anthropic Orchestrator-Workers and Prompt Chaining: https://www.anthropic.com/research/building-effective-agents

**Reference Repos:**

- `crewAIInc/crewAI`: https://github.com/crewAIInc/crewAI
- `microsoft/autogen`: https://github.com/microsoft/autogen

#### 6.8 Multi-Agent Systems with Isolated Context Windows

Coordinating multiple specialised LLM agents, each with isolated context, tools, and instructions. Supervisor/manager pattern (central orchestrator invokes sub-agents as tools) vs. handoff/peer pattern (agents transfer control). Key concerns: context isolation, communication (message passing vs. shared state), and state management.

**Documentation:**

- OpenAI Agents SDK Multi-Agent: https://openai.github.io/openai-agents-python/multi_agent/
- OpenAI Swarm README: https://github.com/openai/swarm/blob/main/README.md

**Reference Repos:**

- `openai/openai-agents-python`: https://github.com/openai/openai-agents-python
- `openai/swarm`: https://github.com/openai/swarm
- `crewAIInc/crewAI`: https://github.com/crewAIInc/crewAI
- `microsoft/autogen`: https://github.com/microsoft/autogen

#### 6.9 Human-in-the-Loop Patterns

Pausing agent workflows at critical decision points to collect human approval, rejection, or feedback. Covers approval workflows, confidence-based routing (auto-escalation below a threshold), return-of-control (editable parameters for human modification), and interactive feedback loops. Workflows can wait hours, days, or weeks for human input.

**Documentation:**

- LangGraph HITL: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- LangGraph Interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- Cloudflare Agents HITL: https://developers.cloudflare.com/agents/guides/human-in-the-loop/

---

### Section 7: Tooling and Protocols

Specific protocols, interfaces, and environments through which agents interact with the external world.

#### 7.1 MCP (Model Context Protocol)

The open standard (Anthropic, now Linux Foundation) for connecting LLM applications to external data and tools. Client-server architecture on JSON-RPC 2.0. Three primitives: Tools (executable functions), Resources (data sources), and Prompts (reusable templates). Two transports: stdio (local) and Streamable HTTP (remote with SSE). Covers lifecycle management, capability negotiation, and dynamic discovery.

**Documentation:**

- MCP Official Documentation: https://modelcontextprotocol.io/docs/getting-started/intro
- MCP Architecture: https://modelcontextprotocol.io/docs/learn/architecture
- MCP Specification: https://modelcontextprotocol.io/specification/2025-11-25
- MCP Build a Server: https://modelcontextprotocol.io/docs/develop/build-server
- Anthropic MCP Connector: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector

**Reference Repos:**

- `modelcontextprotocol/python-sdk`: https://github.com/modelcontextprotocol/python-sdk
- `modelcontextprotocol/typescript-sdk`: https://github.com/modelcontextprotocol/typescript-sdk
- `modelcontextprotocol/servers`: https://github.com/modelcontextprotocol/servers

#### 7.2 CLI-Based Tool Interfaces for Agents

Giving LLM agents direct access to shell commands, file systems, and development toolchains. The agent generates bash commands or file edits, the host executes with permission checks, captures output, and feeds results back. Covers Claude Code's sandboxing model (OS-level primitives), OpenAI Codex CLI, and configurable permission modes.

**Documentation:**

- Claude Code Sandboxing: https://code.claude.com/docs/en/sandboxing
- Anthropic Engineering Sandboxing: https://www.anthropic.com/engineering/claude-code-sandboxing
- OpenAI Codex CLI: https://developers.openai.com/codex/cli

**Reference Repos:**

- `anthropics/claude-code`: https://github.com/anthropics/claude-code
- `Aider-AI/aider`: https://github.com/Aider-AI/aider

#### 7.3 Slash Commands and Agent Skills

Discrete, modular capabilities invoked on demand. Slash commands are Markdown-based prompts stored in `.claude/commands/`. Agent Skills are the evolved successor: standardised `SKILL.md` packages supporting progressive disclosure (lightweight metadata first, full instructions on demand). Skills use a discovery-then-load pattern and work across Claude Code, OpenAI Codex, GitHub Copilot, Cursor, and VS Code.

**Documentation:**

- Claude Code Slash Commands / Skills: https://code.claude.com/docs/en/slash-commands
- Anthropic Agent Skills Overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI Codex Skills: https://developers.openai.com/codex/skills/

**Reference Repos:**

- `wshobson/commands`: https://github.com/wshobson/commands
- `skillmatic-ai/awesome-agent-skills`: https://github.com/skillmatic-ai/awesome-agent-skills

#### 7.4 Agent Sandboxing in Isolated Environments

Executing AI-generated code within isolated environments. Covers microVMs (Firecracker/E2B for strongest isolation), gVisor (Modal for syscall interception), and standard containers (Docker). E2B provides cloud sandboxes with sub-second provisioning; Modal offers Python-first DX with autoscaling; Docker provides local container-level isolation.

**Documentation:**

- E2B Documentation: https://e2b.dev/docs
- Modal Sandboxes: https://modal.com/docs/guide/sandboxes
- Docker Sandboxes for Coding Agents: https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/

**Reference Repos:**

- `e2b-dev/E2B`: https://github.com/e2b-dev/E2B
- `kubernetes-sigs/agent-sandbox`: https://github.com/kubernetes-sigs/agent-sandbox

#### 7.5 Lightweight AI Function Patterns (Marvin)

Treating LLMs as typed function calls. `marvin.extract()` pulls typed entities from text, `marvin.cast()` converts freeform text into Pydantic models, `marvin.classify()` maps text to enum labels, and `@marvin.fn` creates AI-powered functions defined only by signature and docstring. The broader pattern: LLMs as deterministic software components with typed inputs and outputs, using decorators for AI-powered behaviour.

**Documentation:**

- Marvin Documentation: https://askmarvin.ai/welcome

**Reference Repos:**

- `PrefectHQ/marvin`: https://github.com/PrefectHQ/marvin
- `jxnl/instructor`: https://github.com/jxnl/instructor

---

### Section 8: QA and Observability

How to ensure quality, measure performance, and monitor AI systems in production.

#### 8.1 Evaluation (Evals) for LLM Systems

Systematically measuring LLM output quality. The eval-driven development pattern: define eval suites before building features. Covers code-based grading (exact match, regex), LLM-as-judge (stronger model scores against rubrics), and human evaluation. Eval suites consist of input prompts, golden answers, grading criteria, and scoring methods.

**Documentation:**

- Anthropic Eval Guidance: https://docs.anthropic.com/en/docs/empirical-performance-evaluations
- Anthropic Demystifying Evals for AI Agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic Building Evals Cookbook: https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb

**Reference Repos:**

- `confident-ai/deepeval`: https://github.com/confident-ai/deepeval
- `promptfoo/promptfoo`: https://github.com/promptfoo/promptfoo
- `openai/evals`: https://github.com/openai/evals
- User's own evals framework: https://github.com/leobeeson/query-preprocessing-workflow/tree/master/evals

#### 8.2 Tracing and Observability for LLM Applications

Instrumenting AI applications to understand production behaviour. Traces are hierarchical records of all operations in a request lifecycle. Covers Langfuse (open-source, MIT/Apache 2.0), OpenLLMetry (auto-instruments via OpenTelemetry), and Phoenix (Arize AI). The OpenTelemetry Semantic Conventions for GenAI are converging as the vendor-neutral standard.

**Documentation:**

- Langfuse Observability Overview: https://langfuse.com/docs/observability/overview
- Langfuse OpenTelemetry Integration: https://langfuse.com/integrations/native/opentelemetry

**Reference Repos:**

- `langfuse/langfuse`: https://github.com/langfuse/langfuse
- `traceloop/openllmetry`: https://github.com/traceloop/openllmetry
- `Arize-ai/phoenix`: https://github.com/Arize-ai/phoenix

#### 8.3 Guardrails and Safety

Validation and control layers between users and models. Input guardrails detect prompt injection, jailbreaks, off-topic queries, and PII. Output guardrails filter toxic content, prevent data leakage, and check for hallucinations. Covers NVIDIA NeMo Guardrails (Colang), OpenAI Guardrails Python (drop-in client replacement), and defence-in-depth strategies.

**Documentation:**

- NVIDIA NeMo Guardrails: https://docs.nvidia.com/nemo/guardrails/latest/index.html
- OpenAI Guardrails Python: https://openai.github.io/openai-guardrails-python/

**Code Examples:**

- OpenAI Guardrails Cookbook: https://developers.openai.com/cookbook/examples/how_to_use_guardrails

**Reference Repos:**

- `NVIDIA-NeMo/Guardrails`: https://github.com/NVIDIA-NeMo/Guardrails
- `guardrails-ai/guardrails`: https://github.com/guardrails-ai/guardrails
- `openai/openai-guardrails-python`: https://github.com/openai/openai-guardrails-python

#### 8.4 Error Handling and Retry Strategies

Resilience patterns for LLM API calls. Rate limits (HTTP 429), server errors (500/503), timeouts, and invalid requests. Exponential backoff with jitter using `tenacity`. Fallback strategies (alternative providers on failure), circuit breaker (stop retrying after N consecutive failures), and Retry-After header honouring.

**Documentation:**

- OpenAI Rate Limits Handling: https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits/
- Anthropic Rate Limits: https://docs.anthropic.com/en/api/rate-limits
- Instructor Retry Documentation: https://python.useinstructor.com/concepts/retrying/

**Reference Repos:**

- `jd/tenacity`: https://github.com/jd/tenacity

#### 8.5 Rate Limiting and Concurrency Management

Client-side throttling for API rate limits (RPM, TPM, TPD). Covers token bucket, sliding window, and fixed window patterns. Python implementation with `asyncio.Semaphore` and `asyncio.gather()`. Anthropic's cached tokens not counting against ITPM limits. OpenAI's Batch API at 50% discount for non-urgent workloads.

**Documentation:**

- OpenAI Rate Limits: https://platform.openai.com/docs/guides/rate-limits
- Anthropic Rate Limits: https://docs.anthropic.com/en/api/rate-limits

**Reference Repos:**

- `BerriAI/litellm`: https://github.com/BerriAI/litellm
- `mjpieters/aiolimiter`: https://github.com/mjpieters/aiolimiter

#### 8.6 Prompt Versioning and A/B Testing

Treating prompts as critical infrastructure with version control, testing, staged rollouts, and monitoring. Prompt registries (versioned, tagged, served via API), A/B testing (graduated rollouts: 5%, 25%, 100%), and CI/CD integration (automated regression testing with promptfoo). The lifecycle: develop, version, test, deploy with staged rollouts, monitor, iterate.

**Documentation:**

- promptfoo: https://github.com/promptfoo/promptfoo

**Reference Repos:**

- `promptfoo/promptfoo`: https://github.com/promptfoo/promptfoo
- `langfuse/langfuse`: https://github.com/langfuse/langfuse

#### 8.7 Response Caching at the Application Level

Caching LLM responses to reduce cost and latency. Exact match caching (SHA-256 hashing of prompts, stored in Redis) and semantic caching (embedding-based similarity matching with cosine threshold). Research shows 31% of LLM queries exhibit semantic similarity to previous requests. Combined with provider-level prompt caching, total savings can exceed 80%.

**Documentation:**

- GPTCache Documentation: https://gptcache.readthedocs.io/

**Reference Repos:**

- `zilliztech/GPTCache`: https://github.com/zilliztech/GPTCache

---

### Section 9: Cloud Providers

Platform-specific implementations for deploying AI systems on managed infrastructure.

#### 9.1 Building with Google Gemini and Vertex AI

Google's Gemini API: chat, function calling, structured output, multimodal inputs, and built-in tools (Google Search grounding, code execution). Key differences from OpenAI/Anthropic: `generateContent` endpoint, OpenAPI 3.0 schema for structured outputs, `functionDeclarations` within tools arrays, and "thought signatures" in Gemini 3 for maintaining reasoning context across multi-turn function calling.

**Documentation:**

- Gemini Structured Output: https://ai.google.dev/gemini-api/docs/structured-output
- Gemini Function Calling: https://ai.google.dev/gemini-api/docs/function-calling
- Gemini Tools and Agents: https://ai.google.dev/gemini-api/docs/tools
- Vertex AI Function Calling: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling

#### 9.2 Building with AWS Bedrock

Amazon Bedrock's unified interface for multiple foundation models. The Converse API provides a consistent message-based interface across all models. Covers Bedrock's agent framework (build-time configuration, runtime orchestration via `InvokeAgent`), Knowledge Bases (S3, databases, embedding models, vector stores), guardrails, prompt management, and streaming via `ConverseStream`.

**Documentation:**

- Bedrock Converse API: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
- How Bedrock Agents Work: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html
- Bedrock Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

**Code Examples:**

- Amazon Bedrock Samples: https://aws-samples.github.io/amazon-bedrock-samples/introduction-to-bedrock/converse_api/01_converse_api/

---

## Section Dependency Graph

```txt
Foundations
    |
    v
Context Engineering
    |
    +---> Data Persistence ---> Retrieval ---> Memory
    |                                            |
    v                                            v
Orchestration <----------------------------------+
    |
    v
Tooling and Protocols
    |
    v
QA and Observability
    |
    v
Cloud Providers
```

**Reading the graph:**

- **Foundations** is prerequisite for everything.
- **Context Engineering** builds directly on Foundations and is prerequisite for all subsequent sections.
- **Data Persistence**, **Retrieval**, and **Memory** form a vertical chain (each builds on the previous).
- **Orchestration** depends on Context Engineering and Memory (agents need to manage context and state).
- **Tooling and Protocols** builds on Orchestration (protocols are how agents interact with the world).
- **QA and Observability** can be taught in parallel with later sections but is best introduced after Orchestration, so there are meaningful systems to evaluate and observe.
- **Cloud Providers** is standalone and can be taught at any point after Foundations, but is best placed last as a capstone showing how all concepts map to managed services.

---

## Cross-Cutting Reference Repositories

These repositories span multiple sections and serve as foundational learning resources:

| Repository | Primary Value |
|---|---|
| `openai/openai-python` | Official SDK, de facto API standard |
| `anthropics/anthropic-sdk-python` | Official SDK with streaming helpers |
| `openai/openai-cookbook` | Comprehensive code examples across all topics |
| `anthropics/anthropic-cookbook` | Agent patterns, RAG, evals, tool use |
| `openai/openai-agents-python` | Reference agent loop, multi-agent, handoffs |
| `BerriAI/litellm` | Provider-agnostic access, cost tracking |
| `jxnl/instructor` | Structured outputs via Pydantic |
| `langfuse/langfuse` | Open-source observability and prompt management |
| `modelcontextprotocol/python-sdk` | MCP server/client implementation |
| `microsoft/graphrag` | Graph-based RAG reference |
| `stanfordnlp/dspy` | Programmatic prompt optimisation |
