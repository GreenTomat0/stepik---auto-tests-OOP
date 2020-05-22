from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    # регистрирует пользователя
    def register_new_user(self, email, password):
        # вводим email
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)
        # вводим пароль
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)
        # подтверждаем пароль
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        # жмём на кнопку "зарегистрироваться"
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not Login Page URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no Register form"
        