# Stock News Sentiment Analysis

This project implements a stock news sentiment analysis tool that fetches and analyzes news articles related to specific stocks. It uses natural language processing to determine the sentiment of news articles and provides insights into market sentiment. Watch the tutorial on [Learn By Doing with Steven YouTube Channel](https://youtu.be/Z3l0p1-2LO4).

## 🌟 Features
- 📰 Fetches real-time stock news from reliable financial news sources
- 🧠 Performs sentiment analysis on news articles
- 📊 Generates sentiment scores for individual articles
- 📈 Provides aggregated sentiment metrics
- 📉 Visualizes sentiment trends over time
- 🎯 Supports multiple stock symbols

## 📁 Project Structure
```
├── complete_LMS_working.py     # Main script for sentiment analysis
├── plot_daily.py              # Daily sentiment visualization
├── plot_daily_price.py        # Daily price visualization
├── plot_weekly.py             # Weekly sentiment visualization
├── requirements.txt           # Project dependencies
└── Generated Files
    ├── news_articles.csv              # Cached news data
    ├── sentiment_daily.html           # Daily sentiment report
    ├── sentiment_weekly.html          # Weekly sentiment report
    └── stock_and_sentiment_analysis.html # Combined analysis report
```

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20240505 stock news sentiment analysis"
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🔧 Prerequisites
- Python 3.8+
- API Keys:
  - Alpha Vantage API key
  - News API key
- Required packages:
  ```
  pandas
  numpy
  nltk
  requests
  python-dotenv
  textblob
  plotly
  ```

## 📊 Usage

1. Set up your API keys in a `.env` file:
```env
ALPHA_VANTAGE_API_KEY=your_api_key_here
NEWS_API_KEY=your_api_key_here
```

2. Run the main script:
```bash
python complete_LMS_working.py
```

3. Enter the stock symbol when prompted

## 📈 Features in Detail

### Data Collection
- Real-time news fetching
- Historical price data retrieval
- Multiple news source integration
- Automatic data caching

### Sentiment Analysis
- Natural Language Processing
- Sentiment scoring (-1 to 1)
- Topic extraction
- Trend identification

### Visualization
- Interactive daily charts
- Weekly sentiment trends
- Price-sentiment correlation
- Customizable date ranges

## ⚠️ Important Notes
- Free API keys have rate limits
- Consider premium API services for production use
- Results are for informational purposes only
- Regular updates recommended for accuracy

## 🔒 Security Best Practices
- Store API keys securely
- Use environment variables
- Implement rate limiting
- Validate input data
- Handle errors gracefully

## 🤝 Contributing
We welcome contributions:
- Bug reports
- Feature requests
- Documentation improvements
- Code optimizations
- Analysis enhancements

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
- Alpha Vantage API
- News API
- NLTK library
- TextBlob
- Plotly visualization library
- All contributors and users
