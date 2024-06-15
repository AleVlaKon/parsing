import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    actions = ActionChains(browser)
    list_of_elements = []
    count = 0
    for i in range(1, 6):
        scroll_element = browser.find_element(By.XPATH, f'/html/body/div/div[{i}]/div[1]/div')
        while True:
            elements = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]').find_elements(By.TAG_NAME, 'span')
            for element in elements:
                if element not in list_of_elements:
                    list_of_elements.append(element)
                    count += int(element.text)
            if list_of_elements[-1].get_attribute("class") == 'last-of-list':
                break
            actions.move_to_element(scroll_element).scroll_by_amount(0, 5000).perform()
print(count)

