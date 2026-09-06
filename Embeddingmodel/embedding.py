from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings (
    model = "Qwen/Qwen3-Embedding-0.6B"
)
vector = embedding.embed_query("what is Artificial Intelligence")
print(vector)
print("vector dimensions:", len(vector))