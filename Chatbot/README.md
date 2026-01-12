# RAG Chatbot with Gradio GUI
A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on your local documents using Ollama and LangChain.
<img width="790" height="393" alt="image" src="https://github.com/user-attachments/assets/4df3849f-f2fa-4793-a708-df393b6d8944" />

## Features
- Chat interface powered by Gradio
- Uses local LLM (Llama 3.2) via Ollama
- Vector database storage with ChromaDB
- Retrieves relevant context from documents before answering

## Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running

## Installation
1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Pull required Ollama models:
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Setup
1. Place documents in a `data/` folder

2. Run the ingestion script to create the vector database:
```bash
python ingest.py
```

3. Start Ollama (in a separate terminal):
```bash
ollama serve
```

4. Launch the chatbot:
```bash
python app.py
```

5. Open your browser to `http://localhost:7860`

## Project Structure

```
.
├── app.py           # Main chatbot application with Gradio GUI
├── ingest.py        # Script to process documents and create vector DB
├── chroma_db/       # Vector database storage (created after ingestion)
└── data/            # Your source documents
└── requirements.txt
```

## Usage

1. Type your question in the text box
2. Click "Send" or press Enter
3. The chatbot will retrieve relevant context from your documents and generate an answer
4. Use "Clear Chat" to start a new conversation

## Configuration

You can modify these parameters in `app.py`:

- `model`: Change LLM model (default: `llama3.2`)
- `temperature`: Control response randomness (default: `0` for deterministic)
- `k`: Number of documents to retrieve (default: `4`)

## Troubleshooting

**Error: Connection refused to localhost:11434**
- Make sure Ollama is running: `ollama serve`
- Verify models are installed: `ollama list`

**No relevant answers**
- Check that documents were ingested properly
- Verify `chroma_db/` directory exists and contains data
- Try increasing the `k` parameter for more context retrieval

## Below attempts belong to testing.py code. The main app is still under construction.
### Primary attempt:
Using: https://www.gradio.app/main/guides/creating-a-custom-chatbot-with-blocks#a-simple-chatbot-demo
The current code is a bot that only responds with a random motivational message. 
The logic: bot_message is the function that returns the message. We append the user's message, sleep for 1 message simulating a delay, then the bot's, and finally return the data. There is also a Clear button.
### Working example below:
<img width="845" height="278" alt="image" src="https://github.com/user-attachments/assets/918800fa-8702-47e1-8838-d9b2b1f3f16a" />

### My second attempt:
Using https://www.gradio.app/main/guides/creating-a-custom-chatbot-with-blocks#add-streaming-to-your-chatbot
UI has tweaks added to it, basic functionality remains the same. Using a for loop & "yield" keyword, chatbot typing effect is added. Print user's input immediately. Have immediate response using "queue=False" in the "msg.submit" portion.
Ran into issue with ClearButton, it doesn't initialize with any text (as confirmed by docs).
### Working example below:
<img width="794" height="281" alt="image" src="https://github.com/user-attachments/assets/589cc96c-4d09-4f6d-8f37-70a055a7a026" />


## Target local RAG Workflow
PDF text, Chunking, Embedding each chunk (e.g., nomic), Store in vector DB (e.g., ChromaDB), User query → embedded, Vector similarity search, Top-K relevant chunks, LLM answer grounded in those chunks (e.g., Llama 3.2).
