import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Firefox()

try:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "[for=\"robotCheckbox\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, "[for=\"robotsRule\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
