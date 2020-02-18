import math
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


# основные функции при работе со страницами
class BasePage:
    # конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser     # "браузер"
        self.url = url             # ссылка страницы
        self.timeout = timeout     # таймаут для явного ожидания

    # открытие страницы в браузере
    def open(self):
        self.browser.get(self.url)

    # возвращает найденный элемент или выполняет assert
    def get_element(self, selector_type, selector, ec_type):
        try:
            if ec_type == "clickable":
                element = WebDriverWait(self.browser, self.timeout)\
                                              .until(EC.element_to_be_clickable((selector_type, selector)))
            elif ec_type == "presense":
                element = WebDriverWait(self.browser, self.timeout)\
                                              .until(EC.presence_of_element_located((selector_type, selector)))
            else:
                raise Exception('Неверно задан аргумент ec_type')
            return element
        except Exception as e:
            assert 0, f"Невозможно найти элемент по локатору '({selector_type}, {selector})' на странице " + \
                      f"{self.browser.current_url} используя тип ec {ec_type}, ошибка {str(e)}"

    # возвращает массив элементов
    def get_elements(self, selector_type, selector):
        try:
            elements = self.browser.find_elements(selector_type, selector)
            return elements
        except Exception as e:
            assert 0, f"Невозможно найти элементы по локатору '({selector_type}, {selector})' на странице " + \
                      f"{self.browser.current_url}, ошибка {str(e)}"

    # проверка существования ссылки для перехода на страницу входа или регистрации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK_GUEST), "Невозможно найти ссылку на страницу входа"

    # переход на страницу входа и регистрации
    def go_to_login_page(self):
        if self.is_element_present(*BasePageLocators.USER_ICON):
            logout_link = self.get_element(*BasePageLocators.LOGOUT_LINK_USER, "presense")
            logout_link.click()

        link = self.get_element(*BasePageLocators.LOGIN_LINK_GUEST, "presense")
        link.click()

    # переход на страницу с корзиной
    def go_to_basket_page(self):
        go_to_basket_button = self.get_element(*BasePageLocators.BASKET_LINK, "clickable")
        go_to_basket_button.click()
#######################################################################################################################

    # элемент находится на странице
    def is_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    # элемент не находится на странице
    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # элемент находится на странице, но должен исчезнуть
    def is_disappeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Иконка пользователя не представлена," \
                                                                     " возможно неавторизованный пользователь"

    # функция для 4_3_step_2
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")