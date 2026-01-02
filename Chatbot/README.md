## Local RAG Workflow

PDF text

   ↓

Chunking

   ↓

Embedding each chunk (e.g., nomic)
   
   ↓

Store in vector DB (e.g., ChromaDB)
   
   ↓

User query → embedded
   
   ↓

Vector similarity search
   
   ↓

Top-K relevant chunks
   
   ↓

LLM answer grounded in those chunks (e.g., Llama 3.2)
