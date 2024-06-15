import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/table/5/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')
table_headers = [i.text for i in table.find_all('th')]

table_rows = table.find_all('tr')[1:]

sum_columns = [0] * len(table_headers)

for row in table_rows:
    set_orange = [float(i.text) for i in row.find_all('td')]
    for i in range(len(set_orange)):
        sum_columns[i] += set_orange[i]

sum_columns = [round(i, 3) for i in sum_columns]

result = dict(zip(table_headers, sum_columns))
print(result)
