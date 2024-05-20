import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/test/test.html')
    for element in browser.find_elements(By.XPATH, '/html/body/div/div'):
        color_hex = element.find_element(By.TAG_NAME, 'span').text.strip()

        # select_element = element.find_element(By.TAG_NAME, 'select')
        # select = Select(select_element)
        # select.select_by_value(color_hex)

        element.find_element(By.CSS_SELECTOR, f'option[value="{color_hex}"]').click()
        element.find_element(By.CSS_SELECTOR, f'button[data-hex="{color_hex}"]').click()
        element.find_element(By.CSS_SELECTOR, 'input:nth-child(4)').click()
        element.find_element(By.CSS_SELECTOR, 'input:nth-child(5)').send_keys(color_hex)        
        element.find_element(By.XPATH, ".//button[text()='Проверить']").click()

    browser.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
        

    time.sleep(60)