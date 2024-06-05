import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(browser, 60).until(EC.title_is("345FDG3245SFD"))
    print(browser.find_element(By.ID, 'result').text)
