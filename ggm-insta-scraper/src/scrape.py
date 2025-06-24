# Scraper for Instagram search queries
from googlesearch import search
import pandas as pd

queries = [
    "site:instagram.com Shark Tank business made in China",
    "site:instagram.com American startup product made in India",
    "site:instagram.com small batch product made in Vietnam"
]

results = []

for query in queries:
    print(f"Searching: {query}")
    for url in search(query, num_results=20, pause=2.0):
        if "instagram.com" in url and "/p/" not in url:
            results.append({"Query": query, "Instagram URL": url})

df = pd.DataFrame(results)
df.to_excel("data/scraped_instagram_links.xlsx", index=False)
print("✅ Export complete: scraped_instagram_links.xlsx")
