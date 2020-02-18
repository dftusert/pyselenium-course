from selenium.webdriver.common.by import By


# локаторы страницы с товарами
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"].btn-add-to-basket")
    GO_TO_BASKET_LINK_AFTER_ADDING_TO_BASKET = (By.CSS_SELECTOR, "#messages a[href*=\"basket\"]")

    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner .row h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner .row .price_color")

    MESSAGES_TEXT_BOLD = (By.CSS_SELECTOR, "#messages .alertinner strong")
    MESSAGES_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")


# локаторы для страницы регистрации и входа
class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")
    REGISTRATION_ERROR_BOX_INFO = (By.CSS_SELECTOR, "#register_form .alert.alert-danger")

    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=\"login_submit\"]")
    LOGIN_ERROR_BOX_INFO = (By.CSS_SELECTOR, "#login_form .alert.alert-danger")


# основные локаторы (для всех страниц)
class BasePageLocators:
    LOGIN_LINK_GUEST = (By.CSS_SELECTOR, "#login_link")
    LOGOUT_LINK_USER = (By.CSS_SELECTOR, "#logout_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".header.container-fluid .basket-mini .btn-group a.btn-default")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# локаторы корзины
class BasketPageLocators:
    BOOK_NAMES = (By.CSS_SELECTOR, ".basket-items .row h3 a")
    BOOK_PRICES = (By.CSS_SELECTOR, ".col-sm-1 p.price_color")
    BASKET_STATUS = (By.CSS_SELECTOR, "content_inner p")
