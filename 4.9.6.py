import requests
from bs4 import BeautifulSoup
import csv


with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    for cat in range(1, 6):
        for pag in range(1, 5):
            html = requests.get(f'https://parsinger.ru/html/index{cat}_page_{pag}.html')
            html.encoding = 'utf-8'
            soup = BeautifulSoup(html.text, 'lxml')
            for link in soup.select('div.item_card div.item'):
                print(len(link))
                # name = soup.select_one('a.name_item').text.strip()
                # attributes = [i.text.split(':')[1].strip() for i in soup.select('.description li')]
                # price = soup.select_one('p.price').text.strip()
                # print(attributes)
                # writer.writerow([name] + attributes + [price])
        break


