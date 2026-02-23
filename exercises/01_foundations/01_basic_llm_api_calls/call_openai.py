# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "python-dotenv",
# ]
# ///

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()
    client: OpenAI = OpenAI()
    message: str = "What should I look for when choosing a marathon running shoe?"
    response = client.responses.create(
        model="gpt-4o-mini",
        input=message,
    )
    response_text: str = response.output_text
    print(response_text)


if __name__ == "__main__":
    main()
