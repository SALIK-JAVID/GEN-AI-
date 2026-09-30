from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model (
    "openai/gpt-oss-120b", model_provider="groq"
)
response = model.invoke("what is machine learning? in a simple sentence")
print(response.content)