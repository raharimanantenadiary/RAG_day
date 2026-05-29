import os

from groq import Groq
from google import genai


def test_groq():
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Dis bonjour"
            }
        ]
    )

    print("Groq :", response.choices[0].message.content)


def test_gemini():
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Dis bonjour"
    )

    print("Gemini :", response.text)


if __name__ == "__main__":
    test_groq()
    test_gemini()