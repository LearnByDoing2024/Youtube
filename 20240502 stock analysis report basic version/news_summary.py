#news_summary.py
import datetime
from jinja2 import Template
import GoogleNews as google_news
from openai import OpenAI

# Set up the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_latest_news(stock_symbol):
    gn = google_news.GoogleNews()
    gn.set_lang('en')
    gn.set_encode('utf-8')
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)  # Covering the past 30 days
    search_query = f"{stock_symbol} stock"
    gn.set_time_range(start_date.strftime('%m/%d/%Y'), end_date.strftime('%m/%d/%Y'))
    gn.search(search_query)
    return gn.results()

def summarize_news(news_articles, stock_symbol):
    messages = [
        {"role": "system", "content": "You are an intelligent assistant. Provide concise, reasoned answers."},
        {"role": "user", "content": f"Summarize the latest news about {stock_symbol}, and comment on its impact on the stock price using bullet points. Include a final suggestion on stock position for long and short term."}
    ]
    for article in news_articles:
        content = f"* {article['title']}: {article['desc']}"
        messages.append({"role": "user", "content": content})
    completion = client.chat.completions.create(
        model="bartowski/stable-code-instruct-3b-GGUF",
        messages=messages,
        temperature=0.7
    )
    summary = completion.choices[0].message.content
    news_urls = [article['link'] for article in news_articles]
    return summary, news_urls

def generate_html_report(stock_data, predictions, news_summary, company_name):
    news_summary_text, news_urls = news_summary
    template = Template(open("report.html", "r").read())
    html_report = template.render(
        ticker=company_name,
        stock_data=stock_data,
        predictions=predictions,
        news_summary_text=news_summary_text,
        news_urls=news_urls
    )
    return html_report
