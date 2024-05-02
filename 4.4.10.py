import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://parsinger.ru/4.1/1/index4.html'

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

sprisok_kart = soup.find_all('a', {'class': 'name_item product_name'})
# print(sprisok_kart)

for card in sprisok_kart:
    print(card.get_text(strip=True))