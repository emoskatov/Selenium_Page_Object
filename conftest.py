import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose Language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_argument(f'lang={browser_lang}')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        service = ChromeService(executable_path="chromedriver")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "yandex":
        print("\nstart yandex browser for test..")
        service = ChromeService(executable_path="yandexdriver")
        browser = webdriver.Chrome(service=service, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or yandex")
    yield browser
    print("\nquit browser..")
    browser.quit()
