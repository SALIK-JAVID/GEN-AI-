from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model (
    "openai/gpt-oss-120b", model_provider="groq"
)

# saving the context by saving the prompt and the response.content
messages  = [

]
print("--------------------👋🏻 WELCOME, Type 0 to exit the chat--------------------")
while True :
    
    prompt = input("You : ")
    messages.append(prompt)
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(response.content)
    print("Chat Bot: " , response.content)
    
else : 
    print("")


print(messages)


