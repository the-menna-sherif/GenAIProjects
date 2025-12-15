# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
import torch
import pandas as pd
import matplotlib.pyplot as plt

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

# function to create a bar chart from sentiment analysis results
def sentiment_bar_chart(df):
    sentiment_counts = df['Sentiment'].value_counts().reset_index()
    
    # create a bar chart
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='pie', ax=ax, color=['skyblue', 'salmon'])
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title('Sentiment Analysis Results')
    # ax.set_xticklabels(['Negative','Positive'], rotation=0)

    # debugging
    print(type(sentiment_counts))
    print(sentiment_counts)
    print(sentiment_counts.columns if hasattr(sentiment_counts, "columns") else "No columns")

    return fig

# function to read reviews from excel file and analyze sentiment
# modified to accept file object from Gradio File input (no code change- just file_path to file_object)
def read_reviews_analyze_sentiment(file_object):
    # load excel file into dataframe
    df = pd.read_excel(file_object)

    # check if review column exists in DF
    if 'Review' not in df.columns:
        raise ValueError("The provided file does not contain a 'review' column.")
    
    # apply sentiment analysis on each review
    df['Sentiment'] = df['Review'].apply(sentiment_analyzer)

    chart_obj = sentiment_bar_chart(df)
    return df, chart_obj

# Prototype Gradio interface, input is a textbox, output is a textbox (based on single review analysis)
demo = gr.Interface(
    fn=sentiment_analyzer,
    inputs=[gr.Textbox(label="Enter your review here", lines=4)],
    outputs=[gr.Textbox(label="Sentiment", lines=1)],
    title="@GenAI Project 3: Sentiment Analyzer",
    description="Analyze the sentiment based on provided comments."
)


# Dynamic gradio interface, input is a review excel, output is a pandas dataframe 
# (based on multiple reviews analyses)
demo_dynamic = gr.Interface(
    fn=read_reviews_analyze_sentiment,
    inputs=[gr.File(file_types=[".xlsx"],label="Upload your review file")],
    outputs=[gr.DataFrame(label="Sentiments")],
    title="@GenAI Project 3: Sentiment Analyzer",
    description="Analyze the sentiment based on provided review file uploaded."
)

# Extended dynamic gradio interface, input is a review excel, output is a pandas dataframe and a bar chart
# (based on multiple reviews analyses)
demo_graphic = gr.Interface(
    fn=read_reviews_analyze_sentiment,
    inputs=[gr.File(file_types=[".xlsx"],label="Upload your review file")],
    outputs=[gr.DataFrame(label="Sentiments"), gr.Plot(label="Sentiment Analysis Chart")],
    title="@GenAI Project 3: Sentiment Analyzer",
    description="Analyze the sentiment based on provided review file uploaded."
)

# demo.launch()
# demo_dynamic.launch()

demo_graphic.launch()

file_path = r"C:\Users\msherif\PycharmProjects\GenAIProjects\text-classification\Files\sample_reviews.xlsx"
# the relative path would look like this:
# file_path = r"./Files/sample_reviews.xlsx"
# result = read_reviews_analyze_sentiment(file_path)
# print(result)