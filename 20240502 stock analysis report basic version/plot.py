import plotly.graph_objects as go
import pandas as pd

def plot_data(stock_data, predictions, ticker_symbol):
    fig = go.Figure()

    # Add candlestick chart
    fig.add_trace(go.Candlestick(x=stock_data.index,
                                 open=stock_data['Open'],
                                 high=stock_data['High'],
                                 low=stock_data['Low'],
                                 close=stock_data['Close'],
                                 name='Historical Data'))

    # Add 30, 60, 90 days average lines
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].rolling(window=30).mean(), name='30 Days Avg', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].rolling(window=60).mean(), name='60 Days Avg', line=dict(color='yellow')))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].rolling(window=90).mean(), name='90 Days Avg', line=dict(color='brown')))

    # Add predictions
    colors = ['red', 'green', 'purple']
    i = 0
    for key, value in predictions.items():
        years_ago = int(key.split('year -')[1])
        base_year = 2024
        prediction_year = base_year - years_ago
        start_date = f'{prediction_year}-01-01'
        end_date = f'{prediction_year}-12-31'
        # Align prediction dates with the stock data
        prediction_dates = pd.date_range(start=start_date, end=end_date, freq='D')
        fig.add_trace(go.Scatter(x=prediction_dates, y=value, name=f'Prediction {key}', line=dict(color=colors[i])))
        i += 1

    fig.update_layout(title=f'Stock Data and Predictions for {ticker_symbol}',
                      xaxis_title='Date',
                      yaxis_title='Stock Price')

    # Return the HTML content of the plot
    return fig.to_html(full_html=False)

    pass