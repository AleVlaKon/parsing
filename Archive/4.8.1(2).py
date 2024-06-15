import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.8/2/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')


headers = [i.text for i in table.find_all('th')]
rows = table.find_all('tr')[1:]

list_table = []
for row in rows:
    col_data = (col.text for col in row.find_all('td'))
    data = dict(zip(headers, col_data))
    list_table.append(data)

print(list_table)
