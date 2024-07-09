from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CreateOrderPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h1[contains(text(), 'All-in-one')]")
    ORDER_DATE = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    WORKSPACE = (By.XPATH, "//div/input[@placeholder='Пароль']")
    STAFF_UNIT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    CLIENT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    PROJECT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    CONTRACT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    NEXT_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")

    def fill_form(self, order_date, workspace, staff_unit, client, project, contract):
        self.input_text(self.ORDER_DATE, order_date)
        self.input_text(self.WORKSPACE, workspace)
        self.input_text(self.STAFF_UNIT, staff_unit)
        self.input_text(self.CLIENT, client)
        self.input_text(self.PROJECT, project)
        self.input_text(self.CONTRACT, contract)


    def check_page(self):
        assert "All-in-one" in self.get_text(self.HEADER_TEXT), "Sahifa ochilmadi!"

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

