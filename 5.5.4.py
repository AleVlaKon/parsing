import time
from selenium import webdriver
from selenium.webdriver.common.by import By



with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    
    for element in browser.find_elements(By.CLASS_NAME, 'text-field'):
        if not element.get_attribute('disabled'):
            element.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
    time.sleep(15)