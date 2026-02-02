from langchain_core.documents import Document
import arxiv
from pprint import pp

def paper_with_ID(query: str, k: int):
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

query = "Attention Is All You Need"
docs = paper_with_ID(query, k=2)
pp([doc.metadata["title"] for doc in docs])
