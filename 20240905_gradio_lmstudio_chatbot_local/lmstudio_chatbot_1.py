import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv
import sys
import io
import traceback

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1002/v1")
API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")
MODEL = os.getenv("LM_STUDIO_MODEL", "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF")

# Initialize OpenAI client
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Initial system message
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are an intelligent assistant capable of generating and executing Python code. Always provide well-reasoned answers and executable code when appropriate."
}

def format_chat_history(history):
    """Convert Gradio history to LM Studio format."""
    return [SYSTEM_MESSAGE] + [
        {"role": "user" if i % 2 == 0 else "assistant", "content": msg}
        for i, (user_msg, assistant_msg) in enumerate(history)
        for msg in (user_msg, assistant_msg)
    ]

def execute_code(code):
    """Execute Python code and return the output."""
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    
    try:
        exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    except Exception as e:
        sys.stdout = old_stdout
        return f"Error: {str(e)}\n\n{traceback.format_exc()}"

def chat_with_lmstudio(message, history):
    """Chat with LM Studio and return the full response."""
    try:
        lmstudio_history = format_chat_history(history)
        lmstudio_history.append({"role": "user", "content": message})

        completion = client.chat.completions.create(
            model=MODEL,
            messages=lmstudio_history,
            temperature=0.7,
            stream=False,
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {str(e)}\n\n{traceback.format_exc()}"

def process_message(message, history, code_output):
    """Process user message, generate response, and execute code if present."""
    try:
        assistant_response = chat_with_lmstudio(message, history)
        
        # Check if the response contains a code block
        if "```python" in assistant_response:
            code_start = assistant_response.index("```python") + 10
            code_end = assistant_response.index("```", code_start)
            code = assistant_response[code_start:code_end].strip()
            
            # Execute the code
            output = execute_code(code)
            code_output = code_output + f"\nCode Output:\n{output}"
        
        new_history = history + [(message, assistant_response)]
        return new_history, code_output
    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n\n{traceback.format_exc()}"
        return history + [(message, error_message)], code_output + f"\nError:\n{error_message}"

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# LM Studio Chatbot with Code Execution")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Type your message here", placeholder="Ask me anything or request code...")
            clear = gr.Button("Clear")
        
        with gr.Column(scale=2):
            code_output = gr.TextArea(label="Code Output", interactive=False)
    
    msg.submit(process_message, [msg, chatbot, code_output], [chatbot, code_output])
    clear.click(lambda: ([], ""), outputs=[chatbot, code_output])

if __name__ == "__main__":
    demo.launch()