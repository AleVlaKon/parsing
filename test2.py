import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


count = 0
with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    print(browser.execute_script("return document.documentURI;"))

    time.sleep(15)