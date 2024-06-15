import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for button in buttons:
        button.click()
    
    for page in browser.window_handles[1:]:
        browser.switch_to.window(page)
        count += int(browser.title)
print(count)


