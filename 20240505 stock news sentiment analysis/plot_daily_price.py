import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# Fetch stock price data
ticker = 'AAPL'  # Specify the ticker
stock_data = yf.download(ticker, period='300d')

# Read sentiment data
sentiment_data = pd.read_csv('news_articles.csv')
sentiment_data['Date'] = pd.to_datetime(sentiment_data['Date'], format='%a, %d %b %Y %H:%M:%S GMT')
sentiment_data.set_index('Date', inplace=True)
daily_sentiment = sentiment_data.groupby('Sentiment').resample('D').size().unstack(0, fill_value=0)

# Ensure indices match for plotting (align dates)
combined_data = stock_data.join(daily_sentiment, how='left').fillna(0)

# Calculate correlation coefficients between stock price and sentiment counts
correlation = combined_data.corr()

# Create a figure with secondary y-axis
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=combined_data.index, y=combined_data['Adj Close'], name='AAPL Stock Price', yaxis='y1'))
for sentiment in daily_sentiment.columns:
    fig.add_trace(go.Scatter(x=combined_data.index, y=combined_data[sentiment], name=f'{sentiment} Sentiment', yaxis='y2'))

# Create axis objects
fig.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='Stock Price', side='left', showgrid=False),
    yaxis2=dict(title='Sentiment Count', overlaying='y', side='right', showgrid=False),
    title='AAPL Stock Prices and Daily Sentiment Counts'
)

# Save the figure to an HTML file
fig.write_html('stock_and_sentiment_analysis.html')

# Print correlation coefficients
print('Correlation Coefficients:')
print(correlation)
