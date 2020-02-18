from .base_page import BasePage


# методы для "работы" c главной страницей сайта
class MainPage(BasePage):
    # заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
