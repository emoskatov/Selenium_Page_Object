from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        if "login" in url:
            return True
        else:
            return False

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User not authorized"

    def register_new_user(self, email, password):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
