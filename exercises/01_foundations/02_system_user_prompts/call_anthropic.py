# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic",
#     "python-dotenv",
# ]
# ///

from anthropic import Anthropic
from anthropic.types import Message, MessageParam, TextBlock
from dotenv import load_dotenv


load_dotenv()


class AnthropicClient:

    def __init__(
        self,
        model: str,
        system_prompt: str,
        max_tokens: int = 1024,
    ) -> None:
        self.client: Anthropic = Anthropic()
        self.model: str = model
        self.system_prompt: str = system_prompt
        self.max_tokens: int = max_tokens
        self.conversation_history: list[MessageParam] = []


    def send_message(
        self,
        message: str,
    ) -> str:
        user_message: MessageParam = {
            "role": "user",
            "content": message,
        }
        self.conversation_history.append(user_message)
        response: Message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.conversation_history,
        )
        first_block = response.content[0]
        assert isinstance(first_block, TextBlock)
        response_text: str = first_block.text
        assistant_message: MessageParam = {
            "role": "assistant",
            "content": response_text,
        }
        self.conversation_history.append(assistant_message)
        return response_text


def main() -> None:
    system_prompt: str = (
        "You are a customer service assistant for Acme Running, a premium running shoe "
        "company. You help customers with product information, order enquiries, and "
        "general support. Be friendly, professional, and concise."
    )
    client: AnthropicClient = AnthropicClient(
        model="claude-haiku-4-5-20251001",
        system_prompt=system_prompt,
    )
    first_response: str = client.send_message(
        message="What running shoes do you recommend for marathon training, and which is your top pick?"
    )
    print(f"FIRST RESPONSE:\n\n{first_response}\n")
    print()
    second_response: str = client.send_message(
        message="Tell me more about the cushioning technology in your top pick."
    )
    print(f"SECOND RESPONSE:\n\n{second_response}\n")


if __name__ == "__main__":
    main()
