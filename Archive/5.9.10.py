from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 
               'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 
               'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 
               'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 
               'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    elements = [browser.find_element(By.ID, ids) for ids in ids_to_find]
    time.sleep(1)
    zero_el = browser.find_element(By.CLASS_NAME, 'box')
    print(zero_el.__class__)

    for element in elements:
        element = WebDriverWait(browser, 60).until(EC.visibility_of(element))
        print(element.__class__)
        element.click()
        print('!')
    
    print(browser.switch_to.alert.text)