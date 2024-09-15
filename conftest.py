import pytest
from selenium import webdriver
from config import Url

def browser_settings ():
    firefox_options = webdriver.FirefoxOptions()
    return firefox_options

@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=browser_settings())
    firefox.maximize_window()
    yield firefox
    firefox.quit()

@pytest.fixture
def navigate(driver):
    driver.get(Url.SAMOKAT_URL)
    yield driver