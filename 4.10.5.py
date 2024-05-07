import requests
from bs4 import BeautifulSoup
import lxml
import json

json_list = []

for cat in range(1, 6):
    for pag in range(1, 5):
        html = requests.get(f'https://parsinger.ru/html/index{cat}_page_{pag}.html')
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        for item in soup.find_all('div', 'img_box'):
            decription = [i.text.split(': ') for i in item.select('div.description li')]
            decription_dict = {i[0].strip(): i[1].strip() for i in decription}
            name = {'Наименование': item.find('a', 'name_item').text.strip()}
            price = {'Цена': item.find('p', 'price').text.strip()}
            merged_dictionary = {**name, **decription_dict, **price}

            json_list.append(merged_dictionary)

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(json_list, file, indent=4, ensure_ascii=False)
