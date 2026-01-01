# LLM Prompt Comparator 

A minimal Python-based tool to systematically compare how different prompt engineering techniques affect LLM outputs. This project allows you to test the same input against three distinct prompt templates side-by-side using Gradio and an LLM API.

## Architecture

The system follows a linear flow to ensure reproducibility and clear comparison:

**User Input** → **Prompt Templates** → **LLM API** → **Output Comparison** → **Display Results**

## Components

* **Input Box:** Accepts raw text (articles, product reviews, or messy data).
* **Task Selector:** A dropdown to choose between **Summarization**, **Classification**, or **Extraction**.
* **Prompt Engine:** Applies three unique strategies (e.g., Zero-shot, Few-shot, and Chain-of-Thought) to the input.
* **LLM Integration:** Handles the API calls to the model provider.
* **Side-by-Side UI:** A Gradio interface to view results and compare quality instantly.

## Objectives

By building and using this tool, you gain practical experience in:

* **Prompt Patterns:** Discovering why "Chain-of-Thought" instructions often yield higher accuracy than simple "Zero-shot" requests.
* **Output Control:** Learning how to force LLMs into specific formats (like JSON) and identifying which instructions are most effective at preventing "prose chatter."
* **Reliability Testing:** Seeing how the same model can fail or succeed on the same data just by changing the phrasing of the instruction.
* **Rapid Prototyping:** Using Gradio to build internal tools that let non-technical stakeholders test and validate AI behaviors.

## Output:
Testing the classification option:
<img width="1906" height="568" alt="image" src="https://github.com/user-attachments/assets/7e506399-ce44-4a73-a31a-ffe6a9d8d9c6" />

## Next Steps

* **System Prompts:** Add a field to modify the "System Role" (e.g., "You are a legal expert") to see how persona impacts quality.
* **Temperature Slider:** Add a Gradio slider to test how randomness (Temperature) affects the consistency of the three prompts.
* **Batch Export:** Add an "Export to CSV" feature to save your favorite prompt/result pairs for future fine-tuning.
