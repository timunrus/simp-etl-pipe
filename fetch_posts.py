import requests
import psycopg2

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

# print(f"Кол-во записей в измененном списке = {len(transformed_posts)}")
# print(f"Первая запись в новом списке - {transformed_posts[0]}")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="de_db",
    user="de_user",
    password="de_password"
)

cursor = conn.cursor()

insert_query = """
INSERT INTO posts (post_id, author_id, title)
VALUES (%s, %s, %s)
ON CONFLICT (post_id) DO NOTHING;
"""

for post in transformed_posts:
    cursor.execute(
        insert_query,
        (post["post_id"], post["author_id"], post["title"])
    )
conn.commit()
cursor.close()
conn.close()

print("Данные загружены в БД")