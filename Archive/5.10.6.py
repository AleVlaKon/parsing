from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/draganddrop/1/index.html"


with webdriver.Chrome() as driver:
    driver.get(url)
    moving_element = driver.find_element(By.ID, 'draggable')
    target_element = driver.find_element(By.ID, 'field2')
    text_result = driver.find_element(By.XPATH, '//div[@id="result"]')
    ActionChains(driver).drag_and_drop(moving_element, target_element).perform()
    print(text_result.text)
    time.sleep(10)