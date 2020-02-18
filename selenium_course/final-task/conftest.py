import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавление опций:
# опция browser-name - позволяет выбрать браузер chrome или firefox, по умолчанию - chrome
# опция language - позволяет выбрать браузер язык, по умолчанию en
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Выберите браузер: chrome или firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Выберите язык: ru, en или другой")


# фикстура browser, scope function – фикстура запускается для каждого теста)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption("language")    

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name может принимать значения только chrome или firefox")
    
    print(f"\nЗапуск {browser_name} для теста...")
    
    yield browser
    print("\nЗакрытие браузера...")
    browser.quit()
