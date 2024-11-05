import requests

url = "https://jsonplaceholder.typicode.com/posts"

parametr = {
    "userId": 1
}

response = requests.get(url, params=parametr)

print(response.status_code)

print(response.headers)

print(response.text)
