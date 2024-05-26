import requests

html = requests.get(f'https://parsinger.ru/downloads/get_json/res.json')
html.encoding = 'utf-8'
json_string = html.json()
print(len(json_string))
result = {}

for i in json_string:
    category = i.get('categories')
    stoimost_tovarov = int(i.get('count')) * int(i.get('price').replace(' руб', ''))
    result[category] = result.get(category, 0) + stoimost_tovarov

print(result)