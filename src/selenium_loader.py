from selenium import webdriver
from common_config import SELENIUM_DRIVER_PATH


def start():
    driver = webdriver.Chrome(SELENIUM_DRIVER_PATH)
    if driver:
        return driver
    return None
