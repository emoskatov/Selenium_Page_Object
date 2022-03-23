import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose Language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome("chromedriver", options=options)
    elif browser_name == "yandex":
        print("\nstart yandex browser for test..")
        browser = webdriver.Chrome('yandexdriver.exe',
                                   options=options)  # Необходимо доработать этот момент, не передает параметр в браузер
    else:
        raise pytest.UsageError("--browser_name should be chrome or yandex")
    yield browser
    print("\nquit browser..")
    browser.quit()
