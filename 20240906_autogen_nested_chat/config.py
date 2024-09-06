import autogen

# Set up Groq API key (in real-world usage, consider using environment variables)
api_key = ""

# Available models with their corresponding Model IDs
available_models = {
    "Llama 3.1 70B (Preview)": "llama-3.1-70b-versatile",
    "Llama 3.1 8B (Preview)": "llama-3.1-8b-instant",
    "Llama 3 Groq 70B Tool Use (Preview)": "llama3-groq-70b-8192-tool-use-preview",
    "Llama 3 Groq 8B Tool Use (Preview)": "llama3-groq-8b-8192-tool-use-preview",
    "Llama Guard 3 8B": "llama-guard-3-8b",
    "Meta Llama 3 70B": "llama3-70b-8192",
    "Meta Llama 3 8B": "llama3-8b-8192",
    "Mixtral 8x7B": "mixtral-8x7b-32768",
    "Gemma 7B": "gemma-7b-it",
    "Gemma 2 9B": "gemma2-9b-it",
    "Whisper": "whisper-large-v3"
}

def get_llm_config(selected_model_name):
    try:
        selected_model_id = available_models[selected_model_name]
    except KeyError:
        # Fallback to a default model if the specified config is not found
        selected_model_id = available_models["Llama 3.1 8B (Preview)"]

    config_list = [
        {
            "model": selected_model_id,
            "api_key": api_key,
            "api_type": "groq",
        }
    ]

    llm_config = {"config_list": config_list}
    return llm_config
