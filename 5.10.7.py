from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/draganddrop/3/index.html"


with webdriver.Firefox() as driver:
    driver.get(url)
    moving_element = driver.find_element(By.ID, 'block1')
    target_elements = driver.find_elements(By.CLASS_NAME, 'controlPoint')
    action = ActionChains(driver)

    for i in range(5):
        action.drag_and_drop_by_offset(moving_element, 50, 0).perform()


    time.sleep(10)