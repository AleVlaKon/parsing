import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/table/1/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')[1:]

point = set()

for row in table_rows:
    set_i = {float(i.text) for i in row.find_all('td')}
    point |= set_i


print(sum(point))
