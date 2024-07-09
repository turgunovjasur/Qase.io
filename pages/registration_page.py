from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//div/input[@placeholder='Work email']")
    PASSWORD_INPUT = (By.XPATH, "//div/input[@placeholder='Password']")
    PASSWORD_CONFIRMATION_INPUT = (By.XPATH, "//div/input[@placeholder='Password confirmation']")
    SIGN_UP_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")

    def fill_registration_form(self, email, password, password_confirmation):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.PASSWORD_CONFIRMATION_INPUT, password_confirmation)

    def click_sign_up_button(self):
        self.click_element(self.SIGN_UP_BUTTON)
