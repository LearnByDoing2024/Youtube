import pandas as pd
import plotly.graph_objects as go

# Read the data
data = pd.read_csv('news_articles.csv')

# Convert 'Date' from string to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%a, %d %b %Y %H:%M:%S GMT')

# Set Date as the index
data.set_index('Date', inplace=True)

# Resample the data daily and count sentiments
daily_sentiment = data.groupby('Sentiment').resample('D').size().unstack(0, fill_value=0)

# Create a stacked area plot
fig = go.Figure()
for sentiment in daily_sentiment.columns:
    fig.add_trace(go.Scatter(
        x=daily_sentiment.index, 
        y=daily_sentiment[sentiment], 
        mode='lines', 
        stackgroup='one', 
        name=sentiment
    ))

# Update layout
fig.update_layout(
    title='Daily Sentiment Counts',
    xaxis_title='Date',
    yaxis_title='Count',
    hovermode='x'
)

# Save the figure to an HTML file
fig.write_html('sentiment_daily.html')

# Calculate and print statistical properties
print('Statistical Properties:')
print(daily_sentiment.describe())
