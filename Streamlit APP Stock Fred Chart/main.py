# main.py
import streamlit as st
from stock import load_data, add_moving_averages, predict_future_prices
from plotting import plot_economic_data, plot_candlestick_with_moving_averages
from fred import get_economic_data  
import pandas as pd

@st.cache_data
def load_sp500_symbols():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    return table[0]['Symbol'].tolist()

# Load S&P 500 symbols
symbols = load_sp500_symbols()

# Sidebar for stock selection
selected_symbol = st.sidebar.selectbox("Select a stock symbol", symbols, key="stock_selectbox")

# Load stock data
stock_data = load_data(selected_symbol)

# Add moving averages to stock data
stock_data = add_moving_averages(stock_data)

# Predict future stock prices
future_stock_prices = predict_future_prices(stock_data)

# Load S&P 500 data
sp500_data = load_data("^GSPC")
sp500_data = add_moving_averages(sp500_data)


# Display candlestick chart with moving averages for selected stock
# Display the first graph in the first column
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_candlestick_with_moving_averages(stock_data, f"{selected_symbol} Stock Chart", ma_30=stock_data['30D MA'], ma_60=stock_data['60D MA'], ma_90=stock_data['90D MA'], selected_symbol=selected_symbol))

# Display S&P 500 candlestick chart with moving averages in the second column
with col2:
    st.plotly_chart(plot_candlestick_with_moving_averages(sp500_data, "S&P 500 Index Candlestick Chart", ma_30=sp500_data['30D MA'], ma_60=sp500_data['60D MA'], ma_90=sp500_data['90D MA']))

# Display economic data
gdp, interest_rate, inflation, unemployment = get_economic_data()

# Display the first economic data chart in the first column
with col1:
    st.plotly_chart(plot_economic_data({'GDP': gdp, 'Federal Funds Rate': interest_rate}, "US GDP and Interest Rate Line Chart"))

# Display the second economic data chart in the second column
with col2:
    st.plotly_chart(plot_economic_data({'Inflation Rate': inflation, 'Unemployment Rate': unemployment}, "US Inflation and Unemployment Rate Chart"))

# streamlit run main.py



