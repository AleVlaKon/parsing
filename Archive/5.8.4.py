import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'pin')
    test_button = browser.find_element(By.XPATH, '//*[@id="check"]')
    for element in elements:
        element_text = element.text
        test_button.click()
        prompt = browser.switch_to.alert
        prompt.send_keys(element_text)
        prompt.accept()
        if browser.find_element(By.ID, 'result').text != 'Неверный пин-код':
            print(browser.find_element(By.ID, 'result').text)