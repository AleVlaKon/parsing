import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.8/8/index.html')
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, 'lxml')

ht_list = [int(i.text) for i in soup.find_all('th', colspan=True)]
hd_list = [int(i.text) for i in soup.find_all('td', colspan=True) if len(i) == 1]

print(sum(ht_list) + sum(hd_list))


