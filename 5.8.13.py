import time
from selenium import webdriver
from selenium.webdriver.common.by import By

count = []

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/1/1.html')
    for site in sites[1:]:
        browser.execute_script(f'window.open("{site}");')
    
    for page in browser.window_handles:
        browser.switch_to.window(page)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        code = float(browser.find_element(By.ID, 'result').text)
        count.append(code ** 0.5)

    print(round(sum(count), 9))