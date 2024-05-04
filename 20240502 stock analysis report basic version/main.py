# main.py
from flask import Flask, request, render_template
import pandas as pd
import data
import predict
import plot
import download_data
import logging
import os
import news_summary  # Import the news_summary module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            ticker_symbol = request.form['ticker']
            stock_data, predictions, plot_html, news_summary_text, company_name = analyze(ticker_symbol)  # Rename the variable to avoid conflicts
            if not stock_data.empty and len(predictions) > 0 and plot_html and news_summary_text:  # Change the variable name here as well
                stock_data_last10 = stock_data.tail(10)
                return render_template('report.html', company_name=company_name, stock_data=stock_data_last10, plot_html=plot_html, news_summary=news_summary_text)  # Change the variable name here as well
            else:
                return render_template('error.html', message="Failed to analyze the stock. Please try again.")
        else:
            symbols = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values.tolist()
            return render_template('index.html', symbols=symbols)
    except Exception as e:
        return render_template('error.html', message=f"An unexpected error occurred: {str(e)}")

def analyze(ticker_symbol):
    try:
        logging.info(f"Downloading data for {ticker_symbol}")
        download_data.download_data(ticker_symbol)

        logging.info(f"Fetching data for {ticker_symbol}")
        stock_data, company_name = data.fetch_data(ticker_symbol)  # Fetch the company name here

        logging.info(f"Predicting data for {ticker_symbol}")
        predictions = predict.train_predict_model(stock_data)

        logging.info(f"Plotting data for {ticker_symbol}")
        plot_html = plot.plot_data(stock_data, predictions, ticker_symbol)

        logging.info(f"Getting news summary for {ticker_symbol}")
        news_articles = news_summary.get_latest_news(ticker_symbol)
        news_summary_text = news_summary.summarize_news(news_articles, ticker_symbol)

        return stock_data, predictions, plot_html, news_summary_text, company_name

    except Exception as e:
        logging.error(f"Error processing {ticker_symbol}: {e}")
        return pd.DataFrame(), {}, None, "", ""


if __name__ == "__main__":
    app.run(debug=True)
