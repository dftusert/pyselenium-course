from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators


# страница товаров
class ProductPage(BasePage):
    # добавление товара со страницы добавления товара и возврат информации о добавленом товаре
    def add_to_basket(self):
        book_name_on_product_page = self.get_element(*ProductPageLocators.BOOK_NAME, "presense")
        book_price_on_product_page = self.get_element(*ProductPageLocators.BOOK_PRICE, "presense")
        wanted_product = [book_name_on_product_page.text, book_price_on_product_page.text]

        add_to_basket_button = self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON, "clickable")
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        return wanted_product

    # проверка цены и названия добавленного товара с находящимися в корзине
    def check_adding_product_to_basket(self):
        wanted_product = self.add_to_basket()
        self.go_to_basket_page()

        basket_page = BasketPage(self.browser, self.browser.current_url)
        products_in_basket = basket_page.get_basket_products()

        wanted_item_founded = False
        for i in range(len(products_in_basket)):
            if products_in_basket[i][0] == wanted_product[0] and products_in_basket[i][1] == wanted_product[1]:
                wanted_item_founded = True

        assert wanted_item_founded, f"Товар {wanted_product[0]} со стоимостью {wanted_product[1]} не найден в " + \
                                    f"{str(products_in_basket)}"

    # проверка информации о добавленном товаре в сообщениях с реальной информацией о товаре
    def check_messages_on_product_page(self):
        wanted_product = self.add_to_basket()

        message_elements = self.get_elements(*ProductPageLocators.MESSAGES_TEXT_BOLD)

        book_name_is_present_in_messages = False
        book_price_is_present_in_messages = False

        for message_element in message_elements:
            if message_element.text == wanted_product[0]:
                book_name_is_present_in_messages = True
            if message_element.text == wanted_product[1]:
                book_price_is_present_in_messages = True

        assert book_name_is_present_in_messages, f"На странице '{self.browser.current_url}' не удалось найти " + \
                                                 f"точное соответствие названия книги '{wanted_product[0]}' и " + \
                                                 "названия книги в сообщениях"

        assert book_price_is_present_in_messages, f"На странице '{self.browser.current_url}' не удалось найти " + \
                                                  f"точное соответствие цены книги '{wanted_product[1]}' и " +\
                                                  "цены книги в сообщениях"

    # переход на страницу с корзиной после добавления товара на странице с товаром
    def go_to_basket_after_adding_to_basket(self):
        go_to_basket_button = self.get_element(*ProductPageLocators.GO_TO_BASKET_LINK_AFTER_ADDING_TO_BASKET, "clickable")
        go_to_basket_button.click()

#######################################################################################################################

    # "После добавления в корзину продукта присутствуют сообщения об успехе"
    def check_no_success_messages_after_add_to_basket(self):
        add_to_basket_button = self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON, "clickable")
        add_to_basket_button.click()
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_SUCCESS), \
            "После добавления в корзину продукта присутствуют сообщения об успехе"

    # "Присутствуют сообщения об успехе"
    def check_no_success_messages(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_SUCCESS), \
            "Присутствуют сообщения об успехе"

    # "После добавления в корзину продукта сообщения об успехе остаются"
    def check_no_success_messages_after_add_to_basket_no_diss(self):
        add_to_basket_button = self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON, "clickable")
        add_to_basket_button.click()
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_SUCCESS), \
            "После добавления в корзину продукта сообщения об успехе остаются"
