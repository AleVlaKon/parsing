import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    left_right = 16
    top_bottom = 133 + 555 - 488
    browser.set_window_size(555 + left_right, 555 + top_bottom)
        
    

    time.sleep(15)