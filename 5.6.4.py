import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


count = 0
with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie)
        if cookie['name'].startswith('secret_cookie_'):
            count += int(cookie['value'])

print(count)