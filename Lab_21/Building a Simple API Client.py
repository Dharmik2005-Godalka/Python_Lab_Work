import requests

class Client:

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        url = f"{self.base_url}/posts"
        x = requests.get(url)
        if x.status_code == 200:
            return x.json()
        return None

    def create_post(self, title, body, userId):
        url = f"{self.base_url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": userId
        }
        a = requests.post(url, json=data)
        if a.status_code == 201:
            return a.json()
        return None


# Client class:
client = Client()

posts = client.get_posts()
if posts:
    print("\nFetched Posts:")
    for post in posts[:5]:
        print(post["title"])

post = client.create_post("Demo Post", "This is a demo content", 5)
if post:
    print("\nNew Post Created Successfully:")
    print(post)
