from dotenv import load_dotenv
load_dotenv()

from wrapper import LLMClient

# teste les deux providers
for provider in ["groq", "gemini"]:
    llm = LLMClient(provider=provider)
    reponse = llm.chat([{"role": "user", "content": "Dis bonjour en une phrase"}])
    print(f"{provider} : {reponse}")