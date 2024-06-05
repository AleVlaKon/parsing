import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 
               'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 
               'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 
               'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 
               'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

locators = [(By.ID, ids) for ids in ids_to_find]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    for ids in ids_to_find:
        element = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.ID, ids)))
        element.click()
        print('!')
    
    print(browser.switch_to.alert.text)