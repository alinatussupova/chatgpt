import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


class Chatbot:
    def __init__(self):
        openai.api_key = api_key

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens = 3000,
            temperature = 0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about flowers.")
    print(response)