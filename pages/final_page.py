from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class FinalPage(BasePage):
    PAYMENT_TYPE_INPUT = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    STATUS_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    WAYBILL_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")

    SAVE_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")
    YES_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")

    def fill_form(self, payment_type, status):
        self.input_text(self.PAYMENT_TYPE_INPUT, payment_type)
        self.input_text(self.STATUS_INPUT, status)

    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
        self.click_element(self.YES_BUTTON)