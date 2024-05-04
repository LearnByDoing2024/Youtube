import csv
from gnews import GNews
from autogen import ConversableAgent

def get_latest_news(stock_symbol, num_pages):
    google_news = GNews(language='en', country='US', period='100d', start_date=None, end_date=None, max_results=5000, exclude_websites=None,proxy=None)
    #change max result to 1 to test codes
    news_list = []

    try:
        with open('news_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Title', 'Content', 'URL', 'Publisher', 'LLMResponse', 'Sentiment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(num_pages):
                page_news = google_news.get_news(stock_symbol)
                for article in page_news:
                    llm_response = analyze_sentiment(article['description'])  # Analyze sentiment
                    print("LLM Response:", llm_response)  # Print the LLM response
                    sentiment = extract_sentiment(llm_response)  # Extract sentiment from LLM response
                    writer.writerow({'Date': article['published date'], 'Title': article['title'], 'Content': article['description'], 'URL': article['url'], 'Publisher': article['publisher'], 'LLMResponse': llm_response, 'Sentiment': sentiment})
                    news_list.append(article)

        return news_list

    except Exception as e:
        print(f"Error retrieving news: {e}")
        return []

from openai import OpenAI

def analyze_sentiment(text):
    # Initiate conversation with Gemma and get sentiment label
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {"role": "system", "content": "You are agent, a professional financial analyst specializing sentiment assessment. Reply only **POSITIVE**, **NEGATIVE**, **NEUTRAL**, such words."},
            {"role": "user", "content": text}
        ],
        temperature=0.1,
    )

    try:
        llm_response = completion.choices[0].message.content
        return llm_response
    except AttributeError:
        return ""


def extract_sentiment(llm_response):
    # Extract sentiment from LLM response
    if "**POSITIVE**" in llm_response:
        return "POSITIVE"
    elif "**NEGATIVE**" in llm_response:
        return "NEGATIVE"
    elif "**NEUTRAL**" in llm_response:
        return "NEUTRAL"
    else:
        return "UNKNOWN"

# Example usage:
stock_symbol = "AAPL"  # Example stock symbol
num_pages = 10  # Number of pages to fetch from Google News

news_list = get_latest_news(stock_symbol, num_pages)
print("News articles retrieved and sentiment analyzed.")