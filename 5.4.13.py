import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'check')
    for checkbox in input_form:
        checkbox.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(15)