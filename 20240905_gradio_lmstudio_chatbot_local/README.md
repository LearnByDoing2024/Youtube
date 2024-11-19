# Local Chatbot with Gradio and LM Studio

This project demonstrates how to create a local chatbot using Gradio and LM Studio, as shown in [this tutorial video](https://youtu.be/haRuvdnSDPg).

## Overview
This project implements a local chatbot that:
- Runs completely on your local machine for privacy and control
- Uses LM Studio for the language model backend
- Implements a user-friendly interface with Gradio
- Supports real-time chat interactions

## Features
- 🚀 Local model inference using LM Studio
- 🎨 Clean and intuitive chat interface with Gradio
- 🔒 Privacy-focused: all processing happens locally
- ⚡ Fast response times with optimized settings
- 🔧 Customizable chat parameters

## Prerequisites
- Python 3.8+
- LM Studio installed locally
- Required Python packages:
  ```bash
  pip install gradio
  pip install requests
  ```
- A compatible language model downloaded in LM Studio

## Setup Instructions
1. Install LM Studio and download your preferred language model
2. Start LM Studio and run the local server
3. Install the required Python dependencies
4. Run the Gradio interface:
   ```bash
   python app.py
   ```

## Usage
1. Launch LM Studio and start the local server
2. Run the Gradio application
3. Access the chat interface through your web browser
4. Start chatting with your local AI!

## Configuration
You can customize various parameters:
- Model settings in LM Studio
- Chat interface appearance
- Response generation parameters
- API endpoint configuration

## Troubleshooting
Common issues and solutions:
- Ensure LM Studio server is running before starting the chat interface
- Check port configurations if connection issues occur
- Verify model compatibility and system requirements

## Contributing
Feel free to contribute by:
- Reporting issues
- Suggesting improvements
- Submitting pull requests
- Sharing your experiences

## License
This project is open-source and available under the MIT License.
