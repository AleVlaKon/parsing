import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    
    for element in browser.find_elements(By.CLASS_NAME, 'parent'):
        if element.find_element(By.TAG_NAME, 'input').is_selected():
            count += int(element.find_element(By.TAG_NAME, 'textarea').text)
    time.sleep(15)
    print(count)