from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
	# открыть страницу логина
	def go_to_login_page(self):
		link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
		link.click()

	# метод, который будет проверять наличие ссылки залогиниться
	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"
