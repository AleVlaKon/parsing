import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/table/5/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')[1:]

point = 0

for row in table_rows:
    set_orange = float(row.select_one('td.orange').text)
    print(set_orange)
    # set_orange = [float(i.text) for i in row.find_all('td', class_='orange')][0]
    set_blue = [float(i.text) for i in row.find_all('td')][-1]
    # print(set_blue)
    point += set_orange * set_blue


print(point)
