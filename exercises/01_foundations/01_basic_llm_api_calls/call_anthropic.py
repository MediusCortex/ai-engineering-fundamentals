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
        max_tokens: int = 1024,
    ) -> None:
        self.client: Anthropic = Anthropic()
        self.model: str = model
        self.max_tokens: int = max_tokens


    def send_message(
        self,
        message: str,
    ) -> str:
        messages: list[MessageParam] = [
            {
                "role": "user",
                "content": message,
            }
        ]
        response: Message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=messages,
        )
        first_block = response.content[0]
        assert isinstance(first_block, TextBlock)
        response_text: str = first_block.text
        return response_text


def main() -> None:
    message: str = "What should I look for when choosing a marathon running shoe?"
    client: AnthropicClient = AnthropicClient(model="claude-haiku-4-5-20251001")
    response: str = client.send_message(message=message)
    print(response)


if __name__ == "__main__":
    main()
