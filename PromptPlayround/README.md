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

## Ollama:
Brought local Ollama up first using: ollama serve
```java
time=2026-01-01T13:16:22.436+02:00 level=INFO source=routes.go:1511 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GGML_VK_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\msherif\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:1 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_REMOTES:[ollama.com] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES:]"
time=2026-01-01T13:16:22.521+02:00 level=INFO source=images.go:522 msg="total blobs: 10"
time=2026-01-01T13:16:22.525+02:00 level=INFO source=images.go:529 msg="total unused blobs removed: 0"
time=2026-01-01T13:16:22.529+02:00 level=INFO source=routes.go:1564 msg="Listening on 127.0.0.1:11434 (version 0.12.6)"
time=2026-01-01T13:16:22.530+02:00 level=INFO source=runner.go:80 msg="discovering available GPUs..."
time=2026-01-01T13:17:00.640+02:00 level=INFO source=types.go:112 msg="inference compute" id=GPU-fca79cd3-6d51-cc21-2d1c-dabe294d0f2f library=CUDA compute=7.5 name=CUDA0 description="NVIDIA GeForce MX550" libdirs=ollama,cuda_v12 driver=12.8 pci_id=02:00.0 type=discrete total="2.0 GiB" available="1.9 GiB"
time=2026-01-01T13:17:00.642+02:00 level=INFO source=routes.go:1605 msg="entering low vram mode" "total vram"="2.0 GiB" threshold="20.0 GiB"
[GIN] 2026/01/01 - 13:17:00 | 200 |      1.2922ms |       127.0.0.1 | HEAD     "/"
[GIN] 2026/01/01 - 13:17:00 | 200 |     67.8883ms |       127.0.0.1 | GET      "/api/tags"
time=2026-01-01T13:45:16.492+02:00 level=INFO source=runner.go:545 msg="failure during GPU discovery" OLLAMA_LIBRARY_PATH="[C:\\Users\\msherif\\OneDrive - SecurID\\Downloads\\ollama-windows-amd64\\lib\\ollama C:\\Users\\msherif\\OneDrive - SecurID\\Downloads\\ollama-windows-amd64\\lib\\ollama\\cuda_v12]" extra_envs=[] error="failed to finish discovery before timeout"
time=2026-01-01T13:45:16.493+02:00 level=WARN source=runner.go:347 msg="unable to refresh free memory, using old values"
llama_model_loader: loaded meta data with 30 key-value pairs and 255 tensors from C:\Users\msherif\.ollama\models\blobs\sha256-dde5aa3fc5ffc17176b5e8bdc82f587b24b2678c6c66101bf7da77af9f7ccdff (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Llama 3.2 3B Instruct
llama_model_loader: - kv   3:                           general.finetune str              = Instruct
llama_model_loader: - kv   4:                           general.basename str              = Llama-3.2
llama_model_loader: - kv   5:                         general.size_label str              = 3B
llama_model_loader: - kv   6:                               general.tags arr[str,6]       = ["facebook", "meta", "pytorch", "llam...
llama_model_loader: - kv   7:                          general.languages arr[str,8]       = ["en", "de", "fr", "it", "pt", "hi", ...
llama_model_loader: - kv   8:                          llama.block_count u32              = 28
llama_model_loader: - kv   9:                       llama.context_length u32              = 131072
llama_model_loader: - kv  10:                     llama.embedding_length u32              = 3072
llama_model_loader: - kv  11:                  llama.feed_forward_length u32              = 8192
llama_model_loader: - kv  12:                 llama.attention.head_count u32              = 24
llama_model_loader: - kv  13:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  14:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  15:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  16:                 llama.attention.key_length u32              = 128
llama_model_loader: - kv  17:               llama.attention.value_length u32              = 128
llama_model_loader: - kv  18:                          general.file_type u32              = 15
llama_model_loader: - kv  19:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  20:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  21:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  22:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  23:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  24:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  25:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  26:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  27:                tokenizer.ggml.eos_token_id u32              = 128009
llama_model_loader: - kv  28:                    tokenizer.chat_template str              = {{- bos_token }}\n{%- if custom_tools ...
llama_model_loader: - kv  29:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   58 tensors
llama_model_loader: - type q4_K:  168 tensors
llama_model_loader: - type q6_K:   29 tensors
```

Checked what models I've got for this using: ollama list

As I tested, observed the logging and api calls made:
<img width="542" height="70" alt="image" src="https://github.com/user-attachments/assets/ae345eae-4486-4868-900f-babff45e46eb" />

## Next Steps

* **System Prompts:** Add a field to modify the "System Role" (e.g., "You are a legal expert") to see how persona impacts quality.
* **Temperature Slider:** Add a Gradio slider to test how randomness (Temperature) affects the consistency of the three prompts.
* **Batch Export:** Add an "Export to CSV" feature to save your favorite prompt/result pairs for future fine-tuning.
