import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()

try:
    browser.get(link)
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(calc(x))

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

    print(browser.switch_to.alert.text.split(': ')[-1])
finally:
    # time.sleep(30)
    browser.quit()
