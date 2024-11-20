# Bank of Italy AML Sanctions Analysis with LLM

An advanced data analysis project that leverages Large Language Models (LLMs) to analyze Anti-Money Laundering (AML) sanctions data from the Bank of Italy, providing insights into regulatory enforcement patterns and compliance requirements.

## 📁 Project Structure
```
├── README.md                                             # Project documentation
├── Sanction_Details_with_Date.csv                       # Processed sanctions dataset
├── bank of italy AML sanction data clean ver2 experiment.ipynb    # Enhanced analysis notebook
├── bank of italy AML sanction data clean.ipynb          # Initial analysis notebook
├── bank of italy AML sanction data version 3.html       # Analysis report v3
└── bank of italy AML sanction data version 4 mistral.html        # Mistral model analysis
```

## 🌟 Overview
This project provides:
- 📊 AML sanctions data analysis
- 🤖 LLM-powered text analysis
- 📈 Temporal trend analysis
- 🔍 Regulatory pattern detection
- 📋 Compliance insights
- 🎨 Interactive visualizations

## ✨ Features
- 🔢 Data Processing:
  - Sanction data cleaning
  - Date normalization
  - Text preprocessing
  - Entity extraction
  - Amount standardization
- 🤖 LLM Analysis:
  - Sanction reason classification
  - Pattern identification
  - Compliance requirement extraction
  - Risk assessment
  - Trend analysis
- 📊 Visualization:
  - Temporal trends
  - Sanction distributions
  - Geographic analysis
  - Violation categories
  - Amount ranges
- 🔍 Insights Generation:
  - Common violations
  - Risk patterns
  - Compliance recommendations
  - Temporal patterns
  - Regional analysis

## 🛠️ Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install pandas numpy
  pip install jupyter notebook
  pip install matplotlib seaborn plotly
  pip install transformers torch
  pip install scikit-learn
  pip install spacy
  pip install python-dotenv
  ```
- LLM Requirements:
  - Mistral model access
  - Sufficient GPU memory
  - API credentials
- Basic understanding of:
  - AML regulations
  - Banking compliance
  - Data analysis
  - Machine learning
  - Italian banking system

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20240429_boi_sanction_data_llm"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download required models:
```bash
python -m spacy download it_core_news_lg
```

4. Configure environment:
```bash
cp .env.example .env
# Add your API keys and model paths
```

## 💻 Usage
1. Data Preparation:
```bash
jupyter notebook "bank of italy AML sanction data clean.ipynb"
```

2. Advanced Analysis:
```bash
jupyter notebook "bank of italy AML sanction data clean ver2 experiment.ipynb"
```

## 🔍 Technical Details
The project implements:

1. Data Processing:
   - Text cleaning
   - Date parsing
   - Amount extraction
   - Entity recognition
   - Language detection

2. LLM Analysis:
   - Text classification
   - Pattern extraction
   - Semantic analysis
   - Topic modeling
   - Sentiment analysis

3. Statistical Analysis:
   - Temporal trends
   - Amount distributions
   - Violation frequencies
   - Geographic patterns
   - Correlation analysis

4. Visualization:
   - Time series plots
   - Distribution charts
   - Heat maps
   - Network graphs
   - Interactive dashboards

## ⚠️ Best Practices
- Validate data sources
- Handle missing values
- Document assumptions
- Version control datasets
- Monitor model performance
- Regular updates
- Data privacy
- Error handling

## 🔧 Troubleshooting
Common solutions:
- Check data integrity
- Verify model loading
- Update dependencies
- Memory management
- GPU availability
- API rate limits
- Language support
- Encoding issues

## 🤝 Contributing
We welcome contributions in:
- Data cleaning
- Model improvements
- Analysis techniques
- Documentation
- Visualization
- Error handling
- Performance optimization
- Testing

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
- Bank of Italy
- Open-source community
- LLM model providers
- Italian NLP community
- Learn By Doing With Steven community

## 📌 Important Notes
- Data sensitivity
- Model limitations
- Language considerations
- Processing time
- Resource requirements
- Regular updates
- Educational purpose
- Not legal advice
