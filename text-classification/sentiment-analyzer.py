# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
import torch

model_path = r"C:\Users\msherif\PycharmProjects\GenAIProjects\venv\Models\models--distilbert--distilbert-base-uncased-finetuned-sst-2-english"

# Load a pre-trained sentiment analysis model
# cannot have the full path if pushing the code to Hugging Face Hub
# pipe = pipeline("text-classification", 
               # model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
analyzer = pipeline("text-classification", 
                model=model_path)

print(analyzer(["This is a good product",
                 "This was a very expensive product."
                 ]
                 ))