#from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest
import time

# @pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage():
	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = BasePage(browser, link) # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
		page.open() # открываем страницу
		page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = BasePage(browser, link)
		page.open()
		page.should_be_login_link()

@pytest.mark.skip
def test_guest_shoul_open_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_url()

@pytest.mark.skip
def test_guest_should_see_login_form(browser):
	link = "http://selenium1py.pythonanywhere.com/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_form()

@pytest.mark.skip
def test_guest_should_see_register_form(browser):
	link = "http://selenium1py.pythonanywhere.com/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_register_form()

# перейти в корзину, проверить, что она пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasePage(browser, link)
	page.open()
	page.go_to_basket_page()
	# Ожидаем, что в корзине нет товаров
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.open()
	basket_page.should_not_be_items_in_basket() 
	# Ожидаем, что есть текст о том что корзина пуста
	basket_page.message_basket_is_empty()



