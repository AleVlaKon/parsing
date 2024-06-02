
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

    for page in browser.window_handles:
        browser.switch_to.window(page)
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()
        time.sleep(10)