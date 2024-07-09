from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoodsPage(BasePage):
    NAME_INPUT = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    NAME_INPUT_2 = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    QTY_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    QTY_INPUT_2 = (By.XPATH, "//div/input[@placeholder='Пароль']")

    NEXT_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")

    def fill_form(self, name, qty, name_2, qty_2):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.QTY_INPUT, qty)
        self.input_text(self.NAME_INPUT, name_2)
        self.input_text(self.QTY_INPUT, qty_2)


    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)