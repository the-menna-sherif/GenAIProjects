import torch
import gradio as gr
# Using pipeline as a high-level helper
from transformers import pipeline

text_summary = pipeline(task="summarization", model="sshleifer/distilbart-cnn-12-6",
                torch_dtype=torch.bfloat16) # This compresses the model, without degrading performance

# text = "A fairy (also called fay, fae, fae folk, fey, fair folk, or faerie) is a type of mythical being or legendary creature, generally described as anthropomorphic, found in the folklore of multiple European cultures (including Celtic, Slavic, Germanic, and French folklore), a form of spirit, often with magical, metaphysical, supernatural, or preternatural qualities. Myths and stories about fairies do not have a single origin but are rather a collection of folk beliefs from disparate sources. Various folk theories about the origins of fairies include casting them as either demoted angels or demons in a Christian tradition, as deities in pagan belief systems, as spirits of the dead, as prehistoric precursors to humans, or as spirits of nature."
# print(text_summary(text))

def summarize(text):
    output = text_summary(text)
    return output[0]['summary_text']

gr.close_all()
# demo = gr.Interface(fn=summarize, inputs="text", outputs="text")
demo = gr.Interface(summarize,
                    inputs=[gr.Textbox(label="Enter text to summarize",lines=6)],
                    outputs=[gr.Textbox(label="Summarized text",lines=4)],
                    title="GenAI Project 1: Text Summarizer",
                    description="This app summarizes text using LLMs",
                    )
demo.launch()