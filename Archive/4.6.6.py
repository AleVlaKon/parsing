import requests
from bs4 import BeautifulSoup
import lxml

list_of_links = []

begin = 'https://parsinger.ru/html/'
for cat in range(1, 6):
    for pag in range(1, 5):
        html = requests.get(f'https://parsinger.ru/html/index{cat}_page_{pag}.html')
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'html.parser')
        list_pagen = [f'{begin}{i.get("href")}' for i in soup.select('a.name_item')]
        list_of_links.extend(list_pagen)

sum_articles = 0
print(len(list_of_links))
for i in list_of_links:
    html = requests.get(i)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    count = soup.select_one('#in_stock').text.split()[2]
    price = soup.select_one('#price').text.split()[0]
    sum_articles += int(count) * int(price)

print(sum_articles)
