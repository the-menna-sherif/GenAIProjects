# Current state
Facing issues with my Gradio GUI. Abandoning complex code and starting from success. Many issues with Gradio, considering alternatives & refreshing knowledge of Langchain. Code is functional. Working on a new GUI since Gradio is being excessively difficult.

### Below attempts belong to testing.py code. The main app is still under construction.
## Primary attempt:
Using: https://www.gradio.app/main/guides/creating-a-custom-chatbot-with-blocks#a-simple-chatbot-demo
The current code is a bot that only responds with a random motivational message. 
The logic: bot_message is the function that returns the message. We append the user's message, sleep for 1 message simulating a delay, then the bot's, and finally return the data. There is also a Clear button.
### Working example below:
<img width="845" height="278" alt="image" src="https://github.com/user-attachments/assets/918800fa-8702-47e1-8838-d9b2b1f3f16a" />

## My second attempt:
Using https://www.gradio.app/main/guides/creating-a-custom-chatbot-with-blocks#add-streaming-to-your-chatbot
UI has tweaks added to it, basic functionality remains the same. Using a for loop & "yield" keyword, chatbot typing effect is added. Print user's input immediately. Have immediate response using "queue=False" in the "msg.submit" portion.
Ran into issue with ClearButton, it doesn't initialize with any text (as confirmed by docs).
### Working example below:
<img width="794" height="281" alt="image" src="https://github.com/user-attachments/assets/589cc96c-4d09-4f6d-8f37-70a055a7a026" />


## Target local RAG Workflow
PDF text, Chunking, Embedding each chunk (e.g., nomic), Store in vector DB (e.g., ChromaDB), User query → embedded, Vector similarity search, Top-K relevant chunks, LLM answer grounded in those chunks (e.g., Llama 3.2).
