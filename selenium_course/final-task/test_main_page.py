import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # тестирование перехода на страницу регистрации и входа
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        
    # тестирование корректности ссылки на страницу регистрации и входа
    @pytest.mark.xfail(reason="Потому что на используемой в тесте странице локатор для ссылки отличается от остальных")
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# тестирование на соответствие странице регистрации и входа
def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


# проверка на пустую корзину гостя при переходе в нее из главной страницы (до этого гость не заполнял корзину)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()
