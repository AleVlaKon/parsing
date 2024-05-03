import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}

search_param = {"textSearch":"","filters":{"OWNER":{"value":{"values":[5567044],"start":0,"limit":100,"textSearch":""}},"BASE_DOCUMENT":{"value":{"values":[],"limit":100,"start":0,"textSearch":""}},"REGION":{"value":[241515]}},"order":{"colName":"road_value","colSortDirection":0},"paging":{"start":0,"limit":20}}

html = requests.get(f'https://xn--d1aluo.xn--p1ai/roads', headers=headers, data=search_param)
html.encoding = 'utf-8'

print(html.text)

