import requests
from bs4 import BeautifulSoup
import lxml
import json

list_of_links = []

begin = 'https://parsinger.ru/html/'
for i in range(1, 5):
    html = requests.get(f'https://parsinger.ru/html/index2_page_{i}.html')
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    list_pagen = [f'{begin}{i.get("href")}' for i in soup.select('a.name_item')]
    list_of_links.extend(list_pagen)

json_list = []

for link in list_of_links:
    html = requests.get(link)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')

    tag_description_li = soup.select('#description li')
    description_dict = {i.get('id'): i.text.split(': ')[1].strip() for i in tag_description_li}
    prices = soup.select('div.sale span')
    prices_dict = {i.get('id'): i.text.strip() for i in prices}

    json_dict = {
        "categories": "mobile",
        "name": soup.find('p', id='p_header').text.strip(), 
        "article": soup.select_one('p.article').text.split(': ')[1].strip(),
        "description": description_dict,
        "count": soup.find(id='in_stock').text.split(': ')[1]
    }
    json_dict.update(prices_dict)
    json_dict["link"] = link
    json_list.append(json_dict)


with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(json_list, file, indent=4, ensure_ascii=False)