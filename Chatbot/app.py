import gradio as gr
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

DB_DIR = "chroma_db"

# Load the QA chain
def load_qa_chain():
    # Initialize embeddings using Ollama & embedding model from Nomic (context: 8k, 0.1B parameters, open-source)
    # Embedding models convert text into numerical vectors 
    # to search through data and find most relevant info to feed to LLM (here: llama3.2)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Load the vector database from Chroma
    # Vector DB stores embeddings of documents for efficient retrieval
    vectordb = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings # Embedding function initialized above (nomic-embed-text)
    )    
    # Create retriever from vector database
    # Retriever fetches relevant documents based on user queries to provide context for LLM
    retriever = vectordb.as_retriever(
        search_kwargs={"k": 4} # Number of documents to retrieve (default is 4)
    )
    # Initialize Ollama LLM for generating answers
    llm = Ollama(
        model="llama3.2",
        temperature=0 # 0 for deterministic responses
    )

    # Create RetrievalQA chain combining LLM and retriever to be returned
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False 
        # Set to True to return source documents along with answers (helps in debugging)
    )

# Load the QA chain
qa_chain = load_qa_chain()

# def chat(query, history):
#     # Run the chain and extract the answer
#     # history is passed by Gradio as a list of lists or dicts
#     result = qa_chain.invoke(
#         {"query": query}
#         )
#     answer = result["result"]
    
#     # Gradio's Chatbot expects the full updated history back
#     history.append((query, answer))
#     return "", history

if __name__ == "__main__":
   load_qa_chain() # function call to test loading the QA chain fails when loading GUI

# print("#######################################################################")
# print("QA Chain type:", type(qa_chain)) #  <class 'langchain_classic.chains.retrieval_qa.base.RetrievalQA'>

#     # Define the user function to update chat history
# def user(user_message, history: list):
#     return "", history + [{
#         "role": "user",
#             "content": user_message
#         }]

