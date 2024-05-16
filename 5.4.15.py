import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'check')
    for checkbox in input_form:
        value = int(checkbox.text)
        count += value

    browser.find_element(By.NAME, "some_textbox_name").send_keys("Hello, World!")

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(15)