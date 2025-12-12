# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
import torch
import pandas as pd

# Load a pre-trained sentiment analysis model
# cannot have the full path if pushing the code to Hugging Face Hub
analyzer = pipeline("text-classification", 
               model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
# model_path = "C:/Users/msherif/PycharmProjects/GenAIProjects/text-classification/sentiment-model"
# pipe = pipeline("text-classification", 
#                 model=model_path)

# print(analyzer(["This is a good product",
#                  "This was a very expensive product."])
#     )

def sentiment_analyzer(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

demo = gr.Interface(
    fn=sentiment_analyzer,
    inputs=[gr.Textbox(label="Enter your review here", lines=4)],
    outputs=[gr.Textbox(label="Sentiment", lines=1)],
    title="@GenAI Project 3: Sentiment Analyzer",
    description="Analyze the sentiment based on provided comments."
)
# demo.launch()

file_path = "C:/Users/msherif/PycharmProjects/GenAIProjects/text-classification/reviews.xlsx"

def read_reviews_analyze_sentiment(file_path):
    # load excel file into dataframe
    df = pd.read_excel(file_path)

    # check if review column exists in DF
    if 'Review' not in df.columns:
        raise ValueError("The provided file does not contain a 'review' column.")
    
    # apply sentiment analysis on each review
    df['Sentiment'] = df['Review'].apply(sentiment_analyzer)
    return df

file_path = r"text-classification\Files\sample_reviews.xlsx"
result = read_reviews_analyze_sentiment(file_path)
print(result)