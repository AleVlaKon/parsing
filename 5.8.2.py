import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys



with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'buttons')
    for element in elements:
        element.click()
        browser._switch_to.alert.accept()
        if browser.find_element(By.ID, 'result').text:
            print(browser.find_element(By.ID, 'result').text)