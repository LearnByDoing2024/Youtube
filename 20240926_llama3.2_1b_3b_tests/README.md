# Llama 3.2 Model Testing (1B and 3B)

A comprehensive testing and evaluation project for Llama 3.2 models (1B and 3B variants) using different platforms including Groq and Ollama.

## 📁 Project Structure
```
├── README.md                              # Project documentation
├── LLAMA3_2_TESTS.ipynb                  # Main testing notebook
├── groq_llama3_2_models_1B.ipynb         # Groq 1B model tests
├── groq_llama3_2_models_3B.ipynb         # Groq 3B model tests
├── ollama_1b_student_teacher.ipynb        # Ollama 1B model tests
└── ollama_3b_student_teacher*.ipynb       # Ollama 3B model variations
```

## 🌟 Overview
This project demonstrates:
- 🤖 Llama 3.2 model evaluation
- 🔄 Comparison between 1B and 3B variants
- 🚀 Performance testing on Groq and Ollama
- 📊 Model response analysis

## ✨ Features
- 🔍 Model performance comparison
- 📝 Response quality assessment
- 🎯 Latency measurements
- 📊 Platform-specific optimizations
- 📈 Inference capabilities
- 📑 Code examples

## 🛠️ Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install jupyter
  pip install transformers
  pip install torch
  pip install groq  # For Groq tests
  ```
- Ollama installation (for Ollama tests)
- Basic understanding of:
  - Large Language Models
  - Python programming
  - Jupyter notebooks
  - Model inference

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20240926_llama3.2_1b_3b_tests"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Ollama (if needed):
- Follow instructions at [Ollama's official website](https://ollama.ai/)

## 💻 Usage
1. For Groq tests:
```bash
jupyter notebook groq_llama3_2_models_1B.ipynb  # For 1B model
jupyter notebook groq_llama3_2_models_3B.ipynb  # For 3B model
```

2. For Ollama tests:
```bash
jupyter notebook ollama_1b_student_teacher.ipynb  # For 1B model
jupyter notebook ollama_3b_student_teacher.ipynb  # For 3B model
```

## 🔍 Technical Details
The project covers:
- Model architecture differences
- Inference optimization
- Response generation
- Performance metrics
- Platform comparisons

## ⚠️ Best Practices
- Monitor resource usage
- Use appropriate batch sizes
- Handle model responses properly
- Implement error handling
- Consider memory limitations
- Document test results

## 🔧 Troubleshooting
Common solutions:
- Check API keys/access
- Verify model availability
- Monitor memory usage
- Review error messages
- Check platform status

## 🤝 Contributing
We welcome contributions in:
- Model testing scenarios
- Performance optimizations
- Documentation updates
- Best practices
- Platform-specific improvements

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
- Llama model developers
- Groq platform team
- Ollama developers
- Learn By Doing With Steven community

## 📌 Important Notes
- API keys required for Groq
- Sufficient RAM needed for models
- Platform-specific limitations
- Response time variations
- Resource monitoring essential
