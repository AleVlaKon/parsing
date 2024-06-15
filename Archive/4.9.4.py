import requests
from bs4 import BeautifulSoup
import lxml
import csv

headers = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=headers)
    writer.writeheader()

    for page in range(1, 5):
        html = requests.get(f'https://parsinger.ru/html/index4_page_{page}.html')
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        
        for item in soup.find_all('div', 'img_box'):
            decription = [i.text.strip() for i in item.select('div.description li')]

            item_dict = {
                'Наименование': item.find('a', 'name_item').text.strip(),
                'Бренд': decription[0].replace('Бренд: ', '').strip(),
                'Форм-фактор': decription[1].split()[1].strip(),
                'Ёмкость': decription[2].replace('Ёмкость: ', '').strip(),
                'Объем буферной памяти': decription[3].replace('Объем буферной памяти: ', '').strip(),
                'Цена': item.find('p', 'price').text.strip(),
            }
            writer.writerow(item_dict)
