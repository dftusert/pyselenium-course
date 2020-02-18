from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    required_field = browser.find_element(By.CSS_SELECTOR, "input[required].first")
    required_field.send_keys(required_field.get_attribute("class"))

    required_field = browser.find_element_by_css_selector("input[required].second")
    required_field.send_keys(required_field.get_attribute("class"))

    required_field = browser.find_element(By.CSS_SELECTOR, "input[required].third")
    required_field.send_keys(required_field.get_attribute("class"))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # time.sleep(1)
    welcome_text_elt = WebDriverWait(browser, 15).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h1")))
    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
