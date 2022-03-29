import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        """Конструктор класса. Один из магических методов, выполняется при инициализации(создании) объекта"""
        self.browser = browser
        self.url = url

    def go_to_basket_page(self):
        """Функция находит на странице элемент корзины и используя метод click() окрывает данную страницу"""
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def go_to_login_page(self):
        """Находит на странице элемент кнопки для регистрации(авторизации)
                       и используя метод click() окрывает данную страницу
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def is_disappeared(self, how, what, timeout=4):
        """Проверяем что элемент исчезнет через определенный таймаут(по умолчанию он 4 сек.)"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        """ Вспомогательная функиця который находит элемент на страницы
        и если он отсутсвует то обрабатываем исключение
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяем что элемент не появиться на странице в течении определенного таймаута
        (если не передаем его по умолчанию он 4 сек.). Если появляется мы получаем False
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        """Открывает нужную страницу, используя метод get()"""
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        """Проверяем присутсвует ли на странице элемент кнопки для регистрации(авторизации)"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        """ Функция с помощью которой мы обрабатываем Alert сообщение в браузере"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
