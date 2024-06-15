import requests

sum_status_codes = 0

for i in range(1, 201):
    url = f'https://parsinger.ru/3.3/1/{i}.html'
    response = requests.get(url)
    sum_status_codes += response.status_code

print(sum_status_codes)