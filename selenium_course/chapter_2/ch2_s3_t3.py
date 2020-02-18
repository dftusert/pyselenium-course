import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Firefox()

try:
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    num1 = num1_element.text
    num2 = num2_element.text

    z = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(z)

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
