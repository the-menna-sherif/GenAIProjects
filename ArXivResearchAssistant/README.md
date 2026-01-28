# ArXiv Research Assistant with LLMOps + Safety Guardrails

## Goal
Build an AI assistant where users ask a research question and it returns the Top x most relevant ArXiv papers, with:

• RAG (Retrieval-Augmented Generation)

• LLMOps pipeline

• Safety + quality guardrails

• Monitoring + evaluation

## Flow
User Question 

   ↓

Query Guardrails → ArXiv Search → Embed + Rank → LLM Summarizer

   ↓

Output Guardrails → Logging → Monitoring → Feedback Loop

## Components/ Techstack 
### ArXiv Retrieval
Use:
• arXiv API / Semantic Scholar API

Steps:
• Convert question → search query
• Fetch top N papers (e.g., 20)
• Extract title, abstract, authors, link

### Ranking + Relevance
Embed abstracts: OpenAI / SentenceTransformers
Rank by: Cosine similarity to user question then pick Top 3

### LLM Summarization
For each paper: Short summary + Relevance + Key contribution

### LLMOps pipeline
Prompt Versioning

Store prompt templates:
• search prompt
• summarization prompt
• relevance explanation prompt

### Safety Guardrails
#### Input:
Block:
• Prompt injection
• Malicious instructions
• NSFW queries
#### Output:
Ensure:
• Papers are real (verify IDs/links)
• No hallucinated citations
• No unsafe content

### Feedback Loop
Users rate:
Helpful / Not helpful

→ Use bad samples for:
• Prompt tuning
• Ranking improvements

### Monitoring & Evaluation
Log:
• Queries
• Papers returned
• Clicks / feedback
• Hallucination rate
• Relevance score

Use:
• LangSmith / W&B / OpenTelemetry

## Project structure
arxiv_gui_assistant/
├── app.py                # Streamlit UI
├── retrieval.py         # arXiv API
├── ranking.py           # embeddings + cosine sim
├── llm.py               # summarization
├── guardrails.py        # safety checks
├── prompts/
├── monitoring.py
└── requirements.txt
