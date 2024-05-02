import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('http://parsinger.ru/html/index1_page_1.html')
html.encoding = 'utf-8'

def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    # Допишите поиск и извлечение email
    price_div = soup.find_all(class_='price')

    emails = [int(i.text[:-4]) for i in price_div]
    print(emails)

    return sum(emails)

print(get_html(html))