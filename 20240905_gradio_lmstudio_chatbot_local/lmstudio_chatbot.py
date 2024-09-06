import gradio as gr
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1002/v1", api_key="lm-studio")

# Initial system message
system_message = {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."}

def chat_with_lmstudio(message, history):
    # Convert the Gradio history into the format expected by LM Studio
    lmstudio_history = [system_message] + [
        {"role": "user", "content": user_message} if i % 2 == 0 else {"role": "assistant", "content": assistant_message}
        for i, (user_message, assistant_message) in enumerate(history)
    ]
    
    # Append the user's latest message
    lmstudio_history.append({"role": "user", "content": message})
    
    # Call the LM Studio API
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
        messages=lmstudio_history,
        temperature=0.7,
        stream=True,
    )
    
    # Collect the response from the assistant
    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            new_message["content"] += chunk.choices[0].delta.content
    
    # Update the history with the new message
    history.append((message, new_message["content"]))
    
    return new_message["content"]

# Create the Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_with_lmstudio,
    title="LM Studio Chatbot",
    description="Chatbot powered by a locally running LM Studio instance.",
)

# Launch the Gradio interface locally
demo.launch()
