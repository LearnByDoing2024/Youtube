import yfinance as yf

def download_data(ticker_symbol):
    data = yf.download(ticker_symbol, period='5y')
    data.to_csv(f'{ticker_symbol}_data.csv')