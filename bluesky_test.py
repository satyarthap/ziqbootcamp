import os
from atproto import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USERNAME = os.getenv("BSKY_USERNAME")
PASSWORD = os.getenv("BSKY_APP_PASSWORD")

print("=== SAMPLE REQUEST ===")
print("Method: client.login(USERNAME, PASSWORD)")
print("Method: client.app.bsky.feed.search_posts({'q': 'data engineering', 'limit': 5})")
print()

print("Logging in to Bluesky...")
client = Client()
client.login(USERNAME, PASSWORD)

print("Login successful!")
print()

print("Searching for posts...")
results = client.app.bsky.feed.search_posts({
    "q": "data engineering",
    "limit": 5,
})

print("=== SAMPLE RESPONSE ===")
print(results)
print()

print(f"Posts found: {len(results.posts)}")
print()

for i, post in enumerate(results.posts):
    print(f"--- Post {i+1} ---")
    print(f"Author: {post.author.handle}")
    print(f"Name: {post.author.display_name}")
    print(f"Text: {post.record.text}")
    print(f"Posted: {post.indexed_at}")
    print(f"Likes: {post.like_count}")
    print(f"Reposts: {post.repost_count}")
    print(f"Replies: {post.reply_count}")
    print()