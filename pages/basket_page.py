from .base_page import BasePage
from .locators import BasketPageLocators
from selenium import webdriver


class BasketPage(BasePage):
    # в корзине нет товаров
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "There are some items in the basket, but should not be"

    # есть текст о том, что корзина пуста
    def message_basket_is_empty(self):
        msg_container = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MSG)
        msg = msg_container.text
        assert "Your basket is empty." in msg, "No message about empty basket"
