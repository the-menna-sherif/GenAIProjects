from langchain_ollama import OllamaEmbeddings
import ollama
import retrieval
from sklearn.metrics.pairwise import cosine_similarity


def embed_rank(query: str, k: int):
    ############# Embedding and Retrieval #############

    # Embed the query
    query_embedding = OllamaEmbeddings(model="nomic-embed-text").embed_query(query)

    # Retrieve documents
    docs = retrieval.paper_with_ID(query, k)
    
    # build list of (id, text) pairs
    id_and_text = [[doc.metadata["id"], doc.page_content] for doc in docs]
    # separate ids and texts
    texts = [content for doc_id, content in id_and_text]
    ids = [doc_id for doc_id, content in id_and_text]

    # Embed all retrieved documents
    vector_embeddings = OllamaEmbeddings(model="nomic-embed-text").embed_documents(texts)
    # list of dictionaries: {'id': '...', 'embedding': [...]}
    id_to_embedding = {
    doc_id: vector 
    for doc_id, vector in zip(ids, vector_embeddings)
    }

    # Attach embeddings to documents
    for doc in docs:
        doc_id = doc.metadata.get("id")
        
        if doc_id in id_to_embedding:
            doc.metadata["embedding"] = id_to_embedding[doc_id]
            print(f"Embedded document ID: {doc_id}")
        else:
            print(f"Warning: No embedding found for document ID: {doc_id}")

    print(f"Successfully embedded {len(id_to_embedding)} documents.")
    # print(f"First ID: {id_to_embedding[0]['id']}")

    ############# Ranking & scoring #############
    for doc in docs:
        doc_emb = doc.metadata["embedding"]
        if doc_emb is None:
            raise ValueError(f"No embedding found for doc {doc.metadata.get('id')}")
        doc.metadata["score"] = cosine_similarity([query_embedding], [doc_emb])[0][0]

    # Sort documents by score in descending order
    docs.sort(key=lambda x: x.metadata["score"], reverse=True)
    print("Documents ranked by relevance score, the top documents are:")
    for i, doc in enumerate(docs[:2]):  # Print top 2 documents' titles and scores
        print(f"Rank {i+1}: {doc.metadata['title']} (Score: {doc.metadata['score']:.2f})")

    return docs


def main(query: str,k: int):
    print(f"In main of ranking.py, with query: {query}, k: {k} ")
    print("##########################################################")
    docs = embed_rank(query, k=k)

if __name__=="__main__":
    main("RSA", k=5)