import requests

response = requests.get(url='https://parsinger.ru/3.4/2/index.html')
response.encoding = 'UTF-8'
print(response.text)