import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


count = 0

with webdriver.Edge() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    all_squares = browser.find_elements(By.TAG_NAME, 'span')
    print(len(all_squares))
