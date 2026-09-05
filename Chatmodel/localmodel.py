from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/SmolLM2-135M-Instruct",
    task="text-generation",
    model_kwargs={
        "device_map": "auto",
    },
    # pipeline keyword argument 
    pipeline_kwargs={
        "max_new_tokens": 100,
        "do_sample": False,
    },
)
chat_model = ChatHuggingFace(llm = llm )
response = chat_model.invoke("What is Machine learning?")
print(response.content)