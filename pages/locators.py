from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

#class MainPageLocators():
	# LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
	CONFIRM_REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BTN = (By.CSS_SELECTOR, ".register_form button")

class ProductPageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
	BOOK_TITLE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
	BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")

class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")