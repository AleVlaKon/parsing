import requests
from bs4 import BeautifulSoup
import lxml

html = requests.get('http://parsinger.ru/html/index1_page_1.html')
html.encoding = 'utf-8'

def get_html(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    # Допишите поиск и извлечение email
    email_div = soup.find_all(class_='price')

    emails = [i.strong.next_sibling.strip() for i in email_div]

    return emails

print(get_html(html))