import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/everything"

params = {
    "q": "artificial intelligence",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5,
    "apiKey": API_KEY
}

print("=== SAMPLE REQUEST ===")
print("URL:", url)
print("PARAMS:", params)
print()

print("Sending request to NewsAPI...")
response = requests.get(url, params=params)

print("=== STATUS ===")
print(f"Status code: {response.status_code}")
print()

data = response.json()

print("=== SAMPLE RESPONSE ===")
print(data)
print()

print(f"Total results available: {data.get('totalResults')}")
print(f"Articles received: {len(data.get('articles', []))}")
print()

for i, article in enumerate(data.get("articles", [])):
    print(f"--- Article {i+1} ---")
    print(f"Title: {article.get('title')}")
    print(f"Source: {article.get('source', {}).get('name')}")
    print(f"Published: {article.get('publishedAt')}")
    print(f"URL: {article.get('url')}")
    print(f"Desc: {article.get('description')}")
    print()