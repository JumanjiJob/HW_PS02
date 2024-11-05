import requests

url = " https://api.github.com"

parametr = {
    "q": "html"
}
response = requests.get(url, params=parametr)

response_json = response.json()

print(response.status_code)
print(response_json)