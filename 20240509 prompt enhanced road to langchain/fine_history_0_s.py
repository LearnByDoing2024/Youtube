import csv
from gnews import GNews
from openai import OpenAI
import re

def get_gdpr_news(num_pages):
    google_news = GNews(language='en', country='EU', period='180d', max_results=1)
    news_list = []

    try:
        with open('gdpr_fines.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Title', 'Content', 'URL', 'Publisher', 'Fined Entity', 'Fined Amount', 'Fine Reason']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(num_pages):
                page_news = google_news.get_news("GDPR fine")
                for article in page_news:
                    gdpr_details = extract_gdpr_details(article['description'])
                    for detail in gdpr_details:  # Handle multiple entities
                        writer.writerow({
                            'Date': article['published date'],
                            'Title': article['title'],
                            'Content': article['description'],
                            'URL': article['url'],
                            'Publisher': article['publisher'],
                            'Fined Entity': detail.get('entity', ''),
                            'Fined Amount': detail.get('amount', ''),
                            'Fine Reason': detail.get('reason', '')
                        })
                    news_list.append(article)

        return news_list

    except Exception as e:
        print(f"Error retrieving news: {e}")
        return []

def extract_gdpr_details(text):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="your_api_key")
    completion = client.chat.completions.create(
        model="text-davinci-002",
        messages=[
            {"role": "system", "content": "Extract GDPR fine details including entity, amount, and reason."},
            {"role": "user", "content": text}
        ],
        temperature=0.1,
    )

    try:
        response = completion.choices[0].message.content
        print("LLM Response:", response)  # Log the response to debug
        entities = re.findall(r"\*\*(.+?)\*\*: Fined €([\d\.]+) million for (.+?)(?=\.\n|\n\n)", response)

        details_list = []
        for entity, amount, reason in entities:
            details_list.append({
                'entity': entity,
                'amount': f"EUR {amount} million",
                'reason': reason
            })

        return details_list
    except Exception as e:
        print(f"Error processing GDPR details: {e}")
        return []
    
# Example usage:
num_pages = 1  # Number of pages to fetch from Google News

news_list = get_gdpr_news(num_pages)
print("GDPR fine details extracted and saved.")
