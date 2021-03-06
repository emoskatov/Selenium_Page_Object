from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-title")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")
