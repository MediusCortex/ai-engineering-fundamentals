# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "python-dotenv",
# ]
# ///

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import Response


load_dotenv()


class OpenAIClient:

    def __init__(
        self,
        model: str,
        system_prompt: str,
    ) -> None:
        self.client: OpenAI = OpenAI()
        self.model: str = model
        self.system_prompt: str = system_prompt
        self.conversation_history: list[dict[str, str]] = []


    def send_message(
        self,
        message: str,
    ) -> str:
        user_message: dict[str, str] = {
            "role": "user",
            "content": message,
        }
        self.conversation_history.append(user_message)
        response: Response = self.client.responses.create(
            model=self.model,
            instructions=self.system_prompt,
            input=self.conversation_history,
        )
        response_text: str = response.output_text
        assistant_message: dict[str, str] = {
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
    client: OpenAIClient = OpenAIClient(
        model="gpt-5-nano",
        system_prompt=system_prompt,
    )
    first_response: str = client.send_message(
        message="What running shoes do you recommend for marathon training?"
    )
    print(first_response)
    print()
    second_response: str = client.send_message(
        message="Tell me more about the cushioning technology in your top pick."
    )
    print(second_response)


if __name__ == "__main__":
    main()
