import requests
from bs4 import BeautifulSoup
import lxml
import csv

headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)
    

    list_of_links = []

    begin = 'https://parsinger.ru/html/'
    for i in range(1, 5):
        html = requests.get(f'https://parsinger.ru/html/index1_page_{i}.html')
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        list_pagen = [f'{begin}{i.get("href")}' for i in soup.select('a.name_item')]
        list_of_links.extend(list_pagen)

    # print(list_of_links)

    for link in list_of_links:
        html = requests.get(link)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        name = soup.find('p', id='p_header').text.strip()
        articul = soup.find('p', class_='article').text.split(':')[1].strip()
        nalichie = soup.find(id='in_stock').text.split(':')[1].strip()
        price = soup.find(id='price').text
        old_price = soup.find(id='old_price').text
        attributes = [i.text.split(':')[1].strip() for i in soup.select('#description li')]
        writer.writerow([name, articul] + attributes + [nalichie, price, old_price, link])






    