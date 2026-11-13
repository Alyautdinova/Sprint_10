import pytest

from selenium import webdriver
from pages.block_page import BlockPage
from data.urls import Urls
from data.data_test import FROM_ADDRESS, TO_ADDRESS

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions() # создали объект для опций
    driver = webdriver.Chrome(options=chrome_options) # создали драйвер и передали в него настройки

    yield driver

    driver.quit()

@pytest.fixture
def create_default_route(driver):
    blockPage = BlockPage(driver)
    blockPage.open(Urls.BASE_URL)
    blockPage.set_address(from_address = FROM_ADDRESS, to_address = TO_ADDRESS)
