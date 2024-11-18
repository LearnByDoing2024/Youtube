# Enhanced LangChain with LM Studio: GDPR Fine Analysis

A sophisticated implementation combining LangChain and LM Studio for analyzing GDPR fines and regulations. This project demonstrates advanced RAG (Retrieval-Augmented Generation) techniques using local LLMs for processing and analyzing GDPR-related data.

## 📺 Video Tutorial
Watch the step-by-step implementation on YouTube:
[Enhanced LangChain Implementation Tutorial](https://youtu.be/Rv3WNMkvWWY)

## 🌟 Key Features
- Custom vector store implementation for efficient document retrieval
- Integration with local LLMs through LM Studio
- GDPR fine analysis from multiple data sources
- Advanced text processing and embedding using Universal Sentence Encoder
- Debug information generation for transparency
- Interactive HTML report generation

## 🔧 Components

### Data Sources
- GDPR fines dataset (`gdpr_fines_0_s.csv`)
- Wikipedia GDPR information (`gdpr_fines_wiki_0_0_s.csv`)
- GDPR law reference documents
- News articles related to GDPR violations

### Technical Implementation
- Custom `SimpleVectorStore` class for document storage and retrieval
- NLTK-based text processing
- TensorFlow Hub's Universal Sentence Encoder for embeddings
- Local LLM integration via LM Studio
- Comprehensive debugging and reporting system

## 🚀 Installation

1. Install required packages:
```bash
pip install pandas pdfplumber nltk tensorflow-hub numpy openai tensorflow
```

2. Download required NLTK data:
```python
import nltk
nltk.download('punkt')
```

3. Set up LM Studio:
- Install LM Studio
- Configure local API endpoint
- Set up API key in the code

## 📊 Usage

1. Prepare your data files:
- Ensure CSV files are in the correct format
- Place GDPR reference documents in the project directory

2. Run the main script:
```bash
python langchain_lmstudio_4.py
```

3. View generated reports:
- Check `gdpr_compliance_report.html` for analysis results
- Review `debug_report.html` for detailed processing information

## 📝 File Structure
- `langchain_lmstudio_4.py`: Main implementation
- `fine_history_0_s.py`: Historical fine data processing
- `lmstudio_only.py`: Standalone LM Studio implementation
- `key_points.txt`: Development notes and key features
- `step.txt`: Step-by-step implementation guide
- CSV files: GDPR fine and Wikipedia data
- Test versions: Various implementation iterations

## ⚙️ Configuration
- Adjust token limits in the code for different performance requirements
- Modify vector store parameters for different retrieval characteristics
- Customize HTML templates for different reporting needs

## 🔍 Debug Features
- Detailed processing logs
- Vector store state visualization
- Query-response tracking
- Embedding analysis tools

## 🤝 Contributing
Contributions are welcome! Areas for improvement:
- Enhanced data preprocessing
- Additional data sources integration
- UI/UX improvements
- Performance optimizations

## 📜 License
This project is open source and available under the MIT License.

## 📌 Note
You might need to adjust CSV file names based on your local setup and data sources.
