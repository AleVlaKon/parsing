import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    element = WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.ID, 'qQm9y1rk')))
    print(element)
    element[0].click()
    print(browser.switch_to.alert.text)