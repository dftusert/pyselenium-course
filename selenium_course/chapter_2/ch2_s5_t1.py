import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Firefox()

try:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(int(x))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "[for=\"robotCheckbox\"]")
    robot_checkbox.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, "[for=\"robotsRule\"]")
    robots_rule.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
