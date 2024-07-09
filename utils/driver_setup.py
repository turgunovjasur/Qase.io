from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def setup_driver():
    service = Service(executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\'
                                      'chromedriver-win64\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver
