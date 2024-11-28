import json
import os
import wikipediaapi
from datetime import datetime

# Get the data directory path
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def get_data_file_path(filename):
    """Get the full path for a data file."""
    return os.path.join(DATA_DIR, filename)

def get_current_date():
    """Get current date in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def extract_main_terms(query):
    """
    Extract main terms from a query for better Wikipedia search.
    Removes common words and keeps key terms.
    """
    # Common words to filter out
    stop_words = {'what', 'when', 'where', 'which', 'who', 'whom', 'whose', 'why', 'how',
                 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                 'have', 'has', 'had', 'do', 'does', 'did',
                 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                 'with', 'about', 'between', 'into', 'through', 'after', 'before',
                 'during', 'without', 'of', 'by', 'from'}
    
    # Split query into words and filter out stop words
    words = query.lower().split()
    key_terms = [word for word in words if word not in stop_words]
    
    return key_terms

def search_wikipedia(query, language="en"):
    """
    Search and fetch Wikipedia content based on the query.
    Handles both direct page lookups and search queries.

    Args:
        query (str): The search query or page title.
        language (str): Language of the Wikipedia.

    Returns:
        dict: A dictionary containing the page title, summary, URL, and content.
    """
    current_date = get_current_date()
    print(f"[{current_date}] Searching Wikipedia for: {query}")
    
    # Define a valid User-Agent string
    user_agent = "MyWikipediaBot/1.0 (https://example.com; myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(language=language, user_agent=user_agent)
    
    def is_good_match(page):
        """Check if the page has enough content to be useful."""
        return (page.exists() and 
                len(page.summary) > 100 and  # Summary should be substantial
                not page.title.endswith("(disambiguation)"))  # Avoid disambiguation pages
    
    # First try: Direct page lookup
    page = wiki_wiki.page(query)
    if is_good_match(page):
        print(f"[{current_date}] Found exact match: {page.title}")
        return {
            "title": page.title,
            "summary": page.summary,
            "url": page.fullurl,
            "content": page.text,
            "search_method": "direct"
        }
    elif page.exists() and page.title.endswith("(disambiguation)"):
        # If it's a disambiguation page, try to find a more specific match
        print(f"[{current_date}] Found disambiguation page, looking for better match")
        # Try with common suffixes
        suffixes = ["(concept)", "(technology)", "(computing)", "(science)"]
        for suffix in suffixes:
            specific_page = wiki_wiki.page(f"{query} {suffix}")
            if is_good_match(specific_page):
                print(f"[{current_date}] Found better match: {specific_page.title}")
                return {
                    "title": specific_page.title,
                    "summary": specific_page.summary,
                    "url": specific_page.fullurl,
                    "content": specific_page.text,
                    "search_method": "disambiguation_resolution"
                }
    
    # Second try: Search using main terms
    key_terms = extract_main_terms(query)
    print(f"[{current_date}] Trying key terms: {', '.join(key_terms)}")
    
    # Try combinations of key terms
    for i in range(len(key_terms), 0, -1):
        search_term = ' '.join(key_terms[:i])
        page = wiki_wiki.page(search_term)
        if is_good_match(page):
            print(f"[{current_date}] Found match using terms: {search_term}")
            return {
                "title": page.title,
                "summary": page.summary,
                "url": page.fullurl,
                "content": page.text,
                "search_method": "key_terms"
            }
    
    # If no matches found
    print(f"[{current_date}] No suitable Wikipedia content found for the query")
    return {"error": f"No suitable Wikipedia content found for: {query}"}

def save_results_to_json(results, filename="wikipedia.json"):
    """
    Save results to a JSON file.

    Args:
        results (dict): Results to save.
        filename (str): Name of the JSON file.
    """
    try:
        filepath = get_data_file_path(filename)
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)
        print(f"Results saved to {filepath}")
    except Exception as e:
        print(f"Error while saving results to JSON: {e}")

if __name__ == "__main__":
    # Test cases
    test_queries = [
        "Python programming language",  # Direct article title
#        "What is artificial intelligence",  # Question
#        "How do computers work",  # Complex question
#        "GPT",  # Single term
    ]
    
    for query in test_queries:
        print("\nTesting query:", query)
        try:
            results = search_wikipedia(query)
            if "error" in results:
                print(results["error"])
            else:
                print(f"Found article: {results['title']}")
                print(f"Search method: {results['search_method']}")
                print(f"Summary length: {len(results['summary'])} chars")
                # Save results to JSON file
                save_results_to_json(results)
        except Exception as e:
            print(f"Error: {e}")
