from selenium.webdriver.common.by import By
from .base_page import BasePage


class SalesModal(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h1[contains(text(), 'All-in-one')]")
    ORDERS_BUTTON = (By.XPATH, "//div/a[text()='SALES_BUTTON']")

    def check_modal(self):
        assert "All-in-one" in self.get_text(self.HEADER_TEXT), "Sahifa ochilmadi!"

    def click_button(self):
        self.click_element(self.ORDERS_BUTTON)