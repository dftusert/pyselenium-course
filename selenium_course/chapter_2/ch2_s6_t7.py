import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()

try:
    browser.get(link)

    # browser.execute_script("document.getElementByTagName('button')[0].classList.remove('trollface');")
    newtab_button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    newtab_button.click()

    browser.switch_to.window(browser.window_handles[1])


    # bad wait, todo - change it. may be not needed.
    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)


    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(calc(x))

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

    # print(browser.switch_to.alert.text.split(': ')[-1])
finally:
    time.sleep(10)
    browser.quit()
