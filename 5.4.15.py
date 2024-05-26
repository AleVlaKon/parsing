import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    input_form = browser.find_elements(By.TAG_NAME, 'option')
    for checkbox in input_form:
        print(checkbox.text)
        value = int(checkbox.text)
        count += value

    browser.find_element(By.ID, "input_result").send_keys(count)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(15)