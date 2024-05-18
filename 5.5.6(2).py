import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/test/test.html')
    for element in browser.find_elements(By.XPATH, '/html/body/div/div'):
        color_hex = element.find_element(By.TAG_NAME, 'span').text
        element.find_element(By.CSS_SELECTOR, f'option[value="{color_hex}"]').click()
        element.find_element(By.CSS_SELECTOR, f'button[data-hex="{color_hex}"]').click()
        element.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        element.find_element(By.CSS_SELECTOR, f'input[type="text"]').send_keys(color_hex)
        element.find_element(By.CSS_SELECTOR, 'button').click()
    element.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(15)
