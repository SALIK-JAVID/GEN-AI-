from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model  = init_chat_model (
    "openai/gpt-oss-20b",
    model_provider="groq"
)
response = model.invoke("who is Mariyah?")
print(response.content)