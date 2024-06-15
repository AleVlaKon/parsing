from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/draganddrop/2/index.html"


with webdriver.Chrome() as driver:
    driver.get(url)
    moving_element = driver.find_element(By.ID, 'draggable')
    target_elements = driver.find_elements(By.XPATH, '//div[@class="box"]')
    action = ActionChains(driver)

    for element in target_elements:
        action.drag_and_drop(moving_element, element).perform()


    time.sleep(10)