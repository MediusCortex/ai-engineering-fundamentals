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
from openai.types.responses.response_input_item_param import ResponseInputItemParam


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
        self.conversation_history: list[ResponseInputItemParam] = []


    def send_message(
        self,
        message: str,
    ) -> str:
        user_message: ResponseInputItemParam = {
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
        assistant_message: ResponseInputItemParam = {
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
