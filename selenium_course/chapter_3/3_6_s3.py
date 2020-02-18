import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('code', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, code):
    link = f"https://stepik.org/lesson/{code}/step/1"
    browser.get(link)

    textarea = WebDriverWait(browser, 25).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)

    submit_button = WebDriverWait(browser, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    submit_button.click()

    # Fix later because already works
    result_element = WebDriverWait(browser, 25).until(EC.element_to_be_clickable((By.TAG_NAME, "pre")))
    result_text = result_element.text.strip()

    assert result_text == "Correct!", f"Test fails at link, contains {code}, message '{result_text}' not equals with 'Correct!'"
