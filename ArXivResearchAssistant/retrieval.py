from langchain_community.retrievers import ArxivRetriever

retriever = ArxivRetriever(
    load_max_docs=2,
    get_full_documents=True,
)

docs = retriever.invoke("Graph Neural Networks")
docs[0].metadata