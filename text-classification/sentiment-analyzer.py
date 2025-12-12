# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
import torch

# Load a pre-trained sentiment analysis model
# cannot have the full path if pushing the code to Hugging Face Hub
analyzer = pipeline("text-classification", 
               model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
# model_path = "C:/Users/msherif/PycharmProjects/GenAIProjects/text-classification/sentiment-model"
# pipe = pipeline("text-classification", 
#                 model=model_path)

print(analyzer(["This is a good product",
                 "This was a very expensive product."])
    )

def sentiment_analysis(review):
    sentiment = analyzer(review)
    return sentiment