import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        element = browser.find_element(By.ID, 'result').text
        if element.isdigit():
            print(element)
            break
        else:
            browser.refresh()
