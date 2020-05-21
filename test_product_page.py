from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), # этот тест падает. отметили его как xfail
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	link = link
	page = ProductPage(browser, link)
	page.open() 
	book_title = page.get_book_title() # получить название книги
	book_price = page.get_book_price() # получить цену книги
	page.add_to_basket() # добавить в корзину
	page.solve_quiz_and_get_code() # пройти задание в алерте
	time.sleep(2)
	book_title_in_basket = page.book_title_in_basket() # получить название книги, которая добавлена в корзину
	book_price_in_basket = page.book_price_in_basket() # получить цену книги, которая добавлена в корзину

	# проверить, что название книги, которую добавляли в корзину, совпадает с названием книги, которая добавлена в корзину
	assert book_title == book_title_in_basket, "No necessary book is added to the basket"
	# проверить, что цена книги, которую добавляли в корзину, совпадает с ценой книги, которая добавлена в корзину
	assert book_price == book_price_in_basket, "prices don't match"

# Добавляем товар в корзину и проверяем, что нет сообщения об успешном добавлении товара (это падающий тест - сообщение должно быть)
#@pytest.mark.xfail
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open() 
	page.add_to_basket() # добавить в корзину
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()

# НЕ добавляем товар в корзину и проверяем, что нет сообщения об успешном добавлении товара (это работающий тест)
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open() 
	page.should_not_be_success_message()

# Проверяем, что сообщение об успешном добавлении товара в корзину исзечает (это падающий тест - сообщение не должно исчезать)
#@pytest.mark.xfail
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open() 
	page.add_to_basket() # добавить в корзину
	# Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page.message_is_disappeared()

# Гость должен видеть ссылку на страницу логина
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

# Гость может перейти на страницу логина
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()


