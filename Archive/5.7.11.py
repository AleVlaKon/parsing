import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(1)
    actions = ActionChains(browser)
    div = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div')
    list_of_elements = []
    count = 0

    while True:
        elements = browser.find_elements(By.TAG_NAME, 'span')
        for element in elements:
            if element not in list_of_elements:
                if element.text:
                    count += int(element.text)
                list_of_elements.append(element)
        print(list_of_elements)
        actions.move_to_element(div).scroll_by_amount(0, 500).perform()
        if list_of_elements[-1].get_attribute('class') == 'last-of-list':
            break
    print(count)








