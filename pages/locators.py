from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
	BOOK_TITLE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
	BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")