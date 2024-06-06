import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

key  =[]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'box_button')
    for element in elements:
        element.click()
        browser.find_element(By.ID, 'close_ad').click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, "ad_window")))
        WebDriverWait(browser, 10).until(lambda _:  element.text != "")
        key.append(element.text)
        # time.sleep(5)
    print(*key, sep='-')