#data.py
import yfinance as yf

def fetch_data(ticker_symbol):
    # ticker_symbol should be a string like 'AAPL'
    data = yf.download(ticker_symbol, period='5y')
    company_name = yf.Ticker(ticker_symbol).info['longName']  # Fetch the company name
    return data, company_name
