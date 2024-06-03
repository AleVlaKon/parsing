import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    test_field = browser.find_element(By.ID, 'guessInput')
    test_button = browser.find_element(By.ID, 'checkBtn')

    for i in range(1, 10):
        frame = browser.find_element(By.ID, f'iframe{i}')
        browser.switch_to.frame(frame)
        browser.find_element(By.TAG_NAME, 'button').click()
        pin = browser.find_element(By.TAG_NAME, 'p').text
        browser.switch_to.default_content()
        test_field.send_keys(pin)
        test_button.click()
        try:
            alert = browser.switch_to.alert
            print(alert.text)
            alert.accept()
            test_field.clear()
        except:
            test_field.clear()
        
    

    time.sleep(15)