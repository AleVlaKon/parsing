import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys



with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
    first_element = browser.find_element(By.TAG_NAME, 'input')
    for i in range(1000):
        first_element.send_keys(Keys.DOWN)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for i in elements:
        if int(i.get_attribute('value')) % 2 == 0:
            i.click()




    time.sleep(15)