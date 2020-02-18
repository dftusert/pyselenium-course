import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ссылка на страницу для тестирования
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

# search_time - максимальное время поиска элемента
# wait_time - время ожидания - для просмотра правильности языка
# css_selector - селектор для кнопки, вынесен в переменную для удобной проверки assert при отсутствии элемента на странице
search_time = 15
wait_time = 30
css_selector = "button[type=\"submit\"].btn-add-to-basket"

# test_internet_shop_button_add_to_basket_available - проверка доступности кнопки добавления в корзину на сайте интернет-магазина
def test_internet_shop_button_add_to_basket_available(browser, language):
    browser.get(link)
    time.sleep(wait_time)
    
    # кнопка добавить в корзину
    try:
        add_to_basket_element = WebDriverWait(browser, search_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    except Exception as e:
        # если не удалось найти - assert
        assert 0, f"Поиск кнопки добавить в корзину превысил время ожидания поиска ({search_time}s) и завершился с ошибкой {str(e)}"
