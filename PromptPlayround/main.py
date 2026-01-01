import gradio as gr
import requests

# Prompt templates per task
PROMPT_TEMPLATES = {
    "summarization": [
        "Summarize the following text:\n\n{text}",
        "Give a bullet-point summary:\n\n{text}",
        "Write a very short summary:\n\n{text}",
    ],
    "classification": [
        "Classify the sentiment of this text:\n\n{text}",
        "What is the main topic?\n\n{text}",
        "Assign one category to this text:\n\n{text}",
    ],
    "extraction": [
        "Extract named entities:\n\n{text}",
        "Extract key facts:\n\n{text}",
        "List important keywords:\n\n{text}",
    ],
}

# Call local Ollama model
def call_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
        },
    )
    return response.json()["response"].strip()

# Run selected task with three prompts
def run_task(text: str, task: str):
    outputs = []
    for template in PROMPT_TEMPLATES[task]:
        outputs.append(call_llm(template.format(text=text)))
    return outputs[0], outputs[1], outputs[2]

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Multi-Prompt LLM Comparison")

    text_input = gr.Textbox(lines=6, label="Input Text")
    task_selector = gr.Dropdown(
        ["summarization", "classification", "extraction"],
        value="summarization",
        label="Task",
    )
    run_button = gr.Button("Run")

    with gr.Row():
        out1 = gr.Textbox(label="Prompt 1")
        out2 = gr.Textbox(label="Prompt 2")
        out3 = gr.Textbox(label="Prompt 3")

    run_button.click(
        run_task,
        inputs=[text_input, task_selector],
        outputs=[out1, out2, out3],
    )

# Launch app
if __name__ == "__main__":
    demo.launch()