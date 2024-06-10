from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time

url = "https://parsinger.ru/selenium/5.10/3/index.html"


with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(1)
    moving_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "ui-draggable")]')
    target_elements = driver.find_elements(By.XPATH, '//div[@class="draganddrop_end"]')
    action = ActionChains(driver)

    for moving_element in moving_elements:
        moving_element_color = moving_element.value_of_css_property('background-color')
        for target_element in target_elements:
            print(moving_element_color, ' - ', target_element.value_of_css_property("border-top-color"))
            if moving_element_color == target_element.value_of_css_property("border-top-color"):
                action.drag_and_drop(moving_element, target_element).perform()

   
    time.sleep(10)