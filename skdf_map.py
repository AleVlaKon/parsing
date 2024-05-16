import requests
import json
import csv

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}

search_param = json.dumps({"p_box":[4206559.671288764,7472660.224101382,4234612.060669424,7485845.611480576],"p_scale_factor":1,"p_zoom":14})
print(search_param)


session = requests.Session()
session.headers.update(headers)

response = session.get('https://xn--d1aluo.xn--p1ai/map')
json_resp = session.post('https://xn--d1aluo.xn--p1ai/api-pg/rpc/get_road_lr_geobox', data=search_param)

print(json_resp.text)



