import requests
import json
import csv

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}

search_param = json.dumps({"textSearch":"","filters":{"OWNER":{"value":{"values":[5567044],"start":0,"limit":100,"textSearch":""}},"BASE_DOCUMENT":{"value":{"values":[],"limit":100,"start":0,"textSearch":""}},"REGION":{"value":[241515]}},"order":{"colName":"road_value","colSortDirection":0},"paging":{"start":0,"limit":300}})

json_resp = requests.post('https://xn--d1aluo.xn--p1ai/api/v1/portal/roads2/list', headers=headers, data=search_param)


with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(json_resp.json(), file, indent=4, ensure_ascii=False)



dor_json = json_resp.json()['data']

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Имя', 'Протяженность'])
    for i in dor_json:
        row_i = (i['name'], i['length'])
        writer.writerow(row_i)