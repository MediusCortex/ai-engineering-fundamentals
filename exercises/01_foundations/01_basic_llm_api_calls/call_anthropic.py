# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic",
#     "python-dotenv",
# ]
# ///

from anthropic import Anthropic
from anthropic.types import TextBlock
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    client: Anthropic = Anthropic()
    message: str = "What should I look for when choosing a marathon running shoe?"
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )
    first_block = response.content[0]
    assert isinstance(first_block, TextBlock)
    response_text: str = first_block.text
    print(response_text)


if __name__ == "__main__":
    main()
