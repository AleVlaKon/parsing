import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/table/2/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')[1:]

count = 0

for row in table_rows:
    count += float(row.find('td').text)


print(count)
