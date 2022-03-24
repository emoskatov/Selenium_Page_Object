from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(f"{product_name=},\n{message=}")
        assert message == product_name, f"{product_name} is not {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(f"{product_price=},\n{basket_price=}")
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_after_success_message(self): # Доработать
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

