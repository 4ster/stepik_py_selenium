from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/registration1.html')

input1 = browser.find_element(By.XPATH, '//input[@placeholder="Введите имя"]')
input1.send_keys('A')
input2 = browser.find_element(By.XPATH, '//input[@placeholder="Введите фамилию"]')
input2.send_keys('С')
input3 = browser.find_element(By.CLASS_NAME, 'third')
input3.send_keys('abcde@gmail.com')

browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
time.sleep(1)
textElt = browser.find_element(By.TAG_NAME, 'h1').text

assert 'Поздравляем! Вы успешно зарегистировались!' == textElt
