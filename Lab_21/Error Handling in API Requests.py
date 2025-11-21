import requests

url = 'https://jsonplaceholder.typicode.com/posts/1000'

a = requests.get(url)

if a.status_code == 200:
    post = a.json()
    print("Fetched Post:", post)
else:
    print(f"Error: {a.status_code} - {a.reason}")
