from selenium import webdriver
import time


# Проверка одной страницы регистрации
def check_reg(link):
    print("Проверяем страницу: ", link)
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name("input[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name("input[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name("input[placeholder='Input your email']")
    input3.send_keys("123@example.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(3)
    browser.quit()


# Готовим url'ы
path = "http://suninjuly.github.io/"
pages = ["registration1.html", "registration2.html"]

# Проходим по списку страниц, запуская проверку каждой
for p in pages:
    check_reg(path + p)
# Вторая страница должна упасть с ошибкой