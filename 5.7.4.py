import time
from selenium import webdriver
from selenium.webdriver.common.by import By


count = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    all_buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    for button in all_buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        count += int(browser.find_element(By.ID, 'result').text)
    time.sleep(15)

print(count)
