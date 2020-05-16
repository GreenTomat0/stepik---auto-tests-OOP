from .pages.product_page import ProductPage
import pytest
import time

def test_guest_can_add_product_to_basket(browser):
	# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
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
	assert book_title in book_title_in_basket, "No necessary book is added to the basket"
	# проверить, что цена книги, которую добавляли в корзину, совпадает с ценой книги, которая добавлена в корзину
	assert book_price in book_price_in_basket, "prices don't match"