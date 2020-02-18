from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_login_page()
        email_field = self.get_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD, "presense")
        password_field = self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, "presense")
        password_confirm_field = self.get_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, "presense")
        register_button = self.get_element(*LoginPageLocators.REGISTRATION_BUTTON, "presense")

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        register_button.click()

        # если произошла ошибка регистрации - пробуем войти
        # т.к. логин и пароль могут подойти к уже существующему пользователю
        if self.is_element_present(*LoginPageLocators.REGISTRATION_ERROR_BOX_INFO):
            email_field = self.get_element(*LoginPageLocators.LOGIN_EMAIL_FIELD, "presense")
            password_field = self.get_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD, "presense")
            login_button = self.get_element(*LoginPageLocators.LOGIN_BUTTON, "presense")

            email_field.send_keys(email)
            password_field.send_keys(password)
            login_button.click()

            assert not self.is_element_present(*LoginPageLocators.LOGIN_ERROR_BOX_INFO), "Введены неверные данные " + \
                f"для входа: email = '{email}', password = '{password}', измените email и password"

            assert not self.is_element_present(*BasePageLocators.LOGIN_LINK_GUEST), "Не удалось войти, " + \
                                                                                    f"проверьте на ошибки: email = " + \
                                                                                    f"'{email}', password = '{password}'" + \
                                                                                    "и измените email и password"

    # выход пользователя
    def logout_user(self):
        self.should_be_authorized_user()
        logout_link = self.get_element(*BasePageLocators.LOGOUT_LINK_USER, "presense")
        logout_link.click()

    # проверка того что есть формы регистрации и логина, а также то что подстрока "login" есть в текущем url браузера
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка, что подстрока "login" есть в текущем url браузера
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Подстрока 'login' не найдена в url браузера," + \
                                                    f"который равен {self.browser.current_url}"

    # проверка наличия формы входа (не проверяется наличие в ней полей для ввода)
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа на странице" + \
                    f"{self.browser.current_url} не найдена по локатору {str(*LoginPageLocators.LOGIN_FORM)}"

    # проверка наличия формы регистрации (не проверяется наличие в ней полей для ввода)
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Форма регистрации на странице" + \
                    f"{self.browser.current_url} не найдена по локатору {str(*LoginPageLocators.REGISTRATION_FORM)}"
