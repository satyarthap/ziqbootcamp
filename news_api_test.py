import requests

API_KEY = "demo_key"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

print(response.json())