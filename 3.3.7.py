import requests



for i in range(1, 101):
    url = f'https://parsinger.ru/3.3/4/{i}.html'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Первая доступная страница: {url}.html")
        break

for i in range(100, 0, -1):
    url = f'https://parsinger.ru/3.3/4/{i}.html'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Последняя доступная страница: {url}.html")
        break

