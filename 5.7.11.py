import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    actions = ActionChains(browser)
    list_of_elements = []
    count = 0
    while True:
        elements = browser.find_elements(By.TAG_NAME, 'input')
        for element in elements:
            if element not in list_of_elements:
                element.send_keys(Keys.DOWN)
                browser.execute_script("return arguments[0].scrollIntoView(true);", element)
                element.click()
                time.sleep(1)
                list_of_elements.append(element)
                # count += int(element.text)






