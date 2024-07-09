from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class CongratulationsPage(BasePage):
    CONGRATULATIONS_TEXT = (By.XPATH, "//div/h1[contains(text(), 'Congratulations!')]")
    EMAIL_SPAN = (By.XPATH, "//div/span[@data-qase-test='email']")

    def check_congratulations_page(self):
        assert "Congratulations!" in self.get_text(self.CONGRATULATIONS_TEXT), "'Congratulations' Sahifasi ochilmadi!"

    def check_email_on_page(self, email):
        assert email in self.get_text(self.EMAIL_SPAN), "Email xato!"

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("congratulations")
        )
