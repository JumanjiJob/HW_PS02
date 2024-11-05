import requests

# img = "https://sun9-44.userapi.com/impg/-kXS8Ak8NG-gierS3Z95TTw85eEV7a8b-3yJvg/MZps74PCLd0.jpg?size=886x1080&quality=96&sign=26881e05281c5fb5dc23c2240ea57721&type=album"
# response = requests.get(img)
#
# with open("test.jpg", "wb") as file:
#     file.write(response.content)

response = requests.get('https://google.com')

print(response.status_code)

print(response.headers)

print(response.text)