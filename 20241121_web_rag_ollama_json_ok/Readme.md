# Web RAG (Retrieval-Augmented Generation) Chatbot

An advanced chatbot system that leverages multiple data sources combined with a local Large Language Model (LLM) to provide accurate, up-to-date responses with comprehensive source citations.

## 🌟 Key Features

- 🔍 **Multi-source Information Retrieval**
  - Real-time DuckDuckGo web search results
  - Latest Google News articles
  - Comprehensive Wikipedia knowledge
- 🤖 **Local LLM Integration**
  - Powered by Ollama
  - Uses llama3.2:1b model
  - Efficient local processing
- 📝 **Advanced Response System**
  - Real-time citation system with source tracking
  - Streaming responses for immediate feedback
  - Current date/time awareness for temporal context
  - Precise source attribution with unique identifiers
- 💻 **User Interface**
  - Modern Gradio-based web interface
  - Interactive chat experience
  - Real-time response streaming
  - Mobile-responsive design

## 🛠️ Technical Requirements

- Python 3.8+
- Ollama server with llama3.2:1b model
- Internet connection for real-time data fetching
- Required Python packages (add to requirements.txt):
  - gradio
  - requests
  - duckduckgo_search
  - gnews
  - wikipediaapi
  - datetime

## 📦 Project Structure

```
project/
├── gradio_app.py      # Main application and UI
├── ddg.py            # DuckDuckGo search module
├── gn.py             # Google News fetcher
├── wiki.py           # Wikipedia content retriever
├── requirements.txt  # Project dependencies
├── test/            # Test data directory
│   ├── ddg.json
│   ├── gnews.json
│   ├── wikipedia_raw.json
│   └── wikipedia_organized.json
└── data/            # Runtime data storage
    ├── ddg.json
    ├── gnews.json
    └── wikipedia.json
```

## 🔄 Data Flow Architecture

### 1. Data Source Modules

#### DuckDuckGo Module (`ddg.py`)
- **Purpose**: Real-time web search results
- **Implementation**:
  - Uses `duckduckgo_search` for web queries
  - Filters and processes search results
  - Stores structured data in `ddg.json`
- **Output Format**:
  ```json
  {
    "title": "Result title",
    "href": "URL",
    "body": "Content snippet"
  }
  ```

#### Google News Module (`gn.py`)
- **Purpose**: Current events and news coverage
- **Implementation**:
  - Utilizes `gnews` for article retrieval
  - Processes and validates news data
  - Maintains temporal relevance
- **Output Format**:
  ```json
  {
    "title": "Article title",
    "url": "Article URL",
    "description": "Content summary",
    "publisher": {"title": "Source name"},
    "published date": "ISO timestamp"
  }
  ```

#### Wikipedia Module (`wiki.py`)
- **Purpose**: In-depth knowledge base
- **Implementation**:
  - Uses `wikipedia-api` for content retrieval
  - Intelligent search with fallback terms
  - Content extraction and summarization
- **Output Format**:
  ```json
  {
    "title": "Article title",
    "url": "Article URL",
    "summary": "Article summary",
    "content": "Full article content"
  }
  ```

### 2. Core Application (`gradio_app.py`)

#### Processing Pipeline
1. **Query Reception**
   ```
   User Input → Timestamp → Query Processing
   ```

2. **Multi-source Retrieval**
   ```
   Query → Parallel Data Fetching → Source Aggregation
   ```

3. **Context Assembly**
   ```
   Raw Data → Processing → Structured Context
   ```

4. **LLM Inferencing**
   - **Model**: llama3.2:1b via Ollama
   - **Endpoint**: http://localhost:11434/api/generate
   - **Input Processing**:
     ```
     System Prompt + Context + User Query → Formatted Prompt
     ```
   - **Streaming Response**:
     - Real-time token generation
     - Progressive UI updates
   - **Citation System**:
     - [DDG1], [DDG2]: DuckDuckGo results
     - [NEWS1], [NEWS2]: Google News articles
     - [WIKI-P1], [WIKI-P2]: Wikipedia paragraphs
   - **Response Structure**:
     1. Direct answer to the question
     2. Supporting evidence with citations
     3. Relevant dates from sources

5. **Response Generation**
   ```
   Context + LLM Output → Formatted Response with Citations
   ```

## 🚀 Setup and Execution

### 1. Installation
```bash
# Clone repository
git clone [repository-url]

# Install dependencies
pip install -r requirements.txt

# Start Ollama server with the required model
ollama pull llama3.2:1b
ollama run llama3.2:1b
```

### 2. Configuration
- Ensure Ollama is running and accessible at port 11434
- Check network connectivity for data sources
- Verify file permissions for data directory
- Configure model parameters if needed

### 3. Running the Application
```bash
python gradio_app.py
```
- Access the interface at: `http://localhost:7860`

### 4. Running Tests
```bash
# Run all tests
python -m unittest test_app.py -v

# Test individual modules
python wiki.py  # Tests Wikipedia module
python ddg.py   # Tests DuckDuckGo module
python gn.py    # Tests Google News module
```

## 🔍 Response Format

### Citation System
- **Web Sources**: [DDG1], [DDG2], etc.
  - Format: Title and URL from DuckDuckGo search
- **News Articles**: [NEWS1], [NEWS2], etc.
  - Format: Title, Publisher, and Publication Date
- **Wikipedia**: [WIKI-SUMMARY], [WIKI-P1], etc.
  - Format: Article Title, Section, and URL

### Response Structure
```
1. Clear answer with citations for each fact
2. Relevant dates from the sources
3. Limitations or gaps in the provided information
4. Citation Details:
   [DDG1] Title: Example Title - URL
   [NEWS1] Title: News Title - Publisher (Date)
   [WIKI-P1] Content excerpt from Wikipedia Article
```

## 🔧 Troubleshooting

### Common Issues
1. **Ollama Connection**
   - Verify server status
   - Check port availability
   - Confirm model installation

2. **Data Source Access**
   - Check internet connectivity
   - Verify API rate limits
   - Monitor response timeouts

3. **File Operations**
   - Ensure write permissions
   - Check JSON file integrity
   - Monitor disk space

## 📈 Performance Considerations

- **Response Time**: Typically 2-5 seconds
- **Memory Usage**: ~500MB-1GB
- **Concurrent Users**: Up to 10 recommended
- **Data Freshness**: Real-time to 24h depending on source

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed changes
4. Ensure all tests pass

## 📄 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details. The Apache 2.0 license is a permissive license that allows you to freely use, modify, distribute, and sell your software, provided you include the required notices. This license also provides an express grant of patent rights from contributors to users.