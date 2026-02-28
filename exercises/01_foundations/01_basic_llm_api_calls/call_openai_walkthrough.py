# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "python-dotenv",
# ]
# ///

# This walkthrough explores the OpenAI Responses API step by step.
# Run it top-to-bottom, or execute line-by-line in VSCode's interactive window (Shift+Enter).

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import Response, ResponseOutputItem, ResponseOutputMessage, ResponseOutputText

load_dotenv()

# =============================================================================
# 1. Create the client
# =============================================================================
# The OpenAI client reads OPENAI_API_KEY from the environment automatically.
client: OpenAI = OpenAI()

# =============================================================================
# 2. Send a request using the Responses API
# =============================================================================
# The Responses API is OpenAI's recommended API for new projects.
# Unlike Anthropic, `input` accepts a simple string (no messages list needed for single-turn).
# `max_tokens` is not required; the model uses sensible defaults.
message: str = "What should I look for when choosing a marathon running shoe?"
response: Response = client.responses.create(
    model="gpt-5-nano",
    input=message,
)

# =============================================================================
# 3. Inspect the full response object
# =============================================================================
print("=====================\nFull Raw Response:\n=====================\n")
# The response is an `openai.types.responses.Response` object.
# It contains output items (the actual response) and metadata (model, usage, status).
print(f"```json\n{response.model_dump_json(indent=2)}\n```")

# =============================================================================
# 4. Inspect response metadata
# =============================================================================
print("\n=====================\nResponse Metadata:\n=====================\n")
print(f"Model:         {response.model}")
print("  ^ The model that generated the response.\n")

print(f"Status:        {response.status}")
print("  ^ Completion status: 'completed', 'failed', 'incomplete', 'in_progress', or 'cancelled'.\n")

# Token usage determines cost. Input tokens are what you sent; output tokens are what the model generated.
if response.usage is not None:
    print(f"Input tokens:  {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Total tokens:  {response.usage.total_tokens}")
    print("  ^ Token counts determine API cost. Output tokens cost 3 to 8x more than input tokens.")

# =============================================================================
# 5. Inspect response output items
# =============================================================================
print("\n=====================\nResponse Output:\n=====================\n")
# The response output is a list of typed output items.
# Item types include ResponseOutputMessage, ResponseFunctionToolCall, and others.
print(f"This response contains {len(response.output)} output item(s):\n")

all_output_items: list[ResponseOutputItem] = response.output
for i, item in enumerate(all_output_items):
    index: int = i
    item_type: str = type(item).__name__
    print(f"[{index}] type={item_type}:\n```json\n{item.model_dump_json(indent=2)}\n```")

# =============================================================================
# 6. Extract the message content
# =============================================================================
print("\n---------------------\nMessage Output Item:\n---------------------\n")
# The output list can contain multiple item types (e.g. ResponseReasoningItem for
# reasoning models like gpt-5-nano, ResponseFunctionToolCall for tool use, etc.).
# We search for the ResponseOutputMessage, which contains the actual text response.
output_message: ResponseOutputMessage | None = None
for item in all_output_items:
    if isinstance(item, ResponseOutputMessage):
        output_message = item
        break
assert output_message is not None

# The message contains a `content` list. Each content item can be
# a ResponseOutputText (text) or ResponseOutputRefusal (refusal).
first_content = output_message.content[0]
assert isinstance(first_content, ResponseOutputText)
text_content: ResponseOutputText = first_content
print(f"```json\n{text_content.model_dump_json(indent=2)}\n```")

# =============================================================================
# 7. Extract the final text (the easy way)
# =============================================================================
print("\n=====================\nResponse Text:\n=====================\n")
# The `response.output_text` property aggregates all text from output items,
# so you do not need to navigate the output structure manually.
response_text: str = response.output_text
print(f"```txt\n{response_text}\n```\n")
