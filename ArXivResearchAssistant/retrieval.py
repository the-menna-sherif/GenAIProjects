from langchain_core.documents import Document
import arxiv
from pprint import pp

# function to retrieve papers from arXiv with their IDs and metadata sorted by relevance
# returns list of Document objects with metadata including arXiv ID, title, authors, published date, and pdf_url
def paper_with_ID(query: str, k: int): # should grab ~100 papers in PROD run
    search = arxiv.Search(query=query, max_results=k, sort_by=arxiv.SortCriterion.Relevance)
    docs = []
    for d in search.results():
        docs.append(
            Document(
                page_content=d.summary,
                metadata={
                    "id": d.entry_id,
                    "title": d.title,
                    "authors": [a.name for a in d.authors],
                    "published": str(d.published),
                    "pdf_url": d.pdf_url,
                }
            )
        )
    return docs

def main(query: str,k: int):
    print(f"In main of retrieval.py, with query: {query}, k: {k} ")
    print("##########################################################")
    docs = paper_with_ID(query, k=k)
    # pp([doc.metadata for doc in docs])
    # pp([[doc.metadata["id"], doc.page_content] for doc in docs])
    # pp([doc.page_content for doc in docs])

if __name__=="__main__":
    main("RSA", k=20)