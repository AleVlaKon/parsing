import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.1/1/index4.html')
html.encoding = 'utf-8'


def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    tags_li = soup.select('li')
    for tag in tags_li:
        print(tag['id'])

get_html(html)