#stock.py
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

# Load stock data
def load_data(ticker):
    data = yf.download(ticker, start="2015-01-01")
    data.reset_index(inplace=True)
    return data

# Add moving averages to data
def add_moving_averages(data):
    data['30D MA'] = data['Close'].rolling(window=30).mean()
    data['60D MA'] = data['Close'].rolling(window=60).mean()
    data['90D MA'] = data['Close'].rolling(window=90).mean()
    return data

# Predict future stock prices
def predict_future_prices(data, num_days=30):
    X = np.array(range(len(data))).reshape(-1, 1)
    y = data['Close']
    model = LinearRegression()
    model.fit(X, y)
    future_X = np.array(range(len(data), len(data) + num_days)).reshape(-1, 1)
    future_y = model.predict(future_X)
    return future_y


"""

"""