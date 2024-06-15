import requests
from bs4 import BeautifulSoup
import lxml
import json


html = requests.get('https://parsinger.ru/4.8/6/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

list_of_auto = []

ht_list = [i.text for i in soup.find_all('th')]
print(ht_list)

table = soup.find_all('tr')[1:]

def filter_func(row):
    kriterii = (
        int(row[1].text) >= 2005, 
        int(row[7].text) <= 4000000,
        row[4].text == 'Бензиновый'
    )
    return all(kriterii)

for row in table:
    row_auto = row.find_all('td')
    if filter_func(row_auto):
        auto = {
            ht_list[0]: row_auto[0].text,
            ht_list[1]: int(row_auto[1].text),
            ht_list[4]: row_auto[4].text,
            ht_list[7]: int(row_auto[7].text),
        }
        list_of_auto.append(auto)

list_of_auto = sorted(list_of_auto, key=lambda x: x["Стоимость авто"])
print(json.dumps(list_of_auto, indent=4, ensure_ascii=False))

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(json.dumps(list_of_auto, indent=4, ensure_ascii=False))