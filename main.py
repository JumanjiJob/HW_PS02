import pprint

import requests
import json

response = requests.get('https://api.github.com')
print(response.status_code)

# if response.ok:
#     print("Запрос успешно выполнен")
# else:
#     print("произошла ошибка")

print(response.text)
response_json = response.json()
pprint.pprint(response_json)