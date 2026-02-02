from langchain_ollama import OllamaEmbeddings
import ollama
import retrieval

def embed_rank_generate(query: str, k: int):
    
    docs = retrieval.paper_with_ID(query, k=4)
    # 
    id_and_text = [[doc.metadata["id"], doc.page_content] for doc in docs]
    texts = [content for doc_id, content in id_and_text]
    ids = [doc_id for doc_id, content in id_and_text]

    # Embed all retrieved documents
    vector_embeddings = OllamaEmbeddings(model="nomic-embed-text").embed_documents(texts)
    # list of dictionaries: {'id': '...', 'embedding': [...]}
    id_to_embedding = [
        {"id": doc_id, "embedding": vector} 
        for doc_id, vector in zip(ids, vector_embeddings)
    ]

    print(f"Successfully embedded {len(id_to_embedding)} documents.")
    print(f"First ID: {id_to_embedding[0]['id']}")

    # Generate llm's output
    output = ollama.generate(
    model="llama3.2",
    prompt=f"Using this data: {id_to_embedding}. Respond to this prompt: {query}"
    )

    print(output['response'])


query = "Attention Is All You Need"
k=4
embed_rank_generate(query, k)