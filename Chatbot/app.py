import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

DB_DIR = "chroma_db"

# Load the QA chain
def load_qa_chain():
    #  Initialize embeddings using Ollama & embedding model from Nomic (context: 8k, 0.1B parameters, open-source)
    # Recall embedding models convert text into numerical vectors 
    # to search through data and find most relevant info to feed to LLM (here: llama3.2)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")


    #  Load the vector database from Chroma
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

    # Create RetrievalQA chain combining LLM and retriever
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False 
        # Set to True to return source documents along with answers (helps in debugging)
    )

# Load the QA chain
qa_chain = load_qa_chain()

def chat(query, history):
    result = qa_chain(query)
    answer = result["result"]
    history.append((query, answer))
    return history, history

# Blocks is a top level container to put things in rows & columns
with gr.Blocks(title="📄 Local PDF RAG Chatbot") as demo:
    gr.Markdown("# 📄 Chat with Your PDFs (Local RAG)")
    gr.Markdown("Ask questions grounded only in your local PDF documents.")

    # Initialize chatbot section where history will be displayed
    chatbot = gr.Chatbot(height=500)

    # hidden variable which stores the conversation history
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(
            show_label=False,
            placeholder="Ask me something about your documents..."
        )

    # "txt.submit": when the user submits a query (txt), call the chat function whichcontains the llama logic (pressing enter-> submit) 
    # also update the chatbot and state
    txt.submit(chat, [txt, state], [chatbot, state])

    # Clear textbox after submission by setting its value to empty string using a lambda function
    # a UX polish line
    txt.submit(lambda: "", None, txt)

demo.launch()
