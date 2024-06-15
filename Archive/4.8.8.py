import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.8/7/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

count = 0

for cell in soup.find_all('td'):
    if int(cell.text) % 3 == 0:
        count += int(cell.text)

print(count)

