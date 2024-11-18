# Stock News Sentiment Analysis

This project implements a stock news sentiment analysis tool that fetches and analyzes news articles related to specific stocks. It uses natural language processing to determine the sentiment of news articles and provides insights into market sentiment.

## 📺 Video Tutorial
Watch the step-by-step tutorial on YouTube:
[Stock News Sentiment Analysis Tutorial](https://youtu.be/Z3l0p1-2LO4)

## 🌟 Features
- Fetches real-time stock news from reliable financial news sources
- Performs sentiment analysis on news articles
- Generates sentiment scores for individual articles
- Provides aggregated sentiment metrics
- Visualizes sentiment trends over time
- Supports multiple stock symbols

## 🚀 Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd "20240505 stock news sentiment analysis"
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 📊 Usage

1. Set up your API keys in a `.env` file:
```env
ALPHA_VANTAGE_API_KEY=your_api_key_here
NEWS_API_KEY=your_api_key_here
```

2. Run the main script:
```bash
python stock_sentiment_analysis.py
```

3. Enter the stock symbol when prompted

## 🔧 Dependencies
- Python 3.8+
- pandas
- numpy
- nltk
- requests
- python-dotenv
- textblob

## 📝 Note
- Free API keys may have rate limits
- Consider using premium API services for production use
- Results are for informational purposes only

## 📈 Example Output
- Sentiment scores range from -1 (very negative) to 1 (very positive)
- Daily sentiment summaries are provided
- Trending topics in news articles are highlighted

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
