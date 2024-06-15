import requests

sum_status_codes = 0

for i in range(1, 201):
    url = f'https://parsinger.ru/3.3/1/{i}.html'
    response = requests.get(url)
    if response.status_code == 200:
        print(url)