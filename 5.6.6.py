import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

list_of_life_cookies = {}

with webdriver.Edge() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    elements = browser.find_elements(By.TAG_NAME, 'a')
    urls = [el.get_attribute('href') for el in elements]

    for url in urls:
        browser.get(url)
        tag_p = int(browser.find_element(By.TAG_NAME, 'p').text)
        cookie_expire = int(browser.get_cookie('foo2')['expiry'])
        list_of_life_cookies[cookie_expire] = tag_p

print(list_of_life_cookies[max(list_of_life_cookies.keys())])


