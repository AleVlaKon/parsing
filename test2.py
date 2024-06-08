from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://vk.com')
    print(browser.title)
    browser.get('https://ya.ru')
    browser.back()
    assert browser.title == 'ВКонтакте | Добро пожаловать'

    


    