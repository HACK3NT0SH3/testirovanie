from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get('https://ru.wikipedia.org/w/index.php?returnto=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F%D1%8F+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0&returntoquery=source%3Dspecialwelcomesurvey&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%85%D0%BE%D0%B4&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in')

login = browser.find_element(by=By.ID, value='wpName1')
login.send_keys('Hack3nt0sh3')

password = browser.find_element(by=By.ID, value='wpPassword1')
password.send_keys('hg275hbs85b^58')

button_login = browser.find_element(by=By.ID, value='wpLoginAttempt')
button_login.click()

sleep(3)

try:
    assert 'Здравствуйте, ‪Hack3nt0sh3‬! — Википедия' in browser.title

    print("Пользователь успешно авторизован")
except:
    print("Пользователь не авторизован")

browser.close()
