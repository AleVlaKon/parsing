import requests
from bs4 import BeautifulSoup
import lxml

list_of_names = []

for i in range(1, 5):
    html = requests.get(f'http://parsinger.ru/html/index3_page_{i}.html')
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    list_pagen = [i.text for i in soup.select('.name_item')]
    list_of_names.append(list_pagen)


print(list_of_names)
with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_of_names))