from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

sleep(5)

search = browser.find_element(by=By.ID, value='searchInput')
search.send_keys('СССР')

sleep(3)

btn = browser.find_element(by=By.ID, value='searchButton')
btn.click()
sleep(3)

try:
    assert 'Союз Советских Социалистических Республик — Википедия' in browser.title
    print("Статья найдена")
except:
    print("Статья не найдена")

browser.close()
