import time
from selenium import webdriver
from selenium.webdriver.common.by import By


count = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    all_buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for button in all_buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    print(browser.switch_to.alert.text)
    time.sleep(15)

print(count)
