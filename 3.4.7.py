import requests
import collections

response = requests.get(url='https://parsinger.ru/3.4/3/dialog.json')
response.encoding = 'utf-8'

# print(response.json())


count_messages = {}
    
def count_message(json_dict):
    if not json_dict['comments']:
        count_messages[json_dict['username']] = count_messages.get(json_dict['username'], 0) + 1
    else:
        count_messages[json_dict['username']] = count_messages.get(json_dict['username'], 0) + 1
        for i in json_dict['comments']:
            count_message(i)

        
count_message(response.json())
sorted_rooms = dict(sorted(count_messages.items(), key=lambda x: (-x[1], x[0])))

print(sorted_rooms)



