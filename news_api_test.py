import requests
import json

API_KEY = "26d30a9230c44ef78dcc04c737ba4346"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

# Print nicely
print(json.dumps(data, indent=2))

# Save to file
with open("news.json", "w") as f:
    json.dump(data, f)

print("Data saved to news.json")