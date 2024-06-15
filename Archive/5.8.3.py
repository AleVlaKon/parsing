import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'buttons')
    enter_field = browser.find_element(By.XPATH, '//*[@id="input"]')
    test_button = browser.find_element(By.XPATH, '//*[@id="check"]')
    for element in elements:
        element.click()
        pin = browser._switch_to.alert.text
        browser._switch_to.alert.accept()
        enter_field.send_keys(pin)
        test_button.click()
        if browser.find_element(By.ID, 'result').text != 'Неверный пин-код':
            print(browser.find_element(By.ID, 'result').text)