import requests
import json
import csv

headers = {'Host': 'xn--d1aluo.xn--p1ai',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/json',
'Access-Control-Allow-Origin': '*',
'Content-Profile': 'gis_api_public',
'Content-Length': '112',
'Origin': 'https://xn--d1aluo.xn--p1ai',
'Connection': 'keep-alive',
'Referer': 'https://xn--d1aluo.xn--p1ai/map',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'TE': 'trailers',}


url = 'https://xn--d1aluo.xn--p1ai/api-pg/rpc/get_road_lr_geobox'
search_param = json.dumps({"p_box":[7633214.094586074,8320471.824715334,9428567.014948294,8993729.169851167],"p_scale_factor":1,"p_zoom":14})

json_resp = requests.post(url, data=search_param, headers=headers)

with open('res3.json', 'w', encoding='utf-8') as file:
    json.dump(json_resp.json(), file, indent=4, ensure_ascii=False)




