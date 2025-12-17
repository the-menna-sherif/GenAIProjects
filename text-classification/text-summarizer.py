import torch
import gradio as gr
# Using pipeline as a high-level helper
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import os

model = "sshleifer/distilbart-cnn-12-6"

# Load tokenizer & model locally
tokenizer = AutoTokenizer.from_pretrained(
    model,
    local_files_only=True
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    model,
    torch_dtype=torch.float16,
    local_files_only=True
)
text_summary = pipeline(task="summarization", model=model,
                dtype =torch.float16, tokenizer=tokenizer) 

def summarize(text):
    output = text_summary(text)
    return output[0]['summary_text']

# gr.close_all()
demo = gr.Interface(fn=summarize,
                    inputs=[gr.Textbox(label="Enter text to summarize",lines=6)],
                    outputs=[gr.Textbox(label="Summarized text",lines=4)],
                    title="GenAI Project 1: Text Summarizer",
                    description="This app summarizes text using LLMs",
                    )
demo.launch()
