import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    formula = browser.find_element(By.ID, 'text_box').text
    formula_result = eval(formula)
    for_res = 74604646177
    input_form = browser.find_elements(By.TAG_NAME, 'option')

    for checkbox in input_form:
        if int(checkbox.text) == formula_result:
            checkbox.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(15)