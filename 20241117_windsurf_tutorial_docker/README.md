# Windsurf Tutorial: 30-Minute App with Docker

A sleek and modern chat interface for Ollama models built with Streamlit, as demonstrated in [this tutorial video](https://youtu.be/AvNzJryIPcI).

## 📁 Project Structure
```
├── README.md           # Project documentation
├── app.py             # Main Streamlit application
├── Dockerfile         # Docker container configuration
├── docker-compose.yml # Docker Compose configuration
└── requirements.txt   # Python dependencies
```

## ✨ Features

- 🤖 Connect to local Ollama instance
- 📋 Dynamic model selection from available Ollama models
- 💬 Clean chat interface with message history
- 🎨 Modern UI design with custom styling
- ⚡ Real-time responses from AI models
- 🔄 Pull new models directly from the UI
- 🐳 Docker support for easy deployment

## 🛠️ Prerequisites

Choose one of the following setup options:

### 💻 Local Setup
1. Python 3.7+
2. Ollama installed and running locally
3. pip (Python package manager)

### 🐳 Docker Setup
1. Docker and Docker Compose installed
2. Internet connection for pulling Docker images

## 📦 Installation

### Local Installation
1. Clone this repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20241117_windsurf_tutorial_30min_app_and_docker"
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Docker Installation
1. Clone this repository
2. No additional installation needed - Docker will handle dependencies

## 🚀 Running the Application

### Local Run
1. Make sure Ollama is running on your system
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your browser and navigate to http://localhost:8501

### Docker Run
1. Start the application using Docker Compose:
```bash
docker-compose up -d
```
2. Open your browser and navigate to http://localhost:8502
3. To stop the application:
```bash
docker-compose down
```

## 🐳 Docker Configuration

The application runs in two containers:
- 🖥️ Streamlit UI container (exposed on port 8502)
- 🤖 Ollama service container (internal port 11434)

Environment variables:
- `OLLAMA_HOST`: Set to 'http://ollama:11434' in Docker environment
- `PORT`: Streamlit port (default: 8502)

Volume mounts:
- Ollama data is persisted in a named volume

## 💡 Usage

1. If using a new model:
   - Enter the model name in the "Pull New Model" field in the sidebar
   - Click "Pull Model" and wait for the download to complete
2. Select an available model from the dropdown in the sidebar
3. Type your message in the text area
4. Click "Send" or press Enter to send your message
5. Wait for the AI to respond
6. Your chat history will be maintained during the session

## ⚠️ Important Notes

- When running locally, ensure Ollama is running on port 11434 (default port)
- The application will automatically detect available models
- Chat history is maintained only during the current session
- Docker deployment handles all networking automatically
- Large models may take several minutes to pull

## 📜 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

Copyright 2024 Learn By Doing With Steven (YouTube Channel)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Ollama team for the local LLM solution
- All contributors and users
- Learn By Doing With Steven YouTube community
