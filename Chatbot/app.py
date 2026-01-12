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

def chat(message, history):
    """
    Process user message and return response.
    
    Args:
        message: Current user message
        history: List of message dictionaries from previous conversation
    
    Returns:
        Updated chat history
    """
    try:
        response = qa_chain.invoke({"query": message})
        bot_response = response["result"]
    except Exception as e:
        bot_response = f"Error: {str(e)}"
    
    # Append user message
    history.append({"role": "user", "content": message})
    # Append bot response
    history.append({"role": "assistant", "content": bot_response})
    
    return history
    

# Create Gradio interface
with gr.Blocks(title="RAG Chatbot") as demo:
    gr.Markdown("# RAG Chatbot")
    gr.Markdown("Ask questions about your documents!")
    
    chatbot = gr.Chatbot(
        height=500,
    )
    
    with gr.Row():
        msg = gr.Textbox(
            label="Your Question",
            placeholder="Type your question here...",
            scale=4
        )
        submit = gr.Button("Send", scale=1, variant="primary")
    
    with gr.Row():
        clear = gr.Button("Clear Chat")
    
    gr.Markdown("---")
    gr.Markdown("**Note:** This chatbot uses the local documents only.")
    
    # Handle message submission
    def respond(message, chat_history):
        if not message.strip():
            return chat_history, ""
        
        updated_history = chat(message, chat_history)
        return updated_history, ""
    
    # Event handlers
    msg.submit(respond, [msg, chatbot], [chatbot, msg])
    submit.click(respond, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot, queue=False)


if __name__ == "__main__":
#    load_qa_chain() # function call to test loading the QA chain fails when loading GUI
    demo.launch(
        share=False  # Set to True if you want a public link
    )
print("success")