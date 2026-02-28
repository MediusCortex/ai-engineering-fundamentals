# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "python-dotenv",
# ]
# ///

from openai import OpenAI
from openai.types.responses import Response
from dotenv import load_dotenv


load_dotenv()


class OpenAIClient:

    def __init__(
        self,
        model: str,
    ) -> None:
        self.client: OpenAI = OpenAI()
        self.model: str = model


    def send_message(
        self,
        message: str,
    ) -> str:
        response: Response = self.client.responses.create(
            model=self.model,
            input=message,
        )
        response_text: str = response.output_text
        return response_text


def main() -> None:
        message: str = "What should I look for when choosing a marathon running shoe?"
        client: OpenAIClient = OpenAIClient(model="gpt-5-nano")
        response: str = client.send_message(message=message)
        print(response)


if __name__ == "__main__":
    main()
