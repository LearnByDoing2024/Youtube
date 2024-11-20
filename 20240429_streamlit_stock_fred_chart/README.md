# Streamlit Stock & FRED Data Visualization App

An interactive web application built with Streamlit for visualizing stock market data and Federal Reserve Economic Data (FRED) indicators, providing comprehensive financial market analysis tools.

## 📁 Project Structure
```
├── README.md     # Project documentation
├── main.py       # Main Streamlit application
├── stock.py      # Stock data handling
├── fred.py       # FRED data integration
└── plotting.py   # Data visualization
```

## 🌟 Overview
This project provides:
- 📊 Real-time stock data visualization
- 📈 FRED economic indicators
- 🔄 Interactive data updates
- 📉 Technical analysis tools
- 📋 Data export capabilities
- 🎨 Customizable charts

## ✨ Features
- 🔢 Stock Market Data:
  - Real-time price tracking
  - Historical data analysis
  - Volume visualization
  - Technical indicators
  - Price statistics
- 📊 FRED Integration:
  - Economic indicators
  - Monetary policy data
  - Interest rates
  - Employment statistics
  - GDP metrics
- 🎨 Visualization Options:
  - Candlestick charts
  - Line plots
  - Area charts
  - Bar graphs
  - Correlation plots
- 🔄 Interactive Features:
  - Date range selection
  - Indicator overlay
  - Data filtering
  - Custom comparisons
  - Export options

## 🛠️ Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install streamlit pandas numpy
  pip install yfinance fredapi
  pip install plotly matplotlib
  pip install requests python-dotenv
  ```
- FRED API Key (obtain from https://fred.stlouisfed.org/docs/api/api_key.html)
- Basic understanding of:
  - Financial markets
  - Economic indicators
  - Python programming
  - Data visualization
  - Web applications

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/learnbydoingwithsteven/Youtube.git
cd "20240429_streamlit_stock_fred_chart"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Add your FRED API key to .env:
# FRED_API_KEY=your_api_key_here
```

## 💻 Usage
1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Access the application:
- Open your browser
- Navigate to http://localhost:8501
- Start exploring data!

## 🔍 Technical Details
The project implements:

1. Data Integration:
   - Stock market API connection
   - FRED API integration
   - Real-time data fetching
   - Historical data caching
   - Error handling

2. Data Processing:
   - Time series analysis
   - Statistical calculations
   - Technical indicators
   - Data normalization
   - Missing data handling

3. Visualization:
   - Interactive charts
   - Multiple chart types
   - Custom color schemes
   - Responsive design
   - Export capabilities

4. User Interface:
   - Intuitive controls
   - Responsive layout
   - Data filters
   - Download options
   - Help documentation

## ⚠️ Best Practices
- Cache API responses
- Handle rate limits
- Validate user input
- Implement error handling
- Document assumptions
- Monitor performance
- Regular updates
- Security considerations

## 🔧 Troubleshooting
Common solutions:
- Check API keys
- Verify internet connection
- Update dependencies
- Clear cache
- Check data availability
- Review error logs
- Validate inputs
- Browser compatibility

## 🤝 Contributing
We welcome contributions in:
- New features
- Data sources
- Visualization types
- Documentation
- Bug fixes
- Performance improvements
- UI enhancements
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
- Federal Reserve Economic Data (FRED)
- Streamlit development team
- Financial data providers
- Open-source community
- Learn By Doing With Steven community

## 📌 Important Notes
- API rate limits
- Data accuracy
- Market hours
- Update frequency
- Browser support
- Mobile compatibility
- Educational purpose
- Not financial advice

https://youtu.be/dXTNqabJ26Y
