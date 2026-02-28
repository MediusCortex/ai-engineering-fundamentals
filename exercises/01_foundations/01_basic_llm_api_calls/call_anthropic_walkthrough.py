# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic",
#     "python-dotenv",
# ]
# ///

# This walkthrough explores the Anthropic Messages API step by step.
# Run it top-to-bottom, or execute line-by-line in VSCode's interactive window (Shift+Enter).

from anthropic import Anthropic
from anthropic.types import ContentBlock, Message, MessageParam, TextBlock
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# 1. Create the client
# =============================================================================
# The Anthropic client reads ANTHROPIC_API_KEY from the environment automatically.
client: Anthropic = Anthropic()

# =============================================================================
# 2. Build the request
# =============================================================================
# The `messages` parameter is a list of MessageParam dicts with "role" and "content" keys.
message: str = "What should I look for when choosing a marathon running shoe?"
messages: list[MessageParam] = [
    {
        "role": "user",
        "content": message,
    }
]

# Anthropic requires `max_tokens` explicitly, unlike OpenAI which uses model-specific defaults.
response: Message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=messages,
)

# =============================================================================
# 3. Inspect the full response object
# =============================================================================
print("=====================\nFull Raw Response:\n=====================\n")
# The response is an `anthropic.types.Message` object.
# It contains content blocks (the actual response) and metadata (model, usage, stop reason).
print(f"```json\n{response.model_dump_json(indent=2)}\n```")

# =============================================================================
# 4. Inspect response metadata
# =============================================================================
print("\n=====================\nResponse Metadata:\n=====================\n")
print(f"Model:         {response.model}")
print("  ^ The actual model snapshot used in the request.\n")

# Why the model stopped generating: "end_turn" (natural stop), "max_tokens" (hit the limit),
# or "tool_use" (the model wants to call a tool, covered in later lessons).
print(f"Stop reason:   {response.stop_reason}")
print("  ^ Why the model stopped: 'end_turn' (finished naturally), 'max_tokens' (hit the limit),")
print("    or 'tool_use' (wants to call a tool, covered in later lessons).\n")

# Token usage determines cost. Input tokens are what you sent; output tokens are what the model generated.
print(f"Input tokens:  {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print("  ^ Token counts determine API cost. Output tokens cost 3 to 8x more than input tokens.")

# =============================================================================
# 5. Inspect response content blocks
# =============================================================================
print("\n=====================\nResponse Content:\n=====================\n")
# The response content is a list of typed content blocks.
# Block types include TextBlock, ToolUseBlock, and ThinkingBlock.
print(f"This response contains {len(response.content)} content block(s):\n")

all_content_blocks: list[ContentBlock] = response.content
for i, block in enumerate(all_content_blocks):
    index: int = i
    block_type: str = type(block).__name__
    print(f"[{index}] type={block_type}:\n```json\n{block.model_dump_json(indent=2)}\n```")

# =============================================================================
# 6. Extract the first content block
# =============================================================================
print("\n---------------------\nFirst Content Block:\n---------------------\n")
# Extracting the first block. Since it could be any block type,
# we use `isinstance` to verify it is a TextBlock before accessing `.text`.
first_block = all_content_blocks[0]
assert isinstance(first_block, TextBlock)
text_block: TextBlock = first_block
print(f"```json\n{text_block.model_dump_json(indent=2)}\n```")

# =============================================================================
# 7. Extract the final text
# =============================================================================
print("\n=====================\nResponse Text:\n=====================\n")
# The final text is in `text_block.text`.
response_text: str = text_block.text
print(f"```txt\n{response_text}\n```\n")
