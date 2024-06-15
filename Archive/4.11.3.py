import requests

html = requests.get(f'https://parsinger.ru/downloads/get_json/res.json')
html.encoding = 'utf-8'
json_string = html.json()
print(len(json_string))
result = {}

for i in json_string:
    category = i.get('categories')
    result[category] = result.get(category, 0) + int(i.get('count'))

print(result)
