import requests

# Отправляем GET-запрос
r = requests.get('https://api.github.com/events')

# Получаем текст ответа
print("Содержимое ответа:")
print(r.text)

print("Текущая кодировка:", r.encoding)