# plotting.py
import plotly.graph_objs as go

# Plot economic data
def plot_economic_data(series_dict, title, series_labels=None):
    fig = go.Figure()
    for label, series in series_dict.items():
        fig.add_trace(go.Scatter(x=series.index, y=series.values, mode='lines', name=label))
    if series_labels is not None:
        for i, label in enumerate(series_labels):
            fig.data[i].name = label
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Rate', legend_title="Indicator")
    return fig

# Plot candlestick chart with moving averages
def plot_candlestick_with_moving_averages(data, title, ma_30=None, ma_60=None, ma_90=None, selected_symbol=None):
    fig = go.Figure(data=[
        go.Candlestick(x=data['Date'], open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Candlestick'),
    ])
    if ma_30 is not None:
        fig.add_trace(go.Scatter(x=data['Date'], y=ma_30, line=dict(color='blue', width=1), name='30D MA'))
    if ma_60 is not None:
        fig.add_trace(go.Scatter(x=data['Date'], y=ma_60, line=dict(color='red', width=1), name='60D MA'))
    if ma_90 is not None:
        fig.add_trace(go.Scatter(x=data['Date'], y=ma_90, line=dict(color='green', width=1), name='90D MA'))
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=False)
    return fig

"""


"""