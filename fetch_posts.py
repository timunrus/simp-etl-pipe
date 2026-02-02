import requests

URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(URL)
response.raise_for_status()

posts = response.json()

print(f"Кол-во записей = {len(posts)}")
print(f"Первая запись - {posts[0]}")
