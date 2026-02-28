# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic",
#     "python-dotenv",
# ]
# ///

# This walkthrough explores system prompts, user messages, and conversation history with Anthropic step by step.
# Run it top-to-bottom, or execute line-by-line in VSCode's interactive window (Shift+Enter).

import json

from anthropic import Anthropic
from anthropic.types import Message, MessageParam, TextBlock
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# 1. Create the client
# =============================================================================
# The Anthropic client reads ANTHROPIC_API_KEY from the environment automatically.
client: Anthropic = Anthropic()

# =============================================================================
# 2. Define a system prompt
# =============================================================================
# A system prompt sets the model's persona, capabilities, and constraints.
# Anthropic passes the system prompt as a SEPARATE `system` parameter,
# not inside the `messages` list. This clearly separates instructions from conversation.
system_prompt: str = (
    "You are a customer service assistant for Acme Running, a premium running shoe "
    "company. You help customers with product information, order enquiries, and "
    "general support. Be friendly, professional, and concise."
)

# =============================================================================
# 3. Send a single message with a system prompt
# =============================================================================
print("=====================\nSingle Turn with System Prompt:\n=====================\n")
# The `system` parameter goes directly on the API call, separate from `messages`.
# The `messages` list contains only user and assistant turns.
messages: list[MessageParam] = [
    {
        "role": "user",
        "content": "What running shoes do you recommend for marathon training?",
    }
]

response: Message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    system=system_prompt,
    messages=messages,
)
first_block = response.content[0]
assert isinstance(first_block, TextBlock)
response_text: str = first_block.text
print(f"```txt\n{response_text}\n```\n")

# =============================================================================
# 4. Compare with and without a system prompt
# =============================================================================
print("\n=====================\nSame Question Without System Prompt:\n=====================\n")
# Without a system prompt, the model responds as a general assistant
# rather than an Acme Running customer service agent.
response_no_system: Message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=messages,
)
first_block_no_system = response_no_system.content[0]
assert isinstance(first_block_no_system, TextBlock)
response_text_no_system: str = first_block_no_system.text
print(f"```txt\n{response_text_no_system}\n```\n")
print("  ^ Without a system prompt, the model gives generic running shoe advice.")
print("    With the Acme Running system prompt, it stays in character as a brand representative.\n")

# =============================================================================
# 5. Build a multi-turn conversation
# =============================================================================
print("\n=====================\nMulti-turn Conversation:\n=====================\n")
# The API is stateless: each request must include the FULL conversation history.
# We build the history by appending user and assistant messages after each turn.
# In production, you would manage this list carefully, applying truncation or
# sliding window strategies when conversations grow long (covered in Lesson 1.6).
conversation: list[MessageParam] = [
    {
        "role": "user",
        "content": "What running shoes do you recommend for marathon training?",
    },
    {
        "role": "assistant",
        "content": response_text,
    },
    {
        "role": "user",
        "content": "Tell me more about the cushioning technology in your top pick.",
    },
]

# Show the conversation structure being sent to the API.
print("Messages sent to the API:\n")
conversation_dump: str = json.dumps(
    obj=conversation,
    indent=2,
)
print(f"```json\n{conversation_dump}\n```\n")
print(f"  ^ {len(conversation)} messages in the conversation history.")
print("    The API sees the full context, so it can answer follow-up questions.\n")

# =============================================================================
# 6. Send the multi-turn conversation
# =============================================================================
print("\n---------------------\nAssistant Response (Turn 2):\n---------------------\n")
# The model uses the full conversation history to understand "your top pick"
# refers to whatever shoe it recommended in its first response.
multi_turn_response: Message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    system=system_prompt,
    messages=conversation,
)
multi_turn_block = multi_turn_response.content[0]
assert isinstance(multi_turn_block, TextBlock)
multi_turn_text: str = multi_turn_block.text
print(f"```txt\n{multi_turn_text}\n```\n")

# =============================================================================
# 7. Assistant pre-filling for output steering
# =============================================================================
print("\n=====================\nAssistant Pre-filling:\n=====================\n")
# Anthropic supports a unique technique: include a partial assistant message
# at the END of the messages list. The model continues from where you left off,
# letting you steer the output format without elaborate prompt instructions.
prefilled_messages: list[MessageParam] = [
    {
        "role": "user",
        "content": "List three Acme Running shoes suitable for beginners.",
    },
    {
        "role": "assistant",
        "content": "Here are three Acme Running shoes for beginners:\n\n1.",
    },
]

prefilled_response: Message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    system=system_prompt,
    messages=prefilled_messages,
)
prefilled_block = prefilled_response.content[0]
assert isinstance(prefilled_block, TextBlock)
prefilled_text: str = prefilled_block.text

# The response continues from where the pre-fill left off.
# We concatenate the pre-fill with the model's continuation to get the full output.
full_response: str = "Here are three Acme Running shoes for beginners:\n\n1." + prefilled_text
print(f"```txt\n{full_response}\n```\n")
print("  ^ The model continued from '1.' in the pre-filled assistant message.")
print("    Pre-filling is useful for enforcing numbered lists, JSON output, or specific formats.\n")
