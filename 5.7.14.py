import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
    actions = ActionChains(browser)
    list_of_elements = []
    scroll_element = browser.find_element(By.ID, 'main_container')
    while True:
        elements = browser.find_elements(By.TAG_NAME, 'input')
        for element in elements:
            if element not in list_of_elements:
                list_of_elements.append(element)
                value = int(element.get_attribute('value'))
                if value % 2 == 0:
                    element.click()
        actions.move_to_element(scroll_element).scroll_by_amount(0, 10000).perform()
        time.sleep(1)
        actions.move_to_element(scroll_element).scroll_by_amount(0, 10000).perform()
        print(len(list_of_elements))
        if len(list_of_elements) == 1000:
            break

    time.sleep(15)