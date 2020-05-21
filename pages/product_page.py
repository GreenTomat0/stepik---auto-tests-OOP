from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver


class ProductPage(BasePage):
    # добавить товар в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    # получить название товара (книги)
    def get_book_title(self):
        book_title_tag = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title = book_title_tag.text    
        return book_title

    # получить цену товара (книги)
    def get_book_price(self):
        book_price_tag = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price_tag.text    
        return book_price

    # товар (книга) с нужным названием добавлена в корзину
    def book_title_in_basket(self):
        book_title_in_basket_tag = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_BASKET)
        book_title_in_basket = book_title_in_basket_tag.text    
        return book_title_in_basket

    # товар (книга) с нужной ценой добавлен в корзину
    def book_price_in_basket(self):
        book_price_in_basket_tag = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
        book_price_in_basket = book_price_in_basket_tag.text    
        return book_price_in_basket

    # элемент не появляется на странице в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_TITLE_IN_BASKET), \
           "Success message is presented, but should not be"

    # элемент исчезает на странице в течение заданного времени
    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_TITLE_IN_BASKET), \
           "Success message is not disappeared"

