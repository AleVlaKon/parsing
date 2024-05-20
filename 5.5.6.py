import time
from selenium import webdriver
from selenium.webdriver.common.by import By



with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    
    for element in browser.find_elements(By.CLASS_NAME, 'parent'):
        grey, blue = element.find_elements(By.TAG_NAME, 'textarea')
        blue.send_keys(grey.text)
        grey.clear()
        element.find_element(By.TAG_NAME, 'button').click()

    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)
    time.sleep(15)