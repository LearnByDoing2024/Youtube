import json
import requests
import gradio as gr
import os
from datetime import datetime
from gn import search_google_news, save_results_to_json as save_gnews_json
from wiki import search_wikipedia, save_results_to_json as save_wiki_json
from ddg import search_duckduckgo, save_results_to_json as save_ddg_json

# Create data directory if it doesn't exist
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def get_data_file_path(filename):
    """Get the full path for a data file."""
    return os.path.join(DATA_DIR, filename)

def get_current_date():
    """Get current date in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def verify_json_data(memory_data, filename):
    """Verify that saved JSON data matches memory data."""
    try:
        filepath = get_data_file_path(filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
            return file_data == memory_data
        return False
    except Exception as e:
        print(f"[{get_current_date()}] Error verifying JSON data: {str(e)}")
        return False

# --- Generate all source data ---
def generate_source_data(query):
    try:
        current_date = get_current_date()
        print(f"[{current_date}] Generating source data for query: {query}")
        
        # 1. DuckDuckGo Search
        print(f"[{current_date}] Searching DuckDuckGo...")
        ddg_data = search_duckduckgo(query, max_results=3)
        ddg_file = get_data_file_path("ddg.json")
        save_ddg_json(ddg_data, ddg_file)
        if not verify_json_data(ddg_data, "ddg.json"):
            print(f"[{current_date}] Warning: DuckDuckGo data verification failed")
        
        # 2. Google News Search
        print(f"[{current_date}] Searching Google News...")
        gnews_data = search_google_news(query, max_results=3)
        gnews_file = get_data_file_path("gnews.json")
        save_gnews_json(gnews_data, gnews_file)
        if not verify_json_data(gnews_data, "gnews.json"):
            print(f"[{current_date}] Warning: Google News data verification failed")
        
        # 3. Wikipedia Search
        print(f"[{current_date}] Searching Wikipedia...")
        wiki_data = search_wikipedia(query)
        wiki_file = get_data_file_path("wikipedia.json")
        save_wiki_json(wiki_data, wiki_file)
        if not verify_json_data(wiki_data, "wikipedia.json"):
            print(f"[{current_date}] Warning: Wikipedia data verification failed")
        
        return ddg_data, gnews_data, wiki_data
    except Exception as e:
        print(f"[{get_current_date()}] Error in generate_source_data: {str(e)}")
        return [], [], {"error": str(e)}

# --- Build context for LLM ---
def build_context(query):
    try:
        current_date = get_current_date()
        context = f"### Current Date and Time: {current_date}\n\n"
        context += f"### User Query: {query}\n\n"
        
        # Generate and load all source data
        ddg_data, gnews_data, wiki_data = generate_source_data(query)
        
        # Track citations for debugging
        citations_used = []
        
        # Add DuckDuckGo data
        context += "### DuckDuckGo Search Results:\n"
        if ddg_data:
            for i, result in enumerate(ddg_data, 1):
                title = result.get('title', 'No Title')
                url = result.get('href', 'No URL')
                content = result.get('body', 'No content available')
                citation = f"[DDG{i}]"
                citations_used.append(citation)
                context += f"{citation} Title: {title}\nURL: {url}\nContent: {content}\n\n"
        else:
            context += "No DuckDuckGo results available.\n\n"
        
        # Add Google News data
        context += "### Recent News:\n"
        if gnews_data:
            for i, news in enumerate(gnews_data, 1):
                title = news.get('title', 'No Title')
                url = news.get('url', 'No URL')
                description = news.get('description', 'No description available')
                publisher = news.get('publisher', {}).get('title', 'Unknown Source')
                published_date = news.get('published date', 'Unknown Date')
                citation = f"[NEWS{i}]"
                citations_used.append(citation)
                context += f"{citation} Title: {title}\nSource: {publisher}\nDate: {published_date}\nURL: {url}\nSummary: {description}\n\n"
        else:
            context += "No news results available.\n\n"
        
        # Add Wikipedia data
        if "error" not in wiki_data and wiki_data:
            title = wiki_data.get('title', 'No Title')
            url = wiki_data.get('url', 'No URL')
            context += f"### Wikipedia Article: {title}\nURL: {url}\n\n"
            
            # Add summary
            summary = wiki_data.get('summary', '')
            if summary:
                citation = "[WIKI-SUMMARY]"
                citations_used.append(citation)
                context += f"{citation} {summary}\n\n"
            
            # Add content paragraphs
            content = wiki_data.get('content', '')
            if content:
                context += "### Wikipedia Content Excerpts:\n"
                # Split content into paragraphs and add first few meaningful ones
                paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 100]
                for i, para in enumerate(paragraphs[:3], 1):
                    citation = f"[WIKI-P{i}]"
                    citations_used.append(citation)
                    context += f"{citation} {para}\n\n"
        else:
            context += "### Wikipedia:\nNo Wikipedia data available.\n\n"
        
        print(f"[{current_date}] Context built with {len(citations_used)} citations: {', '.join(citations_used)}")
        
        # Add citation details at the end
        context += "\n### Citation Details:\n"
        for citation in citations_used:
            if citation.startswith("[DDG"):
                idx = int(citation[4:-1]) - 1
                if idx < len(ddg_data):
                    result = ddg_data[idx]
                    context += f"{citation}: {result.get('title', 'No Title')} - {result.get('href', 'No URL')}\n"
            elif citation.startswith("[NEWS"):
                idx = int(citation[5:-1]) - 1
                if idx < len(gnews_data):
                    news = gnews_data[idx]
                    context += f"{citation}: {news.get('title', 'No Title')} - {news.get('publisher', {}).get('title', 'Unknown Source')} ({news.get('published date', 'Unknown Date')})\n"
            elif citation.startswith("[WIKI"):
                if citation == "[WIKI-SUMMARY]":
                    context += f"{citation}: Summary of {wiki_data.get('title', 'No Title')} - {wiki_data.get('url', 'No URL')}\n"
                else:
                    context += f"{citation}: Content excerpt from {wiki_data.get('title', 'No Title')}\n"
        
        return context
    except Exception as e:
        print(f"[{get_current_date()}] Error in build_context: {str(e)}")
        return f"Error building context: {str(e)}"

# --- Query Ollama (LLM) model ---
def query_ollama_stream(prompt, context):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    
    current_date = get_current_date()
    # Define the system prompt that guides the LLM's response structure and factual accuracy
    system_prompt = f"""You are a helpful AI assistant. Today's date and time is: {current_date}

    # Core instructions for response structure and factual accuracy
    Using ONLY the provided context, answer the user's question accurately and concisely.
    IMPORTANT RULES:
    1. ALWAYS cite your sources using the reference codes in square brackets (e.g., [DDG1], [NEWS2], [WIKI-P1])
    2. Add citations IMMEDIATELY after each fact or statement you mention
    3. If information is not in the context, explicitly say "I don't have current information about X"
    4. Pay attention to dates in the sources and mention them when relevant
    5. Do not mix historical information with current information
    # Core instruction to avoid making up information
    6. Do not make up or infer information not present in the sources

    # Define the required structure for the LLM's response
    Structure your response with:
    # Main components of the response structure
    1. A clear answer with citations for each fact
    # Temporal context requirement
    2. Relevant dates from the sources
    # Transparency about information completeness
    3. Any limitations or gaps in the provided information 
    # Citation details section for source tracking
    4. Citations:
    # Example citation format for DuckDuckGo results
    [DDG1] Title: ...
    # Example citation format for News results
    [NEWS2] Title: ...
    # Example citation format for Wikipedia paragraphs
    [WIKI-P1] Title: ...

    """
    # Combine system prompt, context, and user query into final prompt
    full_prompt = f"{system_prompt}\n\nContext:\n{context}\n\nUser Question: {prompt}\n\nAnswer:"
    
    # Prepare the API request payload for Ollama
    payload = {
        # Specify the language model to use
        "model": "llama3.2:1b",
        # Include the complete formatted prompt
        "prompt": full_prompt,
        # Enable streaming for the response
        "stream": True
    }
    
    try:
        # Send the request to Ollama and stream the response
        with requests.post(url, json=payload, headers=headers, stream=True) as response:
            response.raise_for_status()
            response_text = ""
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    data = json.loads(decoded_line)
                    token = data.get("response", "")
                    response_text += token
                    yield response_text
    except requests.exceptions.RequestException as e:
        error_msg = f"Error connecting to Ollama: {str(e)}"
        print(f"[{get_current_date()}] {error_msg}")
        yield error_msg

# --- Gradio chatbot interface ---
def chatbot_interface(message, history):
    history = history or []
    current_date = get_current_date()
    
    try:
        print(f"[{current_date}] Processing new message: {message}")
        
        # Build context from multiple sources
        context = build_context(message)
        
        # Get response from LLM
        response_generator = query_ollama_stream(message, context)
        
        # Initialize the response
        current_response = ""
        
        # Stream the response
        for response_chunk in response_generator:
            current_response = response_chunk
            history = history + [[message, current_response]]
            yield history
            # Remove the last message since we'll add an updated version
            history = history[:-1]
        
        # Add the final response
        history = history + [[message, current_response]]
        print(f"[{current_date}] Completed response generation")
        yield history
            
    except Exception as e:
        error_msg = f"Error in chatbot interface: {str(e)}"
        print(f"[{current_date}] {error_msg}")
        history = history + [[message, error_msg]]
        yield history

# --- Clear chat history ---
def clear_history():
    return []

# --- Gradio interface ---
with gr.Blocks() as demo:
    gr.Markdown("# RAG-Enhanced LLM Chatbot")
    gr.Markdown(f"""This chatbot uses Retrieval-Augmented Generation (RAG) with data from:
    - DuckDuckGo Search
    - Google News
    - Wikipedia
    
    Responses include citations to sources using codes like [DDG1], [NEWS1], [WIKI-P1].
    Current date and time: {get_current_date()}""")
    
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message here...", placeholder="Ask me anything...")
    clear = gr.Button("Clear")
    
    msg.submit(chatbot_interface, [msg, chatbot], [chatbot])
    clear.click(clear_history, outputs=[chatbot])

if __name__ == "__main__":
    current_date = get_current_date()
    print(f"[{current_date}] Starting the RAG-Enhanced LLM Chatbot...")
    print(f"[{current_date}] Make sure Ollama is running with the llama3.2:1b model loaded.")
    demo.queue().launch(share=False)
