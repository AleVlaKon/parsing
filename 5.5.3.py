import time
from selenium import webdriver
from selenium.webdriver.common.by import By



with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    for element in browser.find_elements(By.CLASS_NAME, 'text-field'):
        element.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)