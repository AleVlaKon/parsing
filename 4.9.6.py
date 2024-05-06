import requests
from bs4 import BeautifulSoup
import csv

list_of_links = []

begin = 'https://parsinger.ru/html/'
for cat in range(1, 6):
    for pag in range(1, 5):
        html = requests.get(f'https://parsinger.ru/html/index{cat}_page_{pag}.html')
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'html.parser')
        list_pagen = [f'{begin}{i.get("href")}' for i in soup.select('a.name_item')]
        list_of_links.extend(list_pagen)

for i in list_of_links:
    print(i)

# with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';')

#     for link in list_of_links:
#         name = soup.select_one('a.name_item').text.strip()
#         attributes = [i.text.split(':')[1].strip() for i in soup.select('#description li')]
#         price = soup.select_one('p.price').text.strip()
#         writer.writerow([name] + attributes + [price])