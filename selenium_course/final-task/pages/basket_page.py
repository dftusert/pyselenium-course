from .base_page import BasePage
from .locators import BasketPageLocators


# страница корзины
class BasketPage(BasePage):
    # получение списка товаров и их цен из корзины
    def get_basket_products(self):
        book_names = self.get_elements(*BasketPageLocators.BOOK_NAMES)
        book_prices = self.get_elements(*BasketPageLocators.BOOK_PRICES)

        basket_products = []
        for i in range(len(book_names)):
            basket_products.append([book_names[i].text, book_prices[i].text])
        return basket_products

    # проверка на пустую корзину
    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_STATUS), "Корзина не пуста"
