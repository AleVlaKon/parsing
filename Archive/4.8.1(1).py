import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.8/1/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

name, age = [i.text for i in table_rows[0] if i.text.strip()]


list_table = []

for row in table_rows[1:]:
    columns = row.find_all('td')
    list_table.append({name: columns[0].text, age: columns[1].text})

print(list_table)