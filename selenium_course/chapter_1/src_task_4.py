import time
from selenium.webdriver.common.by import By
from selenium import webdriver

print("begin")
browser = webdriver.Firefox()
try:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("y")

    button = browser.find_element(By.XPATH, "//*[text()=\"Submit\"]")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    print("end")
