from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/5.10/2/index.html"


with webdriver.Chrome() as driver:
    driver.get(url)
    moving_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "draggable-handle")]')
    target_element = driver.find_element(By.CLASS_NAME, 'draganddrop_end')
    action = ActionChains(driver)

    for element in moving_elements:
        action.drag_and_drop(element, target_element).perform()


    time.sleep(10)