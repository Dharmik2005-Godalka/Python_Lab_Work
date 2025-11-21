import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# GET request:
a = requests.get(url)

# Check response:
if a.status_code == 200:
    posts = a.json()
    print("Fetched Posts:")
    for post in posts[:5]: 
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {a.status_code}")
