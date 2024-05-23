import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    all_squares = browser.find_elements(By.CLASS_NAME, 'timer_button')
    for square in all_squares:
        hold_time = float(square.get_attribute('value')) + 1
        action = ActionChains(browser)

        action.click_and_hold(square).pause(hold_time).release(square).perform()


    print(browser.switch_to.alert.text)
    time.sleep(15)

