# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "python-dotenv",
# ]
# ///

# This walkthrough explores system instructions, user messages, and conversation history with OpenAI step by step.
# Run it top-to-bottom, or execute line-by-line in VSCode's interactive window (Shift+Enter).

import json

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import Response
from openai.types.responses.response_input_item_param import ResponseInputItemParam

load_dotenv()

# =============================================================================
# 1. Create the client
# =============================================================================
# The OpenAI client reads OPENAI_API_KEY from the environment automatically.
client: OpenAI = OpenAI()

# =============================================================================
# 2. Define system instructions
# =============================================================================
# System instructions set the model's persona, capabilities, and constraints.
# In the Responses API, the system prompt is a SEPARATE `instructions` parameter,
# similar to Anthropic's `system` parameter. (In the older Chat Completions API,
# it was a message with role "system" inside the messages array.)
system_prompt: str = (
    "You are a customer service assistant for Acme Running, a premium running shoe "
    "company. You help customers with product information, order enquiries, and "
    "general support. Be friendly, professional, and concise."
)

# =============================================================================
# 3. Send a single message with system instructions
# =============================================================================
print("=====================\nSingle Turn with System Instructions:\n=====================\n")
# The `instructions` parameter goes directly on the API call.
# For a single turn, `input` can still be a simple string (as in Lesson 1.1).
message: str = "What running shoes do you recommend for marathon training, and which is your top pick?"
response: Response = client.responses.create(
    model="gpt-5-nano",
    instructions=system_prompt,
    input=message,
)
response_text: str = response.output_text
print(f"```txt\n{response_text}\n```\n")

# =============================================================================
# 4. Compare with and without system instructions
# =============================================================================
print("\n=====================\nSame Question Without System Instructions:\n=====================\n")
# Without system instructions, the model responds as a general assistant
# rather than an Acme Running customer service agent.
response_no_system: Response = client.responses.create(
    model="gpt-5-nano",
    input=message,
)
response_text_no_system: str = response_no_system.output_text
print(f"```txt\n{response_text_no_system}\n```\n")
print("  ^ Without system instructions, the model gives generic running shoe advice.")
print("    With the Acme Running instructions, it stays in character as a brand representative.\n")

# =============================================================================
# 5. Build a multi-turn conversation
# =============================================================================
print("\n=====================\nMulti-turn Conversation:\n=====================\n")
# The API is stateless: each request must include the FULL conversation history.
# For multi-turn, pass `input` as a list of role/content items instead of a string.
# In production, you would manage this list carefully, applying truncation or
# sliding window strategies when conversations grow long (covered in Lesson 1.6).
follow_up_message: str = "Tell me more about the cushioning technology in your top pick."
conversation: list[ResponseInputItemParam] = [
    {
        "role": "user",
        "content": message,
    },
    {
        "role": "assistant",
        "content": response_text,
    },
    {
        "role": "user",
        "content": follow_up_message,
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
multi_turn_response: Response = client.responses.create(
    model="gpt-5-nano",
    instructions=system_prompt,
    input=conversation,
)
multi_turn_text: str = multi_turn_response.output_text
print(f"```txt\n{multi_turn_text}\n```\n")

# =============================================================================
# 7. Without history, context is lost
# =============================================================================
print("\n=====================\nWithout Conversation History:\n=====================\n")
# To demonstrate the stateless nature: send only the follow-up question
# without any prior context. The model cannot know what "your top pick" means.
isolated_message: str = follow_up_message
response_no_history: Response = client.responses.create(
    model="gpt-5-nano",
    instructions=system_prompt,
    input=isolated_message,
)
response_text_no_history: str = response_no_history.output_text
print(f"```txt\n{response_text_no_history}\n```\n")
print("  ^ Without conversation history, the model has no context for 'your top pick'.")
print("    The API is stateless: you must send the full conversation each time.\n")
