import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
    print(element.text)
