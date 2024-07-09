from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrdersPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h1[contains(text(), 'All-in-one')]")
    CREATE_BUTTON = (By.XPATH, "//div/a[text()='SALES_BUTTON']")
    COUNT = (By.XPATH, "Deals Qty")

    def check_page(self):
        assert "All-in-one" in self.get_text(self.HEADER_TEXT), "Sahifa ochilmadi!"

    def check_count(self):
        return self.get_text(self.COUNT)


    def click_create_button(self):
        self.click_element(self.CREATE_BUTTON)