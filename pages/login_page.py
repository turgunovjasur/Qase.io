from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_INPUT = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    PASSWORD_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    SIGN_UP_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")

    def fill_registration_form(self, email, password):
        self.input_text(self.LOGIN_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)


    def click_sign_up_button(self):
        self.click_element(self.SIGN_UP_BUTTON)

