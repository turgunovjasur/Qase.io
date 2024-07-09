import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.congratulations_page import CongratulationsPage
from utils.driver_setup import setup_driver


@pytest.fixture(scope="module")
def driver():
    driver = setup_driver()
    driver.get("https://qase.io/")
    yield driver
    driver.quit()


def test_registration(driver):
    email = "ksdsxbcjxj24653@gmail.com"
    password = '01443354Hsdshsdghgdgf@'
    password_confirmation = '01443354Hsdshsdghgdgf@'

    main_page = MainPage(driver)
    main_page.check_main_page()
    main_page.click_start_free_button()

    reg_page = RegistrationPage(driver)
    reg_page.fill_registration_form(email, password, password_confirmation)
    reg_page.click_sign_up_button()

    congrats_page = CongratulationsPage(driver)
    try:
        congrats_page.check_congratulations_page()
    except:
        congrats_page.take_screenshot("congratulations_error")
        raise  # Xatoni qayta ko'tarish

    congrats_page.check_email_on_page(email)
