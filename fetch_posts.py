import requests

URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(URL)
response.raise_for_status()

posts = response.json()

# print(f"Кол-во записей = {len(posts)}")
# print(f"Первая запись - {posts[0]}")

transformed_posts = []

for post in posts:
    new_dict = {
        "post_id": post["id"],
        "author_id": post["userId"],
        "title": post["title"]
    }
    transformed_posts.append(new_dict)

print(f"Кол-во записей в измененном списке = {len(transformed_posts)}")
print(f"Первая запись в новом списке - {transformed_posts[0]}")