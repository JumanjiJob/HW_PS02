import requests
import pprint

parametr = {
    'q':'JavaScript'
}

response = requests.get('https://api.github.com/search/repositories', params=parametr)

response_json = response.json()
#pprint.pprint(response_json)

print(f"количество репозиотриев с использованием js: {response_json['total_count']}")