import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
html.encoding = 'utf-8'

def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    # Допишите поиск и извлечение email
    price = int(soup.find(id='price').text[:-4])
    old_price = int(soup.find(id='old_price').text[:-4])
    
    print(price, old_price)

    return (old_price - price) * 100 / old_price

print(get_html(html))