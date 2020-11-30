import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x = browser.find_element_by_css_selector("#input_value")
    x_value = x.text
    y = calc(x_value)

    answer = browser.find_element_by_css_selector(".form-control")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radiobttn = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobttn)
    radiobttn.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()