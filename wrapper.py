import os

from groq import Groq
from google import genai


class LLMClient:

    def __init__(self, provider):

        self.provider = provider

        if provider == "groq":

            self.model = "llama-3.3-70b-versatile"

            self.client = Groq(
                api_key=os.getenv("GROQ_API_KEY")
            )

        elif provider == "gemini":

            self.model = "gemini-2.5-flash"

            self.client = genai.Client(
                api_key=os.getenv("GEMINI_API_KEY")
            )

        else:
            raise ValueError(
                f"Provider inconnu : {provider}"
            )

    def chat(self, messages):

        if self.provider == "groq":

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            return response.choices[0].message.content

        elif self.provider == "gemini":

            prompt = messages[-1]["content"]

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text