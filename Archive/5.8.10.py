import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    left_right_x = 16
    top_bottom_y = 200
    for i in product(window_size_x, window_size_y):
        browser.set_window_size(left_right_x + i[0], top_bottom_y + i[1])
        if browser.find_element(By.ID, 'result').text:
            value = browser.get_window_size()
            value['width'] -= left_right_x
            value['height'] -= top_bottom_y
            print(value)
            time.sleep(14)
            break
            
    

