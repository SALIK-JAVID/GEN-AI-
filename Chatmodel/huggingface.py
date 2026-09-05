from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
# these are the hugging face classes we can use this or the first one , just have to add the model provider in the first case
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
llm = HuggingFaceEndpoint ( 
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
)
model= ChatHuggingFace(llm=llm)
response = model.invoke("what is RAG in simple terms?")
print(response.content)
