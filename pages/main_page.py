from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h1[contains(text(), 'All-in-one')]")
    START_FREE_BUTTON = (By.XPATH, "//div/a[text()='Start for free']")

    def check_main_page(self):
        assert "All-in-one" in self.get_text(self.HEADER_TEXT), "Sahifa ochilmadi!"

    def click_start_free_button(self):
        self.click_element(self.START_FREE_BUTTON)
