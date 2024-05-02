import requests


response = requests.get(url='https://parsinger.ru/3.4/1/json_weather.json')
response.encoding = 'utf-8'
# for i in response.json():
#     print(i)

print(min(response.json(), key=lambda x: int(x['Температура воздуха'].rstrip('°C'))))
