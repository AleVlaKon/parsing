import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.1/1/index6.html')
html.encoding = 'utf-8'


def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    section3 = soup.find('section', id='section3')

    sibling = section3.find('p', class_='section-text').next_sibling.strip()
    sibling = section3.div.p.next_sibling.strip()
    return sibling


print(get_html(html))