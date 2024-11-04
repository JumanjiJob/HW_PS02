import requests

response = requests.get('https://www.google.com/search?q=%D0%B3%D1%83%D0%B3%D0%BB+%D0%B4%D0%B8%D1%81%D0%BA&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIPCAMQLhgDGI8BGLQCGOoCMhEIBBAAGAMYQhiPARi0AhjqAjIRCAUQABgDGEIYjwEYtAIY6gIyEQgGEAAYAxhCGI8BGLQCGOoCMg8IBxAuGAMYjwEYtAIY6gLSAQkxNTIwajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8')
print(response.status_code)

# is response.ok:
#     print("Запрос успешно выполнен")
# else:
#     ("произошла ошибка")

print(response.content)