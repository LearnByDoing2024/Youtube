import json
import os
from gnews import GNews

# Get the data directory path
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def get_data_file_path(filename):
    """Get the full path for a data file."""
    return os.path.join(DATA_DIR, filename)

def search_google_news(query, max_results=5, language="en", country="US"):
    """
    Perform a Google News search using the given query.

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
        language (str): Language of the news articles.
        country (str): Country for regional news.

    Returns:
        list: A list of dictionaries with search results.
    """
    google_news = GNews(language=language, country=country, max_results=max_results)
    results = google_news.get_news(query)
    return results

def save_results_to_json(results, filename="gn.json"):
    """
    Save search results to a JSON file.

    Args:
        results (list): Search results to save.
        filename (str): Name of the JSON file.
    """
    filepath = get_data_file_path(filename)
    with open(filepath, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)
    print(f"Results saved to {filepath}")

if __name__ == "__main__":
    query = "GPT"
    max_results = 5
    try:
        # Perform the search
        results = search_google_news(query, max_results=max_results)
        
        # Save results to JSON
        save_results_to_json(results, filename="gnews.json")
        
        # Print results to the console
        for idx, result in enumerate(results, 1):
            print(f"Result {idx}:")
            print(f"Title: {result.get('title')}")
            print(f"URL: {result.get('url')}")
            print(f"Published Date: {result.get('published date')}")
            print(f"Description: {result.get('description')}")
            print("-" * 80)
    except Exception as e:
        print(f"Error: {e}")
