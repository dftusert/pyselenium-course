import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# добавление опций:
# опция browser_name - позволяет выбрать браузер chrome или firefox, по умолчанию - chrome
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language: ru, en or other")

# фикстура browser, scope function – фикстура запускается для каждого теста)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption("language")    

    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    print(f"\nStarting {browser_name} browser for test...")
    
    yield browser
    print("\nQuiting browser...")
    browser.quit()

# фикстура language, scope class – фикстура запускается один раз для всех тестов, запущенных в данной сессии
@pytest.fixture(scope="session")
def language(request):
    language = request.config.getoption("language")
    print(f"\nStarting language '{language}' for test...")
    
    yield language
    print(f"Stopping using language '{language}' for test...")
