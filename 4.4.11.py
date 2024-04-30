import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('https://parsinger.ru/4.1/1/index4.html')
html.encoding = 'utf-8'


def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    prices = soup.find_all('p', class_='price product_price')

    count = 0
    for price in prices:
        int_price = int(price.string[:-4].replace(' ', ''))
        count += int_price

    return count

print(get_html(html))