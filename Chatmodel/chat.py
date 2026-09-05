from dotenv import load_dotenv

load_dotenv() 
# Initializing the model 
from langchain.chat_models import init_chat_model

model = init_chat_model("openai/gpt-oss-120b", model_provider="groq", temperature=0, max_token = 30 )
response = model.invoke("who is salik?")
print(response.content)