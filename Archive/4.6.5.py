import requests
from bs4 import BeautifulSoup
import lxml

list_of_links = []

begin = 'https://parsinger.ru/html/'
for i in range(1, 5):
    html = requests.get(f'https://parsinger.ru/html/index3_page_{i}.html')
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    list_pagen = [f'{begin}{i.get("href")}' for i in soup.select('a.name_item')]
    list_of_links.extend(list_pagen)

sum_articles = 0

for i in list_of_links:
    html = requests.get(i)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    articul = soup.select_one('p.article').text.split()[1]
    sum_articles += int(articul)

print(sum_articles)
