import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# Data:
post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

# POST request:
a = requests.post(url, json=post)

# Check response:
if a.status_code == 201:
    created_post = a.json()
    print("Created Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {a.status_code}")
