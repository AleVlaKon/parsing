import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    for div in browser.find_elements(By.CLASS_NAME, 'text'):
            for p in div.find_elements(By.TAG_NAME, 'p'):
                count += int(p.text)


print(count)