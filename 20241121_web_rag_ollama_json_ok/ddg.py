import json
import os
from duckduckgo_search import DDGS

# Get the data directory path
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def get_data_file_path(filename):
    """Get the full path for a data file."""
    return os.path.join(DATA_DIR, filename)

def search_duckduckgo(query, max_results=5):
    """
    Perform a DuckDuckGo search using the given query.

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.

    Returns:
        list: A list of dictionaries with search results.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results, region="wt-wt")
        return list(results)

def save_results_to_json(results, filename="ddg.json"):
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
        results = search_duckduckgo(query, max_results)
        
        # Save results to JSON
        save_results_to_json(results, filename="ddg.json")
        
        # Print results to the console
        for idx, result in enumerate(results, 1):
            print(f"Result {idx}:")
            print(f"Title: {result.get('title')}")
            print(f"URL: {result.get('href')}")
            print(f"Snippet: {result.get('body')}")
            print("-" * 80)
    except Exception as e:
        print(f"Error: {e}")
