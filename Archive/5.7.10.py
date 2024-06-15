import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


count = 0

with webdriver.Edge() as browser:
    browser.get('http://parsinger.ru/scroll/2/index.html')
    all_squares = browser.find_elements(By.CLASS_NAME, 'item')
    for square in all_squares:
        actions = ActionChains(browser)
        checkbox = square.find_element(By.CLASS_NAME, 'checkbox_class')
        actions.move_to_element(checkbox).click(checkbox).perform()
        
        if x := square.find_element(By.TAG_NAME, 'span').text:
            count += int(x)
        

    print(count)
    time.sleep(15)


