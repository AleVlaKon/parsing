import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from timeit import Timer




def dict_func():
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
    return list_of_life_cookies[max(list_of_life_cookies.keys())]

def two_way_func():
    max_life = 0
    tag = 0
    with webdriver.Edge() as browser:
        browser.get('https://parsinger.ru/methods/5/index.html')
        elements = browser.find_elements(By.TAG_NAME, 'a')
        urls = [el.get_attribute('href') for el in elements]

        for url in urls:
            browser.get(url)
            tag_p = int(browser.find_element(By.TAG_NAME, 'p').text)
            cookie_expire = int(browser.get_cookie('foo2')['expiry'])
            if cookie_expire > max_life:
                max_life = cookie_expire
                tag = tag_p
    return tag

print(Timer(dict_func).timeit(number=1))
print(Timer(two_way_func).timeit(number=1))




