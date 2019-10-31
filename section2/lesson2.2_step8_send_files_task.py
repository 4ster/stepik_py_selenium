from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 


link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# print(file_path)
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
# element.send_keys(file_path)

with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input[placeholder='Enter first name']")
    input1.send_keys("FirstName")
    input2 = browser.find_element_by_tag_name("input[placeholder='Enter last name']")
    input2.send_keys("LastName")
    input3 = browser.find_element_by_tag_name("input[placeholder='Enter email']")
    input3.send_keys("email@example.org")

    file_upload = browser.find_element(By.ID, "file")
    file_upload.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(15)