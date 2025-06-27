import os
import requests

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def get_google_results(query):
    if not SERPAPI_KEY:
        raise ValueError("SERPAPI_KEY environment variable not set.")

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 10,
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    results = []
    for result in data.get("organic_results", []):
        if "instagram.com" in result.get("link", ""):
            results.append(result["link"])
    return results
