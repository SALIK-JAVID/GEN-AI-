from langchain_community.document_loaders import TextLoader
# creating a document loader 
loader = TextLoader("RAG-project/Documentloaders/notes.txt", encoding="utf-8")

# load the document 
documents = loader.load()

# print the loaded documents 
# print(documents)

# every document has these 2 things!
print(documents[0].metadata)
print(documents[0].page_content)