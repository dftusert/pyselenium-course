import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()

try:
    browser.get(link)

    firstname_element = browser.find_element(By.CSS_SELECTOR, "[name=\"firstname\"]")
    firstname_element.send_keys(firstname_element.get_attribute("placeholder"))

    lastname_element = browser.find_element(By.CSS_SELECTOR, "[name=\"lastname\"]")
    lastname_element.send_keys(lastname_element.get_attribute("placeholder"))

    email_element = browser.find_element(By.CSS_SELECTOR, "[name=\"email\"]")
    email_element.send_keys(email_element.get_attribute("placeholder"))

    file_element = browser.find_element(By.CSS_SELECTOR, "[type=\"file\"]")
    
    current_wd = os.path.abspath(os.path.dirname(__file__))
    current_file = os.path.join(current_wd, "stepic.txt")
    
    file_element.send_keys(current_file)

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
